from llama_index.core.indices.query.query_transform.base import DecomposeQueryTransform


decompose = DecomposeQueryTransform()

query_bundle = decompose.run(
    "how men get hard fealling about the sex while materbuabating "
)


print(query_bundle.query_str)
