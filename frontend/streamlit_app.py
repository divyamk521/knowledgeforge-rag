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
    page_icon="📚"
)

st.title("📚 KnowledgeForge")

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

question = st.text_input(
    "Ask a question about your documents"
)

if st.button("Ask"):

    if question:

        with st.spinner("Generating answer..."):

            result = answer_question(question)

        st.subheader("Answer")

        st.write(result["answer"])

        if result["sources"]:

            st.subheader("Sources")

            for source in result["sources"]:

                st.write(
                    f"• {source['source']} "
                    f"(page {source['page']})"
                )