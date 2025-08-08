def get_answer(question, csv_data, vector_store):
    print(f"[DEBUG] Received query: {question}")

    # 1. Try answering using the CSVs
    for df_name, df in csv_data.items():
        for _, row in df.iterrows():
            for col in row.index:
                cell = str(row[col])
                if question.lower() in cell.lower():
                    print(f"[DEBUG] Matched in CSV: {df_name} at column: {col}")
                    return f"(from {df_name}) {cell}"

    # 2. Try from vector store if CSV doesn't answer
    try:
        docs = vector_store.similarity_search(question, k=3)
        context = "\n\n".join([doc.page_content for doc in docs])
        print(f"[DEBUG] Context from vector store:\n{context}")
        return f"(from site content)\n{context}"
    except Exception as e:
        print(f"[ERROR] Failed during vector search: {e}")
        return "Error while retrieving site content."
