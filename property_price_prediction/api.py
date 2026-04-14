from fastapi import FastAPI
from rag_engine import RAGEngine

app = FastAPI()
rag = RAGEngine("data/real_estate_knowledge.txt")

@app.get("/rag")
def get_rag(query: str):
    context = rag.retrieve(query)
    return {"context": context}