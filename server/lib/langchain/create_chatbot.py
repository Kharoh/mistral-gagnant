import os

from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_mistralai import ChatMistralAI


def create_chatbot():
    """Create a chatbot graph that uses MistralAI to generate responses."""

    class State(TypedDict):
        messages: Annotated[list, add_messages]

    graph_builder = StateGraph(State)

    llm = ChatMistralAI(
        model="mistral-small-2409",
        temperature=0,
        max_retries=2,
        api_key=os.environ["MISTRAL_API_KEY"],
    )

    def chatbot(state: State):
        """Chatbot node that uses MistralAI to generate responses."""
        return {"messages": [llm.invoke(state["messages"])]}

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    graph = graph_builder.compile()

    return graph
