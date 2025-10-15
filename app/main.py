from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.qa import process_document, ask_question
from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str

app = FastAPI(title="AI Document Q&A")

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    text = process_document(file) 
    return {"filename": file.filename, "status": "indexed"}

@app.post("/query")
def query_document(request: QueryRequest):
    answer = ask_question(request.question)
    return {"question": request.question, "answer": answer}

