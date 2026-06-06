from app.chains.rag_chain import answer_question


while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    result = answer_question(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")
    print(result["sources"])