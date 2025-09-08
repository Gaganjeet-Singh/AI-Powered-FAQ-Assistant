import streamlit as st
import os
from langchain_helper import get_qa_chain, create_vector_db

st.title("💡 AI-Powered FAQ Assistant")

if not os.path.exists("faiss_index"):
    with st.spinner("Building knowledgebase..."):
        create_vector_db()
    st.success("Knowledgebase created successfully!")

# Question input
question = st.text_input("Ask a question:")

if question:
    chain = get_qa_chain()
    response = chain.invoke({"query": question})

    st.header("Answer:")
    st.write(response["result"])
