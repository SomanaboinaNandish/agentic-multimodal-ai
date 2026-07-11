from fastapi import UploadFile

from app.services.upload_service import UploadService
from app.services.document_service import DocumentService
from app.services.image_service import ImageService
from app.services.audio_service import AudioService

from app.agent.context_builder import ContextBuilder
from app.agent.agent_executor import AgentExecutor
from app.agent.tool_registry import ToolRegistry

from app.services.gemini_service import gemini_service


class AgentService:

    @staticmethod
    async def process(query: str, files: list[UploadFile]):

        extracted_contents = []

        uploaded = await UploadService.process(files)

        for file in files:

            suffix = file.filename.lower()

            temp_path = f"temp_{file.filename}"

            with open(temp_path, "wb") as f:
                f.write(await file.read())

            if suffix.endswith(".pdf"):

                result = DocumentService.process(temp_path)

                extracted_contents.append(result)

            elif suffix.endswith((".png", ".jpg", ".jpeg")):

                result = ImageService.process(temp_path)

                extracted_contents.append(result)

            elif suffix.endswith((".wav", ".mp3", ".m4a")):

                result = AudioService.process(temp_path)

                extracted_contents.append(result)

        context = ContextBuilder.build(query, extracted_contents)

        plan = AgentExecutor.execute(query)

        print("========== PLAN ==========")
        print(plan)

        final_answer = ""

        if "summarizer" in plan["tools"]:
            print("Calling Gemini...")

            final_answer = gemini_service.summarize(context)

            print("========== GEMINI RESPONSE ==========")
            print(final_answer)
        print("\n========== FINAL ANSWER ==========")
        print(final_answer)

        

        return {

            "success": True,

            "query": query,

            "uploaded_files": [x.model_dump() for x in uploaded],

            "context": context,

            "plan": plan,

            "response": final_answer

        }