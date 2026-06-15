import pandas as pd


def show_dashboard():

    dataframe = pd.read_csv(
        "evaluation_results.csv"
    )

    print("\n===== METRICS DASHBOARD =====\n")

    print(
        f"Total Questions: {len(dataframe)}"
    )

    print(
        f"Average Confidence: "
        f"{round(dataframe['confidence_score'].mean(), 2)}%"
    )

    print(
        f"Average Response Time: "
        f"{round(dataframe['response_time'].mean(), 2)} sec"
    )

    print("\n=============================\n")


if __name__ == "__main__":
    show_dashboard()