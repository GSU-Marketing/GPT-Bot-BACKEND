def load_vector_store(sites):
    # Placeholder - would use real embeddings and vector db
    from chatbot_utils.page_scraper import update_pages
    docs = update_pages(sites)
    return {"docs": docs}
