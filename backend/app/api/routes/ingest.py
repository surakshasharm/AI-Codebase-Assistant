from fastapi import APIRouter
from pydantic import BaseModel
from app.ingestion.cloner import clone_repo, get_source_files
from app.ingestion.parser import parse_python_file
from app.rag.embedder import embed_texts
from app.rag.vector_store import VectorStore

router = APIRouter()

vector_store = VectorStore()  # global store

class IngestRequest(BaseModel):
    repo_url: str

@router.post("/ingest")
def ingest_repo(data: IngestRequest):
    path = clone_repo(data.repo_url)
    files = get_source_files(path)

    all_chunks = []
    texts = []

    for file in files:
        if file.endswith(".py"):
            chunks = parse_python_file(file)
            for chunk in chunks:
                text = f"""
                You are analyzing a codebase.

                File: {file}
                Function/Class: {chunk['name']}
                Lines: {chunk['start_line']} - {chunk['end_line']}

                This code belongs to a larger project.

                Code:
                {chunk['content'][:2000]}
                """
                texts.append(text)
                all_chunks.append(chunk)

    # Generate embeddings
    embeddings = embed_texts(texts)

    # Store in FAISS
    vector_store.add(embeddings, texts)

    return {
        "message": "Embeddings created successfully 🚀",
        "total_chunks": len(all_chunks)
    }