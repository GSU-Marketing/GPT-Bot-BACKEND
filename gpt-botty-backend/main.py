
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from chatbot_utils.rag_engine import answer_query
from chatbot_utils.page_scraper import crawl_and_update
from chatbot_utils.vector_store import load_vector_store
import uvicorn

app = FastAPI()

# Allow frontend origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vector_store = load_vector_store()

@app.get("/chat")
def chat(q: str):
    return {"answer": answer_query(q, vector_store)}

@app.post("/refresh")
def refresh():
    crawl_and_update()
    return {"status": "updated"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
