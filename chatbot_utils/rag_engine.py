def get_answer(question, csv_data, vector_store):
    # Search CSV responses first
    for _, row in csv_data["responses"].iterrows():
        if row['query'].lower() in question.lower():
            return row['response']
    for _, row in csv_data["faq"].iterrows():
        if row['question'].lower() in question.lower():
            return row['answer']
    # If nothing found, fallback to site vector store (mock)
    docs = vector_store.get("docs", [])
    for doc in docs:
        if question.lower() in doc.lower():
            return doc
    return "Sorry, I couldn't find an exact match. Can you rephrase?"
