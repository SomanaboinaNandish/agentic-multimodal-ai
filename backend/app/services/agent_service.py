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

        print("\n========== RECEIVED FILES ==========")

        if not files:
            print("No files received!")

        # -----------------------------------
        # Process uploaded files
        # -----------------------------------

        for file in files:

            print("\n========== CURRENT FILE ==========")
            print("Filename:", file.filename)

            suffix = file.filename.lower()

            print("Suffix:", suffix)

            temp_path = f"temp_{file.filename}"

            with open(temp_path, "wb") as f:
                f.write(await file.read())

            print("Saved:", temp_path)

            # ---------------- PDF ----------------

            if suffix.endswith(".pdf"):

                print("✅ PDF DETECTED")

                result = DocumentService.process(temp_path)

                print("PDF Content Length:", len(result.content))

                extracted_contents.append(result)

                if result.content.strip():

                    rag_pipeline.ingest(
                        text=result.content,
                        source=file.filename
                    )

                else:

                    print(f"⚠️ Empty PDF: {file.filename}")

            # ---------------- IMAGE ----------------

            elif suffix.endswith((".png", ".jpg", ".jpeg")):

                print("✅ IMAGE DETECTED")

                result = ImageService.process(temp_path)

                print("OCR Length:", len(result.content))

                extracted_contents.append(result)

                if result.content.strip():

                    rag_pipeline.ingest(
                        text=result.content,
                        source=file.filename
                    )

                else:

                    print(f"⚠️ No OCR text found: {file.filename}")

            # ---------------- AUDIO ----------------

            elif suffix.endswith((".wav", ".mp3", ".m4a")):

                print("✅ AUDIO DETECTED")

                result = AudioService.process(temp_path)

                print("\n========== AUDIO TRANSCRIPT ==========")
                print(result.content)

                extracted_contents.append(result)

                if result.content.strip():

                    print("✅ Adding audio transcript to FAISS")

                    rag_pipeline.ingest(
                        text=result.content,
                        source=file.filename
                    )

                else:

                    print(f"⚠️ Empty transcript: {file.filename}")

            else:

                print("❌ Unsupported file:", file.filename)

        # -----------------------------------
        # Build Context
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
        # RAG
        # -----------------------------------

        if "summarizer" in plan["tools"] or "rag_qa" in plan["tools"]:

            print("\n========== SEARCHING FAISS ==========")

            retrieved_chunks = rag_pipeline.retrieve(
                query=query,
                top_k=5
            )

            print("\n========== RETRIEVED CHUNKS ==========")

            rag_context = ""

            for chunk in retrieved_chunks:

                print(chunk)

                if isinstance(chunk, dict):

                    rag_context += (
                        f"Source: {chunk['source']}\n\n"
                        f"{chunk['content']}\n\n"
                        f"{'-'*60}\n\n"
                    )

                else:

                    rag_context += chunk + "\n\n"

            conversation_memory.add_user_message(query)

            history = conversation_memory.get_formatted_history()

            print("\n========== CONVERSATION HISTORY ==========")
            print(history)

            print("\n========== CALLING GROQ ==========")

            final_answer = groq_service.answer(
                query=query,
                context=rag_context,
                history=history
            )

            conversation_memory.add_assistant_message(
                final_answer
            )

            print("\n========== GROQ RESPONSE ==========")
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
            "response": final_answer,
        }