"""Faire boucler le chatbot dans la console du serveur."""

from langgraph.graph import StateGraph


def stream_graph_updates(user_input: str, graph: StateGraph):
    """Stream graph updates to the console."""
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


def run_server_chat(graph: StateGraph):
    """Run the server chatbot in the console."""
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(user_input, graph)
        except EOFError:
            # fallback if input() is not available
            USER_INPUT = "What do you know about LangGraph?"
            print("User: " + USER_INPUT)
            stream_graph_updates(USER_INPUT, graph)
            break
