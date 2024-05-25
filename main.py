import streamlit as st
import os
from langchain_experimental.agents import create_csv_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

def main():
    load_dotenv()
    groq_qpi_key = os.getenv("GROQ_QPI_KEY")


    st.set_page_config(page_title="Ask your CSV 📈")
    st.header("Ask Your CSV 🚀")

    user_csv = st.file_uploader("Upload your CSV file here 📂", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask your question here 🤔 : ")
        llm = ChatGroq(groq_api_key= groq_qpi_key, model_name="Llama3-8b-8192")
        agent = create_csv_agent(llm, user_csv, verbose=True)

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)

if __name__ == "__main__":
    main()
