import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.index = None
        self.documents = []

    def add_documents(self, chunks, embeddings):

        dimension = embeddings.shape[1]

        if self.index is None:
            self.index = faiss.IndexFlatL2(dimension)

        self.index.add(np.array(embeddings).astype("float32"))

        self.documents.extend(chunks)

    def search(self, query_embedding, top_k=3):

        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"),
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx < len(self.documents):

                results.append(self.documents[idx])

        return results


vector_store = VectorStore()