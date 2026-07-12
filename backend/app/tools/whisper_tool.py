import whisper

from app.utils.text_cleaner import TextCleaner


class WhisperTool:

    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, audio_path: str) -> str:

        print("\n========== TRANSCRIBING AUDIO ==========")

        result = self.model.transcribe(audio_path)

        print(result)

        text = result.get("text", "")

        print("\n========== TRANSCRIPT ==========")
        print(text)

        return TextCleaner.clean(text)


whisper_tool = WhisperTool()