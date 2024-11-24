def retrieve(query, vectorstore, k=3):
    """Retrieve the most similar text to the query from the vectorstore containing fashion articles and data."""
    # Use the vectorstore as a retriever
    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": k}
    )

    # Retrieve the most similar text
    retrieved_docs = retriever.invoke(query)

    # show the retrieved document's content
    return retrieved_docs
