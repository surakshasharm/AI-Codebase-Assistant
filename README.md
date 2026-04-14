# 🤖 AI Codebase Assistant — Repo Chat

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-FF6B35?style=for-the-badge)

**Chat with any GitHub repository using AI. Understand codebases instantly.**


</div>

---

## 📌 Overview

**AI Codebase Assistant (Repo Chat)** is an intelligent full-stack application that lets you have natural language conversations with any GitHub repository. Simply paste a GitHub URL and ask questions like:

- *"What does this repo do?"*
- *"Explain the authentication flow."*
- *"What are the main modules and how do they interact?"*

Powered by a **Retrieval-Augmented Generation (RAG)** pipeline, the system clones the repo, parses the code at the AST level, embeds it semantically, and answers your questions with full codebase context — instantly.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Semantic Code Search** | Embeds code chunks and retrieves the most relevant ones using FAISS vector similarity |
| 🌳 **AST-Level Parsing** | Extracts functions, classes, and structures using Python's Abstract Syntax Tree |
| 💬 **Conversational Interface** | Ask follow-up questions naturally; context is maintained across the conversation |
| 🚀 **FastAPI Backend** | Blazing-fast REST API with async support |
| ⚛️ **React + Vite Frontend** | Clean, responsive UI with real-time feedback |
| 🧹 **Smart File Filtering** | Ignores test files, `node_modules`, build artifacts, and other noise |
| 📦 **Token-Safe Chunking** | Intelligently splits large files to stay within LLM token limits |
| 🗂️ **File & Function Attribution** | Responses include source file and function references for traceability |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│                    (React + Vite Frontend)                   │
└───────────────────────────┬─────────────────────────────────┘
                            │ HTTP (Axios)
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      FastAPI Backend                         │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │  Repo Cloner │───▶│  AST Parser  │───▶│   Embedder   │  │
│  │  (GitPython) │    │  (Python AST)│    │  (OpenAI)    │  │
│  └──────────────┘    └──────────────┘    └──────┬───────┘  │
│                                                  │          │
│  ┌──────────────┐    ┌──────────────┐    ┌──────▼───────┐  │
│  │  LLM Answer  │◀───│   Retriever  │◀───│     FAISS    │  │
│  │  (GPT Model) │    │  (Top-K RAG) │    │  Vector DB   │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Core RAG Pipeline

```
GitHub URL
    │
    ▼
Clone Repo (GitPython)
    │
    ▼
Scan & Filter Files  ──── Ignore: tests, node_modules, builds
    │
    ▼
Parse with AST  ──────── Extract: functions, classes, docstrings
    │
    ▼
Chunk & Embed (OpenAI)
    │
    ▼
Store in FAISS
    │
    ▼
User Query ──▶ Embed Query ──▶ FAISS Similarity Search
                                        │
                                        ▼
                              Retrieve Top-K Chunks
                                        │
                                        ▼
                              LLM (GPT) + Structured Prompt
                                        │
                                        ▼
                              Contextual Answer ──▶ User
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI, Python 3.10+ |
| **Frontend** | React 18, Vite, Axios |
| **AI / LLM** | OpenAI GPT (chat completion) |
| **Embeddings** | OpenAI `text-embedding-ada-002` |
| **Vector Store** | FAISS (Facebook AI Similarity Search) |
| **Code Parsing** | Python `ast` module |
| **Repo Cloning** | GitPython |
| **Version Control** | Git, GitHub |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- OpenAI API Key
- Git installed on your system

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-codebase-assistant.git
cd ai-codebase-assistant
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Start the FastAPI server:

```bash
uvicorn main:app --reload --port 8000
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:5173`.

---

## 💡 Usage

1. **Open the app** in your browser at `http://localhost:5173`
2. **Paste a GitHub repository URL** (e.g., `https://github.com/tiangolo/fastapi`)
3. **Click "Index Repository"** — the system will clone, parse, and embed the codebase
4. **Ask questions** in natural language:
   - *"What is the main entry point of this project?"*
   - *"Explain how authentication is handled."*
   - *"List all API endpoints and what they do."*
   - *"What design patterns are used in this codebase?"*

---

## 📁 Project Structure

```
ai-codebase-assistant/
├── backend/
│   ├── main.py               # FastAPI app & API routes
│   ├── repo_handler.py       # GitHub cloning & file scanning
│   ├── ast_parser.py         # AST-based code extraction
│   ├── embedder.py           # OpenAI embedding logic
│   ├── vector_store.py       # FAISS indexing & retrieval
│   ├── llm_handler.py        # GPT prompt construction & response
│   ├── requirements.txt
│   └── .env                  # API keys (not committed)
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx           # Main application component
│   │   ├── components/       # Chat UI, input forms, response cards
│   │   └── api/              # Axios API calls
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## ⚙️ How It Works — Deep Dive

### 1. Repository Ingestion
The system uses **GitPython** to clone the target repository into a temporary directory. It then walks the file tree, filtering out irrelevant files using configurable ignore patterns (test files, `__pycache__`, `node_modules`, `.git`, build artifacts, etc.).

### 2. AST Parsing
Rather than treating code as plain text, the system uses Python's built-in **`ast` module** to parse source files into their syntactic structure. This extracts:
- Function definitions (names, arguments, docstrings, body)
- Class definitions and their methods
- Module-level docstrings and imports

This produces semantically meaningful chunks that are far more useful to an LLM than arbitrary line-split text.

### 3. Embedding & Indexing
Each extracted code chunk is converted into a high-dimensional vector using **OpenAI's embedding model**. These vectors are stored in a **FAISS index** for ultra-fast nearest-neighbor retrieval at query time.

### 4. Retrieval-Augmented Generation (RAG)
When a user asks a question:
1. The query is embedded using the same OpenAI model.
2. FAISS retrieves the **Top-K most semantically similar** code chunks.
3. These chunks are injected into a structured prompt alongside the user's question.
4. **GPT** generates a grounded, context-aware answer — citing specific files and functions.

---

## 🧠 Challenges & Solutions

| Challenge | Solution |
|---|---|
| Large codebases with thousands of files | Smart filtering + AST chunking to extract only meaningful structures |
| LLM token limits | Chunk size capped; only Top-K relevant chunks retrieved per query |
| Low retrieval accuracy on generic queries | Semantic embeddings + AST-level granularity improve signal quality |
| Irrelevant files polluting context | Configurable ignore list (tests, build files, dependencies) |
| Scalable pipeline design | Modular RAG architecture separates ingestion, retrieval, and generation |

---

## 🗺️ Roadmap

- [ ] Support for multi-language repos (JavaScript, TypeScript, Go, Java)
- [ ] Persistent vector store across sessions (save indexed repos)
- [ ] GitHub OAuth for private repositories
- [ ] Streaming LLM responses for faster UX
- [ ] Shareable chat sessions with permalinks
- [ ] Docker containerization for one-command deployment
- [ ] Support for local LLMs (Ollama, LLaMA)

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
# Open a Pull Request
```

Please follow [Conventional Commits](https://www.conventionalcommits.org/) and open an issue before working on major changes.

---


## 🙌 Acknowledgements

- [OpenAI](https://openai.com) for embeddings and GPT models
- [FAISS](https://github.com/facebookresearch/faiss) by Meta AI for vector search
- [FastAPI](https://fastapi.tiangolo.com) for the blazing-fast backend
- [GitPython](https://gitpython.readthedocs.io) for repository management

---

<div align="center">

Built with ❤️ to make codebases less intimidating.

⭐ **Star this repo if you found it useful!** ⭐

</div>
