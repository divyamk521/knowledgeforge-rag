from app.llm.groq_client import get_llm


llm = get_llm()

response = llm.invoke(
    "What is a breadth-first search algorithm?"
)

print(response.content)