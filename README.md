# 🤖 AI Codebase Assistant (Repo Chat)

An AI-powered tool that allows users to query GitHub repositories using natural language.

## 🚀 Features

- 🔍 Analyze GitHub repositories
- 💬 Ask questions about codebase
- 🧠 RAG-based architecture (Embeddings + LLM)
- ⚡ FastAPI backend + React frontend
- 📂 Code parsing using AST (functions/classes)

## 🧱 Tech Stack

- Backend: FastAPI, Python
- Frontend: React (Vite)
- LLM: OpenAI
- Vector DB: FAISS
- Parsing: AST (Python)

## 🧠 How It Works

1. Clone GitHub repo
2. Extract functions/classes
3. Generate embeddings
4. Store in FAISS
5. Retrieve relevant code
6. Answer using LLM

## ▶️ Run Locally

### Backend

```bash
cd backend
venv\Scripts\activate
python -m uvicorn app.main:app --reload