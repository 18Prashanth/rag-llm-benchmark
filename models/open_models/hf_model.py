from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from models.base_model import BaseModel


class HFModel(BaseModel):
    def __init__(self, model_name="microsoft/phi-3-mini-4k-instruct"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32,
            device_map="auto"
        )

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.0
        )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Remove prompt from output
        return response.replace(prompt, "").strip()