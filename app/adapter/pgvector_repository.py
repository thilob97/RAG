from langchain_postgres import PGVector
from langchain_core.documents import Document
from .model_repository import ModelRepository
import os

class PGVectorRepository:
    def __init__(self):
        pgurl = os.getenv('PGVECTOR_URL')

        if not pgurl:
            print("PGVector is not set in the environment variables.")

        embeddings = ModelRepository().init_embeddings()

        self.vector_store = PGVector(
            embeddings=embeddings,
            collection_name="my_docs",
            connection=pgurl,
        )

    def get_vector_store(self):
        return self.vector_store

    def store_data(self, docs: list[Document]):
        document_ids = self.vector_store.add_documents(docs)
        print(f"Stored {len(docs)} documents in PGVector.")
        print(f"Document IDs: {document_ids}")

