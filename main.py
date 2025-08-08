from fastapi import FastAPI, Request
from chatbot_utils.rag_engine import get_answer
from chatbot_utils.page_scraper import update_pages
from chatbot_utils.vector_store import load_vector_store
import pandas as pd
import os

app = FastAPI()

# Load CSV data
csv_data = {
    "responses": pd.read_csv("data/response-types-export.csv"),
    "faq": pd.read_csv("data/GSU_Grad_DQ.csv")
}

# Load the vector store for site data
vector_store = load_vector_store(["https://graduate.gsu.edu/", "https://online.gsu.edu/"])

@app.get("/chat")
def query_bot(q: str):
    if not q:
        return {"error": "No query provided."}
    answer = get_answer(q, csv_data, vector_store)
    return {"answer": answer}
