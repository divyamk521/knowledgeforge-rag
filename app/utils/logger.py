import json
from datetime import datetime
from pathlib import Path


LOG_FILE = Path(__file__).resolve().parents[2] / "logs" / "rag_logs.jsonl"

LOG_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)


def log_query(
    question,
    rewritten_question,
    answer,
    sources
):

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "rewritten_question": rewritten_question,
        "answer": answer,
        "sources": sources
    }

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            json.dumps(log_entry)
            + "\n"
        )

    print("Query logged successfully.")