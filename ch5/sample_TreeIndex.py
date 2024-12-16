from llama_index.core import TreeIndex, SimpleDirectoryReader
import rich

documents = SimpleDirectoryReader("files").load_data()

index = TreeIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query(
    "which are important from earth Dogs or laptop and why and why not  "
)

rich.print(response)
