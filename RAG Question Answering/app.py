import streamlit as st
from rag import ask_question

st.title("Ahmed Farag AI Assistant")

st.write("Ask anything about Ahmed Farag.")

query = st.text_input("Enter your question")

if st.button("Ask"):

    if query:

        answer, context = ask_question(query)

        st.subheader("Answer")
        st.write(answer)

        with st.expander("Retrieved Context"):
            st.write(context)