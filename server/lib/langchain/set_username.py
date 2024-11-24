"""Define the set username tool"""

from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
import socketio


def create_set_username_tool(sio: socketio.Server):
    """Create the set username tool"""

    @tool
    def set_username(username: str, sid: str) -> str:
        """
        Useful for setting the username of the user of the chatbot.
        Args:
            username: The new username of the user.
            sid: The socket id of the user.
        """
        sio.emit("username", {"username": username}, room=sid)
        return "Username set to: " + username

    return set_username
