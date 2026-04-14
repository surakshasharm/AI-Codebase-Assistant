from app.rag.embedder import embed_texts
from app.api.routes.ingest import vector_store

def retrieve_chunks(question: str, top_k=5):
    query_embedding = embed_texts([question])[0]

    results = vector_store.search(query_embedding, top_k)

    return results