import chromadb
import rich
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext

db = chromadb.PersistentClient(path="chroma_database")

chroma_collection = db.get_or_create_collection("my_chroma_store")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

storage_context = StorageContext.from_defaults(vector_store=vector_store)

documents = SimpleDirectoryReader("files").load_data()
index = VectorStoreIndex.from_documents(
    documents=documents, storage_context=storage_context
)


results = chroma_collection.get()
rich.print(results)

""" We can use the next part to rebuild the Index from the ChromaDB in future sessions
index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store, 
    storage_context=storage_context
)
"""
