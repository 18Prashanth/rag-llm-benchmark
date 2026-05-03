from openai import OpenAI
from app.core.config import Config
from models.base_model import BaseModel

config = Config()


class GPTModel(BaseModel):
    def __init__(self):
        self.client = OpenAI()

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content