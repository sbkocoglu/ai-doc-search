from pyexpat import model
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
import os
from PyPDF2 import PdfReader
from docx import Document
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set. Check your .env file.")

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectordb = Chroma(persist_directory="db", embedding_function=embeddings)

def extract_text(file):
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        return "\n".join([page.extract_text() for page in reader.pages])
    elif file.filename.endswith(".docx"):
        doc = Document(file.file)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return file.file.read().decode("utf-8")

def process_document(file):
    text = extract_text(file)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    vectordb.add_texts(chunks)
    return text

def ask_question(question):
    retriever = vectordb.as_retriever(search_kwargs={"k":3})
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-5-nano",temperature=0),
        chain_type="stuff",
        retriever=retriever
    )
    return qa.invoke({"query": question})
