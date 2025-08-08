
import pandas as pd
from sentence_transformers import SentenceTransformer

def load_vector_store():
    df1 = pd.read_csv("data/response-types-export.csv")
    df2 = pd.read_csv("data/GSU_Grad_DQ.csv")
    texts = df1["response"].dropna().tolist() + df2["response"].dropna().tolist()
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, convert_to_tensor=True)
    return {"texts": texts, "embeddings": embeddings}
