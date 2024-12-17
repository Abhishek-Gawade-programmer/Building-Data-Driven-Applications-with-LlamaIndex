from llama_index.core.selectors.llm_selectors import LLMSingleSelector

options = [
    "option 1: this is good for summarization questions",
    "option 2: this is useful for precise definitions",
    "option 3: this is useful for comparing concepts",
]
selector = LLMSingleSelector.from_defaults()

decision_obj = selector.select(
    options, query="What's the definition of space?"
).selections
print(decision_obj)

decision = decision_obj[0]
print(decision.index + 1)
print(decision.reason)
