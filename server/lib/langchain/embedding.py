import pandas as pd
import csv
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

def embedding(docs):
    embeddings = MistralAIEmbeddings(model="mistral-embed",)
    vectorstore = InMemoryVectorStore.from_texts(docs, embedding=embeddings,)
    return(vectorstore)

def retrieve(query, vectorstore, k = 3):
    # Use the vectorstore as a retriever
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    # Retrieve the most similar text
    retrieved_docs = retriever.invoke(query)

    # show the retrieved document's content
    return(retrieved_docs)
