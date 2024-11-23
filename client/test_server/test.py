"""Lancement des tests http sur le serveur."""

import requests

if __name__ == "__main__":

    # Test the server chatbot
    response = requests.post(
        "http://localhost:5000/chat",
        json={"user_input": "Hi, my name is bob", "thread_id": "test1"},
        timeout=1000,
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={
            "user_input": "What's my own name ?",
            "thread_id": "test2",
        },
        timeout=1000,
    )
    print(response.json())

    response = requests.post(
        "http://localhost:5000/chat",
        json={
            "user_input": "Do you remember my own name ?",
            "thread_id": "test1",
        },
        timeout=1000,
    )
    print(response.json())
