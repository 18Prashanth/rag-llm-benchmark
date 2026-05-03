from rag.vectorstore.faiss_store import load_faiss_index
from rag.ingestion.embedder import get_embedding_model
from app.services.model_service import get_model
from rag.prompts.base_prompt import PROMPT_TEMPLATE
from app.core.config import Config
from app.services.langsmith_service import trace

config = Config()



@trace
def run_rag(model_name: str, question: str):
    # Load retriever
    embedding_model = get_embedding_model()
    vectorstore = load_faiss_index(embedding_model)

    docs = vectorstore.similarity_search(question, k=config.top_k)

    # Build context
    context = "\n".join([doc.page_content for doc in docs])

    # Build prompt
    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    # Generate answer
    model = get_model(model_name)
    answer = model.generate(prompt)

    return {
        "question": question,
        "answer": answer,
        "context": context
    }