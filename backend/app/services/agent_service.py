from fastapi import UploadFile

from app.services.upload_service import UploadService
from app.services.document_service import DocumentService
from app.services.image_service import ImageService
from app.services.audio_service import AudioService

from app.agent.context_builder import ContextBuilder
from app.agent.agent_executor import AgentExecutor

from app.services.groq_service import groq_service

from app.rag.rag_pipeline import rag_pipeline

from app.memory.conversation_memory import conversation_memory


class AgentService:

    @staticmethod
    async def process(query: str, files: list[UploadFile]):

        extracted_contents = []

        uploaded = await UploadService.process(files)

        # -----------------------------------
        # Process uploaded files
        # -----------------------------------

        for file in files:

            suffix = file.filename.lower()

            temp_path = f"temp_{file.filename}"

            with open(temp_path, "wb") as f:
                f.write(await file.read())

    # ---------------- PDF ----------------

            if suffix.endswith(".pdf"):

                result = DocumentService.process(temp_path)

                extracted_contents.append(result)

                if result.content.strip():

                    rag_pipeline.ingest(
                        text=result.content,
                        source=file.filename
                    )

                else:

                    print(f"⚠️ Skipping empty PDF: {file.filename}")

    # ---------------- IMAGE ----------------

            elif suffix.endswith((".png", ".jpg", ".jpeg")):

                result = ImageService.process(temp_path)

                extracted_contents.append(result)

    # ---------------- AUDIO ----------------

            elif suffix.endswith((".wav", ".mp3", ".m4a")):

                result = AudioService.process(temp_path)

                extracted_contents.append(result)

        # -----------------------------------
        # Build extracted context (UI)
        # -----------------------------------

        context = ContextBuilder.build(
            query,
            extracted_contents
        )

        # -----------------------------------
        # Agent Planning
        # -----------------------------------

        plan = AgentExecutor.execute(query)

        print("\n========== PLAN ==========")
        print(plan)

        final_answer = ""

        # -----------------------------------
        # RAG + Gemini
        # -----------------------------------

        if "summarizer" in plan["tools"] or "rag_qa" in plan["tools"]:

            print("\n========== SEARCHING FAISS ==========")

            retrieved_chunks = rag_pipeline.retrieve(
                query=query,
                top_k=5
            )

            print("\n========== RETRIEVED CHUNKS ==========")

            if not retrieved_chunks:
                print("No chunks retrieved!")

            rag_context = ""

            for i, chunk in enumerate(retrieved_chunks, start=1):

                print(f"\n---------- Chunk {i} ----------")
                print(chunk)

                rag_context += (
                    f"Source: {chunk['source']}\n\n"
                    f"{chunk['content']}\n\n"
                    f"{'-'*60}\n\n"
                )

            print("\n========== RAG CONTEXT ==========")
            print(rag_context)

            print("\n========== CALLING GEMINI ==========")

            # -----------------------------------
            # Conversation Memory
            # -----------------------------------

            conversation_memory.add_user_message(query)

            history = conversation_memory.get_formatted_history()

            print("\n========== CONVERSATION HISTORY ==========")
            print(history)

            final_answer = groq_service.answer(
                query=query,
                context=rag_context,
                history=history
            )

            conversation_memory.add_assistant_message(
                final_answer
            )

            print("\n========== GEMINI RESPONSE ==========")
            print(final_answer)

        print("\n========== FINAL ANSWER ==========")
        print(final_answer)

        return {

            "success": True,

            "query": query,

            "uploaded_files": [
                x.model_dump()
                for x in uploaded
            ],

            "context": context,

            "plan": plan,

            "response": final_answer

        }