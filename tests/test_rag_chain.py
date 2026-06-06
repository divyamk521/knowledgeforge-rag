from app.chains.rag_chain import answer_question


while True:

    question = input("\nAsk a question (type exit to quit): ")

    if question.lower() == "exit":
        break

    response = answer_question(question)

    print("\nAnswer:")
    print(response)