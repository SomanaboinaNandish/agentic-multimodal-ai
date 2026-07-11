from app.rag.chunker import Chunker

text = "Hello World " * 300

chunks = Chunker.split(text)

print("Chunks:", len(chunks))

for i, c in enumerate(chunks):

    print(f"\nChunk {i+1}")

    print(c[:80])