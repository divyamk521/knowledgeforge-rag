import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st

from app.core.config import settings
from app.ingestion.indexer import index_documents
from app.chains.rag_chain import answer_question


st.set_page_config(
    page_title="KnowledgeForge",
    page_icon="📚",
    layout="wide"
)

st.title("📚 KnowledgeForge")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.subheader("Upload Documents")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    save_path = (
        Path(settings.RAW_DATA_PATH)
        / uploaded_file.name
    )

    with open(save_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success(
        f"{uploaded_file.name} uploaded successfully."
    )

    with st.spinner("Indexing documents..."):
        index_documents()

    st.success("Documents indexed successfully.")

st.divider()

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input(
    "Ask about your documents..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    # Use only last 3 exchanges (6 messages)
    recent_messages = st.session_state.messages[-6:]

    chat_history = "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in recent_messages
        ]
    )

    print("\n========== CHAT HISTORY ==========")
    print(chat_history)
    print("==================================\n")

    result = answer_question(
        question=question,
        chat_history=chat_history
    )

    with st.chat_message("assistant"):
        st.write(result["answer"])

        if result["sources"]:

            st.markdown("**Sources:**")

            for source in result["sources"]:

                st.write(
                    f"• {source['source']} "
                    f"(page {source['page']})"
                )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )