from .data_repository import DataRepository
from .schemas.state import State
from ..adapter.hub_repository import HUBRepository
from ..adapter.model_repository import ModelRepository
from ..domain.retriever_repository import RetrieverRepository
from pathlib import Path

class Data:
    def embedData(self, data_repository:'DataRepository') -> None:
        """
        This method is responsible for embedding data using the provided DataRepository instance.
        It retrieves data, splits it, and stores it in a vector store.
        """
        path = Path(__file__).parent.parent.parent / "data" / "article_seed_list.csv"
        #data = data_repository.getDataFromUrl()
        data = data_repository.getDataFromFile(str(path))
        data_repository.splitData(data)


    def generate(self):
        state: State = {
            "question": "Article that matches Fanta 12x1l Mango the best?",
            "context": [], # or some list of Document objects
            "answer": "some_answer_string"
        }

        retriever_repository = RetrieverRepository()
        retrieved_docs = retriever_repository.retrieve(state)
        state["context"] = retrieved_docs["context"]

        docs_content =  "\n\n".join(doc.page_content for doc in state["context"])

        hub_repository = HUBRepository()
        prompt = hub_repository.pull()
        
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = prompt.invoke({"question": state["question"], "context": docs_content})

        print(messages)

        model_repository = ModelRepository()
        llm = model_repository.init_model()
        response = llm.invoke(messages)

        return {"answer": response.content}
