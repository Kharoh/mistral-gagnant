from dotenv import load_dotenv
from lib.langchain.create_chatbot import create_chatbot
from lib.http.run_socket_server import run_socket_server
from lib.http.create_sio import create_sio

load_dotenv()


if __name__ == "__main__":
    sio = create_sio()
    chatbot_graph = create_chatbot(sio)
    run_socket_server(chatbot_graph, sio)
