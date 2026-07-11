from app.services.image_service import ImageService

image_path = r"samples\question (1).png"

result = ImageService.process(image_path)

print("\n========== OCR Result ==========\n")
print(result["text"])
print("\n================================")
print(f"Characters: {result['length']}")