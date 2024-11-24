import os

from langgraph.graph import StateGraph, START, END

from langchain_mistralai import ChatMistralAI
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
import socketio
from langgraph.prebuilt import ToolNode, tools_condition


def create_chatbot(sio: socketio.Server):
    """Create a chatbot graph that uses MistralAI to generate responses."""

    class State(TypedDict):
        """Define the state of the chatbot.
        - messages: A list of messages in the conversation.
        - sid: The socket id of the user.
        """

        # messages: A list of messages in the conversation.
        messages: Annotated[list, add_messages]
        # sid: The socket id of the user.
        sid: str

    graph_builder = StateGraph(State)

    llm = ChatMistralAI(
        model="mistral-small-2409",
        temperature=0,
        max_retries=2,
        api_key=os.environ["MISTRAL_API_KEY"],
    )

    tools = []
    llm_with_tools = llm.bind_tools(tools)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a cordial and highly knowledgeable fashion sales advisor. Your primary goal is to assist customers in finding the perfect clothing items that match their preferences, needs, and style. Be friendly, professional, and patient in all your interactions. \
                You have access to a database of clothing items currently in stock. Use this tool to recommend specific products based on the customer's requirements, such as size, color, budget, or occasion. Always prioritize providing the best possible advice to ensure customer satisfaction. \
                If a customer asks a question, respond clearly and warmly. If they describe their needs or preferences, suggest clothing options that align with their description. When necessary, ask clarifying questions to understand their needs better. Maintain a positive and welcoming tone throughout the conversation.",
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    def chatbot(state: State):
        """Chatbot node that uses MistralAI to generate responses."""
        graph = prompt | llm_with_tools
        response = graph.invoke(state)
        return {"messages": response}

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("tools", ToolNode(tools))
    graph_builder.add_edge("tools", "chatbot")
    graph_builder.add_conditional_edges(
        "chatbot",
        tools_condition,
        {"tools": "tools", END: END},
    )
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    memory = MemorySaver()
    graph = graph_builder.compile(checkpointer=memory)

    return graph
