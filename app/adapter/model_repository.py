from langchain.chat_models import init_chat_model
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dataclasses import dataclass

@dataclass
class ModelRepository:
    def init_model(self, model_name: str = "gemini-2.0-flash", model_provider: str = "google_genai"):
        return init_chat_model(
            model=model_name,
            model_provider=model_provider,
        )

    def init_embeddings(self, embedding_model: str = "models/embedding-001"):
        return GoogleGenerativeAIEmbeddings(model=embedding_model)

