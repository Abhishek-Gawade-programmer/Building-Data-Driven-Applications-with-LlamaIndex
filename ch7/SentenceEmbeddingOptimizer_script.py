from llama_index.core.postprocessor.optimizer import SentenceEmbeddingOptimizer

optimizer = SentenceEmbeddingOptimizer(percentile_cutoff=0.8, threshold_cutoff=0.7)
query_engine = index.as_query_engine(optimizer=optimizer)


response = query_engine.query("<your_query_here>")
