import streamlit as st

from app.chains.rag_chain import answer_question


st.set_page_config(
    page_title="KnowledgeForge",
    page_icon="📚"
)

st.title("📚 KnowledgeForge")

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
                    f"• {source['source']} (page {source['page']})"
                )