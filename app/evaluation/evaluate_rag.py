import pandas as pd

from app.chains.rag_chain import answer_question
from app.evaluation.sample_questions import TEST_QUESTIONS


def evaluate():

    results = []

    for question in TEST_QUESTIONS:

        response = answer_question(question)

        results.append(
            {
                "question": question,
                "answer": response["answer"],
                "confidence_score": response["confidence_score"],
                "response_time": response["response_time"]
            }
        )

    dataframe = pd.DataFrame(results)

    print("\nEvaluation Results:\n")
    print(dataframe)

    dataframe.to_csv(
        "evaluation_results.csv",
        index=False
    )

    print(
        "\nSaved results to evaluation_results.csv"
    )


if __name__ == "__main__":
    evaluate()