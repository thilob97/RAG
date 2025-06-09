from .schemas.state import State
from ..adapter.pgvector_repository import PGVectorRepository

class RetrieverRepository:
    def retrieve(self, state: State) :
        vector_store = PGVectorRepository().get_vector_store()
        retrieved_docs = vector_store.similarity_search(state["question"])
        return {"context": retrieved_docs}

