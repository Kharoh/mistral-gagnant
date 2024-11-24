import os
import pandas as pd
from langchain_mistralai import MistralAIEmbeddings
from langchain.vectorstores import FAISS


def create_embedding():
    vectorstore_path = "server/data/vectorstore"
    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
    )
    # Check if vectorstore already exists
    if os.path.exists(vectorstore_path):
        vectorstore = FAISS.load_local(
            vectorstore_path,
            embeddings=embeddings,
            allow_dangerous_deserialization=True,
        )
        return vectorstore

    mode = pd.read_csv("./data/mode.csv")
    mode = mode.head(100)
    docs = [mode.iloc[i, :].to_string() for i in range(mode.shape[0])]

    vectorstore = FAISS.from_texts(
        docs,
        embedding=embeddings,
    )
    vectorstore.save_local(vectorstore_path)
    return vectorstore
