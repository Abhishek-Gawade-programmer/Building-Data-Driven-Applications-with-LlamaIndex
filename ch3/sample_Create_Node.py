from llama_index.core.schema import TextNode
from llama_index.core import Document

text = "The quick brown fox jumps over the lazy dog."
doc = Document(text=text)
node1 = TextNode(text=doc.text[0:16], doc_id=doc.id_)
node2 = TextNode(text=doc.text[17:30], doc_id=doc.id_)

print(node1)
print(node2)
