"""Lancement des tests http sur le serveur."""

import requests

if __name__ == "__main__":

    # Test the server chatbot
    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What do you know about LangGraph?", "thread_id": "test"},
    )
    print(response.text)

    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What is the purpose of LangGraph?", "thread_id": "test"},
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What is the purpose of LangGraph?", "thread_id": "test"},
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What is the purpose of LangGraph?", "thread_id": "test"},
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What is the purpose of LangGraph?", "thread_id": "test"},
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What is the purpose of LangGraph?", "thread_id": "test"},
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What is the purpose of LangGraph?", "thread_id": "test"},
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What is the purpose of LangGraph?", "thread_id": "test"},
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What is the purpose of LangGraph?", "thread_id": "test"},
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "What is the purpose of LangGraph?", "thread_id": "test"},
    )
    print(response.json())
