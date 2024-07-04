import os
import streamlit as st
import time
import openai
from langchain.document_loaders import UnstructuredURLLoader
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env (especially openai api key)

st.title("Article Research Tool")
st.sidebar.title("Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

main_placeholder = st.empty()
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key here

context = ""  # Initialize context

if process_url_clicked:
    # Load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()

    # Concatenate the articles into a single context string
    context = " ".join([doc.page_content for doc in data])  # Update to use page_content

    main_placeholder.text("Data Loading...Completed...✅✅✅")

query = main_placeholder.text_input("Question: ")
if query:
    if context:
        # Formulate the prompt with context and query
        prompt = f"{context}\n\nQuestion: {query}"

        # Query the GPT-4 model using the new API interface
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the correct model name for GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        st.header("Answer")
        st.write(response.choices[0].message["content"])

        # Display sources, if available (if your model or API provides this feature)
        # This part may not be applicable if sources are not provided by the model
