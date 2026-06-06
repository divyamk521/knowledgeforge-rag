from app.chains.rag_chain import answer_question


while True:

    question = input(
        "\nAsk a question (type exit to quit): "
    )

    if question.lower() == "exit":
        break

    result = answer_question(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")

    for source in result["sources"]:
        print(
            f"- {source['source']} "
            f"(page {source['page']})"
        )