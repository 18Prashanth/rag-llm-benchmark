from google import genai
from app.core.config import Config
from models.base_model import BaseModel

config = Config()


class GeminiModel(BaseModel):
    def __init__(self):
        self.client = genai.Client(api_key=config.google_api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        return response.text