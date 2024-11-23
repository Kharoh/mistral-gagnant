"""
Create an http server through which the chatbot can be accessed.
The requests will contain the user input and the username, 
    used as config thread_id to remember the conversation.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from langgraph.graph import StateGraph


def run_http_server(graph: StateGraph):
    """Run the server chatbot in the console."""

    app = Flask(__name__)
    CORS(app)

    @app.route("/chat", methods=["POST"])
    def chat():
        print(request)
        print(request.json)
        user_input = request.json["user_input"]
        thread_id = request.json["thread_id"]

        print(thread_id)

        event = graph.invoke(
            {"messages": [user_input]},
            config={"configurable": {"thread_id": thread_id}},
        )
        response = event["messages"][-1].content

        return jsonify({"response": response})

    app.run(debug=True, host="localhost", port=5000)
