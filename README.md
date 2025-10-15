# AI Document Q&A

An AI-powered document question-answering app built with **Python, FastAPI, LangChain, OpenAI, and ChromaDB**. Users can upload documents (PDF, DOCX, TXT) and ask questions about their content.

**Tech Stack:**
- **Python 3.11**
- **FastAPI** (REST API)
- **LangChain** (retrieval + LLM)
- **OpenAI** (embeddings & LLM)
- **ChromaDB** (vector database)
- **Docker** (optional, for containerization)

---

## Features

- Upload documents (PDF, DOCX, TXT)
- Automatic text extraction and vector embedding
- Query documents with natural language
- Fully containerized with Docker for easy deployment

---

## Getting Started

### **1. Clone the Repository**

```bash
git clone https://github.com/sbkocoglu/ai-doc-search.git
cd ai-doc-search
```

### **2. Create `.env` file**

Create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

> Replace with your OpenAI API key.

---

### **3. Install Python Dependencies**

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

---

### **4. Run the FastAPI Server**

```bash
uvicorn app.main:app --reload
```

Server runs at `http://127.0.0.1:8000`.

---

## API Endpoints

### **Upload a Document**

**POST** `/upload`  

**Form-data:**  

| Key  | Value                 |
|------|----------------------|
| file | Select your document |

**Example CMD `curl`:**

```cmd
curl -X POST http://127.0.0.1:8000/upload -F "file=@C:\path\to\your\document.pdf"
```

**Response:**

```json
{
  "filename": "document.pdf",
  "status": "indexed"
}
```

---

### **Ask a Question**

**POST** `/query`  

**JSON Body:**

```json
{
  "question": "What is the main topic of the document?"
}
```

**Example CMD `curl`:**

```cmd
curl -X POST http://127.0.0.1:8000/query -H "Content-Type: application/json" -d "{\"question\":\"What is the main topic of the document?\"}"
```

**Response:**

```json
{
  "question": "What is the main topic of the document?",
  "answer": "The Ottoman Empire was a powerful empire that..."
}
```

---

## Optional: Docker Setup

**Build Docker Image:**

```bash
docker build -t ai-doc-search .
```

**Run Container:**

```bash
docker run -p 8000:8000 --env-file .env ai-doc-search
```

Optional with `docker-compose`:

```bash
docker-compose up --build
```

---

## Project Structure

```
ai-doc-search/
├─ app/
│  ├─ main.py       # FastAPI endpoints
│  └─ qa.py         # Document processing & LangChain
├─ sample_docs/     # Example documents
├─ db/              # Chroma vector DB storage
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ .env             # OpenAI API key
└─ README.md
```

