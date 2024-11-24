from flask import Flask, render_template
import socketio
import eventlet
from langgraph.graph import StateGraph


def run_socket_server(graph: StateGraph, sio: socketio.Server):
    # Create a Flask app
    app = Flask(__name__)

    # Wrap the Flask app with the Socket.IO server
    app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

    # Handle socket events
    @sio.event
    def connect(sid, environ):
        print(f"Client connected: {sid}")
        sio.emit("message", "Welcome to the server!", to=sid)

    @sio.event
    def disconnect(sid):
        print(f"Client disconnected: {sid}")

    @sio.event
    def chat(sid, data):
        user_input = data["user_input"]
        thread_id = sid

        print(user_input)
        print(thread_id)

        event = graph.invoke(
            {"messages": [user_input], "sid": sid},
            config={"configurable": {"thread_id": thread_id}},
        )
        response = event["messages"][-1].content

        print(response)

        sio.emit("chat", {"response": response}, room=sid)

    # Define a basic Flask route
    @app.route("/")
    def index():
        return "Socket.IO server is running."

    eventlet.wsgi.server(eventlet.listen(("localhost", 5000)), app, log_output=False)
