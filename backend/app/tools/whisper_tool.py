import whisper

from app.utils.text_cleaner import TextCleaner


class WhisperTool:
    def __init__(self):
        # Load the model once when the application starts
        self.model = whisper.load_model("base")

    def transcribe(self, audio_path: str) -> str:
        result = self.model.transcribe(audio_path)

        text = result.get("text", "")

        return TextCleaner.clean(text)


whisper_tool = WhisperTool()