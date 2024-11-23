from dotenv import load_dotenv
from lib.create_chatbot import create_chatbot
from lib.run_server_chat import run_server_chat

load_dotenv()


if __name__ == "__main__":
    chatbot_graph = create_chatbot()
    run_server_chat(chatbot_graph)
