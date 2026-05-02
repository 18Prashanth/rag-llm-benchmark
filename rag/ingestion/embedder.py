from app.core.config import Config
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings

config = Config()


def get_embedding_model():
    if config.embedding_provider == "openai":
        return OpenAIEmbeddings(model=config.embedding_model_name)

    return HuggingFaceEmbeddings(model_name=config.embedding_model_name)