from app.tools.whisper_tool import whisper_tool


class AudioService:

    @staticmethod
    def process(audio_path: str):

        transcript = whisper_tool.transcribe(audio_path)

        return {
            "success": True,
            "transcript": transcript,
            "length": len(transcript)
        }