import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

class RAGEngine:
    def __init__(self, file_path):
        loader = TextLoader(file_path, encoding="utf-8")
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        docs = splitter.split_documents(documents)

        os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vectorstore = FAISS.from_documents(docs, embeddings)

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0
        )

    def query(self, query):
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": 5})
        docs = retriever.invoke(query) 

        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a legal property assistant.

STRICT RULES:
- Give SHORT and PRECISE answers
- ONLY answer what is asked
- Do NOT include:
  - market trends
  - recommendations
  - risks
- Use bullet points if needed
- Stick to legal facts only

Context:
{context}

Question:
{query}

Answer:
"""

        response = self.llm.invoke(prompt)
        return response.content.strip()

current_dir = os.path.dirname(__file__)
knowledge_file_path = os.path.join(current_dir, "data", "real_estate_knowledge.txt")
try:
    rag = RAGEngine(knowledge_file_path)
except Exception as e:
    print(f"Warning: Failed to load RAG engine. {e}")
    rag = None
