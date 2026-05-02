from rag.ingestion.loader import load_pdfs
from rag.ingestion.chunker import chunk_documents
from rag.ingestion.embedder import get_embedding_model
from rag.vectorstore.faiss_store import build_faiss_index


DATA_PATH = "./data"  # Path to your PDF files


def main():
    print("📄 Loading PDFs...")
    documents = load_pdfs(DATA_PATH)

    print(f"Loaded {len(documents)} pages")

    print("✂️ Chunking...")
    chunks = chunk_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("🔢 Loading embeddings...")
    embedding_model = get_embedding_model()

    print("🧠 Building index...")
    build_faiss_index(chunks, embedding_model)

    print("✅ Done!")


if __name__ == "__main__":
    main()