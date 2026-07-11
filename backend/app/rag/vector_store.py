import os
import pickle

import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.index = None
        self.documents = []

        self.storage_dir = "storage"
        self.index_path = os.path.join(
            self.storage_dir,
            "faiss.index"
        )
        self.documents_path = os.path.join(
            self.storage_dir,
            "documents.pkl"
        )

        os.makedirs(self.storage_dir, exist_ok=True)

    def add_documents(self, chunks, embeddings):

        dimension = embeddings.shape[1]

        if self.index is None:
            self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            np.array(embeddings).astype("float32")
        )

        self.documents.extend(chunks)

    def search(self, query_embedding, top_k=5):

        if self.index is None:
            return []

        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"),
            top_k
        )

        results = []

        for idx in indices[0]:

            if 0 <= idx < len(self.documents):
                results.append(self.documents[idx])

        return results

    # -------------------------
    # Save FAISS
    # -------------------------

    def save(self):

        if self.index is None:
            return

        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(self.documents_path, "wb") as f:
            pickle.dump(self.documents, f)

        print("✅ FAISS index saved.")

    # -------------------------
    # Load FAISS
    # -------------------------

    def load(self):

        if (
            os.path.exists(self.index_path)
            and os.path.exists(self.documents_path)
        ):

            self.index = faiss.read_index(
                self.index_path
            )

            with open(self.documents_path, "rb") as f:
                self.documents = pickle.load(f)

            print(
                f"✅ Loaded {len(self.documents)} chunks from disk."
            )

    # -------------------------
    # Clear FAISS
    # -------------------------

    def clear(self):

        self.index = None
        self.documents = []

        if os.path.exists(self.index_path):
            os.remove(self.index_path)

        if os.path.exists(self.documents_path):
            os.remove(self.documents_path)

        print("🗑️ Vector store cleared.")


vector_store = VectorStore()