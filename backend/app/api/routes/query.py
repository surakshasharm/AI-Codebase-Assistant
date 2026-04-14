from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.retriever import retrieve_chunks
from app.rag.generator import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def query_repo(data: QueryRequest):
    chunks = retrieve_chunks(data.question, top_k=10)

    answer = generate_answer(data.question, chunks)

    return {
    "answer": answer,
    "sources": [
        {
            "preview": chunk[:200]
        } for chunk in chunks[:3]
    ]
}