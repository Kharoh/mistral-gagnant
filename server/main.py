from dotenv import load_dotenv
from lib.langchain.create_chatbot import create_chatbot
from lib.langchain.run_server_chat import run_server_chat
from lib.http.run_http_server import run_http_server

load_dotenv()


if __name__ == "__main__":
    chatbot_graph = create_chatbot()
    run_http_server(chatbot_graph)
