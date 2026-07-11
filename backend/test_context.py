from app.agent.context_builder import ContextBuilder
from app.models.extracted_content import ExtractedContent


def main():
    contents = [
        ExtractedContent(
            source="PDF",
            content="This document explains Retrieval-Augmented Generation (RAG)."
        ),
        ExtractedContent(
            source="IMAGE",
            content="Architecture diagram showing embeddings and vector database."
        ),
        ExtractedContent(
            source="AUDIO",
            content="The speaker discusses LangChain, FastAPI, and AI agents."
        ),
    ]

    context = ContextBuilder.build(
        query="Summarize all uploaded content.",
        contents=contents,
    )

    print("\n========== UNIFIED CONTEXT ==========\n")
    print(context)
    print("\n=====================================")


if __name__ == "__main__":
    main()