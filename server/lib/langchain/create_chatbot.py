import os

from langgraph.graph import StateGraph, START, END

from langchain_mistralai import ChatMistralAI
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_mistralai import MistralAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
import socketio
from langgraph.prebuilt import ToolNode, tools_condition

from lib.langchain.create_embedding import create_embedding
from lib.langchain.retrieval import retrieve


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

    vector_store = create_embedding()

    def retrieve_tool(query: str):
        """Récupération des articles de mode en stock en fonction de la requête.
        - query: The articles to search for."""
        results = retrieve(query, vector_store)
        return {"articles": results}

    tools = [retrieve_tool]
    llm_with_tools = llm.bind_tools(tools)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Vous êtes un conseiller de vente en mode, cordial et extrêmement compétent. Votre objectif principal est d'aider les clients à trouver les vêtements parfaits qui correspondent à leurs préférences, besoins et style. Soyez amical, professionnel et patient dans toutes vos interactions. Vous avez accès à une base de données des vêtements actuellement en stock au travers d'un outil. Utilisez cet outil pour recommander des produits en fonction des besoins des clients, tels que la taille, la couleur, le budget ou l'occasion. Priorisez toujours la satisfaction du client en fournissant les meilleurs conseils possibles.\
                Si un client pose une question, répondez de manière claire et chaleureuse. Si le client décrit ses besoins ou préférences, proposez des options vestimentaires qui correspondent à sa description en utilisant l'outil. Maintenez toujours un ton positif et accueillant tout au long de la conversation. Les réponses doivent être les plus humaines possibles, sans listes ni caractères markdown. Sois exhaustif sur les exemples proposés à partir du stock.",
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


def embedding(docs):
    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
    )
    vectorstore = InMemoryVectorStore.from_texts(
        docs,
        embedding=embeddings,
    )
    return vectorstore
