from langchain_community.vectorstores import FAISS
import os
from app.core.config import Config

config = Config()


def build_faiss_index(chunks, embedding_model):
    vectorstore = FAISS.from_documents(chunks, embedding_model)

    os.makedirs(config.index_path, exist_ok=True)
    vectorstore.save_local(config.index_path)

    return vectorstore


def load_faiss_index(embedding_model):
    return FAISS.load_local(
        config.index_path,
        embedding_model,
        allow_dangerous_deserialization=True
    )