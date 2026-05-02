from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import Config

config = Config()


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap
    )

    return splitter.split_documents(documents)