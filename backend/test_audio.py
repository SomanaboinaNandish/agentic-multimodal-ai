from app.services.audio_service import AudioService

audio_path = r"C:\Users\nandi\Desktop\agentic-multimodal-ai\backend\samples\record-1782457223978.wav"

result = AudioService.process(audio_path)

print("\n========== Audio Transcript ==========\n")
print(result["transcript"])
print("\n======================================")
print(f"Characters: {result['length']}")