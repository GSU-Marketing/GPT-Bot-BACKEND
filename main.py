from fastapi import FastAPI, Request
from chatbot_utils.rag_engine import get_answer
from chatbot_utils.page_scraper import update_pages
from chatbot_utils.vector_store import load_vector_store
import pandas as pd

app = FastAPI()

# Load CSV data only (fast)
csv_data = {
    "responses": pd.read_csv("data/response-types-export.csv"),
    "faq": pd.read_csv("data/GSU_Grad_DQ.csv")
}

# Do not crawl at startup
vector_store = None

def get_answer(query, csv_data, vector_store):
    print(f"[DEBUG] Received query: {query}")

    try:
        # 1. Try to find a response from the CSVs first
        for df_name, df in csv_data.items():
            for _, row in df.iterrows():
                if query.lower() in str(row.to_string()).lower():
                    return f"(from CSV: {df_name}) {row.to_string()}"

        # 2. Otherwise, use vector store (RAG from site content)
        docs = vector_store.similarity_search(query, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        print(f"[DEBUG] Top context:\n{context}")

        # Simulated GPT-style output
        return f"(from site data)\nAnswer based on: {context}"

    except Exception as e:
        print(f"[ERROR] Exception in get_answer: {e}")
        return "An error occurred while processing your query."



@app.post("/update")
def refresh_pages():
    global vector_store
    urls = ["https://graduate.gsu.edu/", "https://online.gsu.edu/"]
    vector_store = load_vector_store(urls)
    return {"status": "Vector store updated with latest pages"}
