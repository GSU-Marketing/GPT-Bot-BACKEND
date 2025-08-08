from fastapi import FastAPI
from chatbot_utils.vector_store import load_vector_store
from chatbot_utils.page_scraper import update_vector_store
from chatbot_utils.rag_engine import get_answer
from chatbot_utils.utils import load_csv_data

app = FastAPI()

# ✅ Load CSVs and vector store once when the server starts
csv_data = load_csv_data()
vector_store = load_vector_store()

@app.post("/update")
def update():
    global vector_store
    vector_store = update_vector_store()
    print(f"[DEBUG] Vector store loaded: {type(vector_store)}")
    return {"status": "Vector store updated with latest pages"}

@app.get("/chat")
def query_bot(q: str):
    print(f"[DEBUG] Received query: {q}")
    answer = get_answer(q, csv_data, vector_store)
    return {"answer": answer}
