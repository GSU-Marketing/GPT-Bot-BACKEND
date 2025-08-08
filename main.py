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

@app.get("/chat")
def query_bot(q: str):
    if not q:
        return {"error": "No query provided."}
    answer = get_answer(q, csv_data, vector_store)
    return {"answer": answer}





@app.post("/update")
def refresh_pages():
    global vector_store
    urls = ["https://graduate.gsu.edu/", "https://online.gsu.edu/"]
    vector_store = load_vector_store(urls)
    return {"status": "Vector store updated with latest pages"}
