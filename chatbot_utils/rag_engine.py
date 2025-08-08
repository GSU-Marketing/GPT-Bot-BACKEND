
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch

model = SentenceTransformer("all-MiniLM-L6-v2")

def answer_query(question, store):
    query_embedding = model.encode(question, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, store["embeddings"])[0]
    best_idx = torch.argmax(scores).item()
    return store["texts"][best_idx]
