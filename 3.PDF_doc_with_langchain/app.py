import streamlit as st
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv

# Modern LangChain Imports
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_classic.chains.question_answering import load_qa_chain
from langchain_core.prompts import PromptTemplate

load_dotenv()

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    # Swapped FAISS for Chroma - this will save to a folder called "chroma_db"
    vectorstore = Chroma.from_texts(
        texts=chunks, 
        embedding=embeddings, 
        persist_directory="./chroma_db"
    )
    return vectorstore

def get_conversation_chain():
    prompt_template = """Answer the question as detailed as possible from the provided context. Make sure to provide all the details. If the answer is not in the provided context, just say, "Answer is not available in the context", don't provide a wrong answer.\n\n
    Context: \n{context} \n
    Question: \n{question} \n
    
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Load the Chroma database we saved earlier
    new_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    docs = new_db.similarity_search(user_question)

    chain = get_conversation_chain()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )
    st.write("Reply: ", response["output_text"])

def main():
    st.set_page_config(page_title="Chat with Multiple PDF")
    st.header("Chat with Multiple PDF using Gemini")

    user_question = st.text_input("Ask a question from the pdf files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files and Click on Submit & Process", accept_multiple_files=True, type=["pdf"])
        if st.button("Submit & Process"):
            if pdf_docs is not None:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vectorstore(text_chunks)
                    st.success("PDF files processed successfully!")

if __name__ == "__main__":
    main()