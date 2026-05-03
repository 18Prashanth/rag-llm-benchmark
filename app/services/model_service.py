from models.closed_models.gpt import GPTModel
from models.closed_models.gemini import GeminiModel
from models.open_models.hf_model import HFModel


def get_model(model_name: str):
    if model_name == "gpt":
        return GPTModel()
    elif model_name == "gemini":
        return GeminiModel()
    elif model_name == "phi3":
        return HFModel()
    else:
        raise ValueError(f"Unsupported model: {model_name}")