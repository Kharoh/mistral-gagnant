"""Define the set username tool"""

from typing import Annotated
from langchain_core.tools import tool, InjectedToolArg
from langgraph.prebuilt import ToolNode
import socketio
from langgraph.prebuilt import InjectedState
from langchain_core.runnables import RunnableConfig


@tool
def set_username(
    username: str,
    state: Annotated[dict, InjectedState],
    sio: Annotated[socketio.Server, InjectedToolArg],
) -> str:
    """
    Useful for setting the username of the user of the chatbot.
    Args:
        state: The state of the chain, containing the messages and sid.
        username: The new username of the user.
    """
    try:

        print(username, state["sid"])
        print(sio)

        sio.emit(
            "chat", {"response": "Username successfully set to: " + username}
        )  # On essaie de broadcast plutot
        sio.emit("username", {"username": username})

        return (
            "Username successfully set to: "
            + username
            + ". You have to tell the user about this change."
        )
    except Exception as e:
        print(e)
        return "Error setting username."
