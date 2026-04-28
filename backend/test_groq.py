import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
print(f"API Key loaded: {api_key[:20]}..." if api_key else "No API key found")
print(f"API Key length: {len(api_key)}" if api_key else "N/A")

try:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )
    print("LLM initialized successfully")
    
    response = llm.invoke("Say hello in one word")
    print(f"Response: {response.content}")
    print("✅ Groq API is working!")
except Exception as e:
    print(f"❌ Error: {e}")
