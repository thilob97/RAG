from langchain_community.document_loaders.csv_loader import CSVLoader
import bs4
from ..adapter.pgvector_repository import PGVectorRepository
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class DataRepository:
    def __init__(self):
        self.name = "Core Module"

    def getDataFromUrl(self) -> list[Document]:
        bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))
        loader = WebBaseLoader(
            web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
                bs_kwargs={"parse_only": bs4_strainer},
            )

        docs = loader.load()
       
        assert len(docs) == 1
        print(f"Total characters: {len(docs[0].page_content)}")
        
        return docs

    def getDataFromFile(self, file_path: str) -> list[Document]:
        loader = CSVLoader(file_path=file_path, encoding='unicode_escape')
        docs = loader.load()
        return docs

        
    def splitData(self, docs: list[Document]):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # chunk size (characters)
            chunk_overlap=200,  # chunk overlap (characters)
            add_start_index=True,  # track index in original document
        )
        all_splits = text_splitter.split_documents(docs)

        print(f"Split blog post into {len(all_splits)} sub-documents.")

        pgvector_module = PGVectorRepository()
        pgvector_module.store_data(all_splits)



