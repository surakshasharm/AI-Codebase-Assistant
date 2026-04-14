from fastapi import APIRouter
from app.rag.retriever import retrieve_chunks
from app.rag.generator import generate_answer

router = APIRouter()

SUGGESTED = [
    "What does this repo do?",
    "Explain main functionality",
    "How is authentication handled?",
    "What are key modules?"
]

@router.get("/summary")
def get_summary():
    chunks = retrieve_chunks("Explain this entire repository", top_k=10)

    answer = generate_answer(
        "Give a high-level summary of this codebase",
        chunks
    )

    return {
        "summary": answer,
        "suggested_questions": SUGGESTED
    }