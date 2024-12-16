from llama_index.core import KeywordTableIndex, SimpleDirectoryReader
import rich

documents = SimpleDirectoryReader("files").load_data(show_progress=True)
index = KeywordTableIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What famous buildings were in ancient Rome?")
rich.print(response)
