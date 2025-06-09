from langchain_core.documents import Document
from typing_extensions import TypedDict

class State(TypedDict):
    question: str
    context: list[Document]
    answer: str
