from rag.ingestion.embedder import get_embedding_model
from rag.vectorstore.faiss_store import load_faiss_index
from app.core.config import Config

config = Config()


def test_query(query):
    embedding_model = get_embedding_model()
    vectorstore = load_faiss_index(embedding_model)

    docs = vectorstore.similarity_search(query, k=config.top_k)

    print("\n🔎 Query:", query)
    print("=" * 50)

    for i, doc in enumerate(docs):
        print(f"\nResult {i+1}:")
        print(doc.page_content)


if __name__ == "__main__":
    test_query("What should you do at a pedestrian crossing?")