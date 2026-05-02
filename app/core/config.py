import os
import yaml
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self._load_env()
        self._load_yaml()

    def _load_env(self):
        self.embedding_model = os.getenv("EMBEDDING_MODEL")
        self.vector_db = os.getenv("VECTOR_DB")
        self.faiss_index_path = os.getenv("FAISS_INDEX_PATH")

    def _load_yaml(self):
        with open("configs/retriever_config.yaml", "r") as f:
            data = yaml.safe_load(f)

        self.chunk_size = data["retriever"]["chunk_size"]
        self.chunk_overlap = data["retriever"]["chunk_overlap"]
        self.top_k = data["retriever"]["top_k"]

        self.embedding_provider = data["embedding"]["provider"]
        self.embedding_model_name = data["embedding"]["model"]

        self.vectorstore_type = data["vectorstore"]["type"]
        self.index_path = data["vectorstore"]["index_path"]