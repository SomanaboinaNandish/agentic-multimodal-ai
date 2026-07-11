from app.services.document_service import DocumentService
pdf_path = r"C:\Users\nandi\Desktop\agentic-multimodal-ai\backend\samples\Nandish_IIIT Sricity_Gen AI.pdf"

result = DocumentService.process(pdf_path)

print("\n========== PDF Extraction Result ==========\n")
print(result["text"])
print("\n===========================================")
print(f"Characters Extracted: {result['length']}")