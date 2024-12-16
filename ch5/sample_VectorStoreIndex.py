from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import rich

documents = SimpleDirectoryReader("files").load_data()

index = VectorStoreIndex.from_documents(documents)
rich.print(index)
print("Index created successfully!")
