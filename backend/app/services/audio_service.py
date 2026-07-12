from app.models.extracted_content import ExtractedContent
from app.tools.whisper_tool import whisper_tool


class AudioService:

    @staticmethod
    def process(audio_path: str) -> ExtractedContent:

        transcript = whisper_tool.transcribe(audio_path)

        print("\n========== AUDIO TRANSCRIPT ==========")
        print(transcript)

        return ExtractedContent(
            source="audio",
            content=transcript
        )