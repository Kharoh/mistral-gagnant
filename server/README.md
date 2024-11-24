# MODESTRAL : Hackathon QuantumBlack x MistralAI

Ce projet, réalisé dans le cadre du Hackathon QuantumBlack x MistralAI, vise à développer un chatbot spécialisé dans le conseil de clients d'une boutique en ligne de vêtements.
Il se présente sous forme d'une interface permettant un dialogue entre le client et l'assistant.
L'assistant utilise le modèle Mistral-small pour générer une réponse.
Grâce à un Retrieval Augmented Generation (RAG), il consulte une base de données répertoriant des vêtements avec description, prix, marque... afin de proposer au client les vêtements les plus susceptibles de correspondre à ses attentes.
Les messages sont gardés en mémoire au cours d'une même session, permettant de construire un entre le client et l'assistant, et d'affiner les recommandations.

# Structure du projet

Le projet se découpe en deux dossiers principaux : server (backend) et client (frontend).

* server :
    * data : jeux de données
    * lib
        * http : session utilisateur
        * langchain : chatbot et RAG

* client : interface utilisateur
    * frontend : site web de Modestral
    * images : images pour le site

## Tutoriels langchain

https://python.langchain.com/docs/tutorials/

## Installation des dépendances langchain (getting started de langchain)

pip install langchain_mistralai

## Structure .env

Créer un fichier .env à la racine de server/

```MISTRAL_API_KEY=votre_clé```