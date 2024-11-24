# MODESTRAL : Hackathon QuantumBlack x MistralAI

Ce projet, réalisé dans le cadre du Hackathon QuantumBlack x MistralAI, vise à développer un chatbot spécialisé dans le conseil de clients d'une boutique en ligne de vêtements.

Nous voulons concevoir une nouvelle manière d'explorer les boutiques et de faire du shopping en ligne. Le client dispose d'une vitrine d'articles et d'une conversation avec un assistant où il expose ses envies du moment. A partir des stocks et des collections connus (ou bien restreints à un magasin, ou bien à travers tous les magasins partenaires), l'assistant lui propose une sélection de produits, l'utilisateur peut conserver ses produits dans son panier ou s'orienter vers certains produits tout en continuant à chercher des produits similaires.

Il se présente sous forme d'une interface permettant un dialogue entre le client et l'assistant.

L'assistant utilise le modèle Mistral-small pour générer une réponse.

Grâce à une Retrieval Augmented Generation (RAG), il consulte une base de données répertoriant des vêtements avec description, prix, marque... afin de proposer au client les vêtements les plus susceptibles de correspondre à ses attentes. Ce modèle peut être amélioré de nombreuses manières, nous n'avons pas eu le temps de toutes les implémenter, voici les différentes améliorations que nous avons pensées :
- Ajout automatique des articles recommandés par le retrieval dans un panier
- Possibilité de guider le prompt en "s'orientant vers un article" : l'utilisateur s'oriente vers un article qui lui a été présenté et les prochains prompts de retrieval font intervenir la description de l'article d'orientation

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

## Pré-requis

### Client

- Installer `node.js` et `npm`, lancer `npm install` à la racine de `frontend` située dans `client`.
- Lancer l'interface en écrivant à la racine de `frontend` `npm run dev`.
- Se rendre sur le lien signalé dans la console pour avoir accès au site.

### Serveur

- Installer les pré-requis, notés dans `requirements.txt`.
- Créer un fichier `.env` à la racine de `server` et y insérer la ligne `MISTRAL_API_KEY=votre_clé`.
- Lancer le serveur à l'aide de la commande `python main.py` à la racine de `server`.

Si le serveur et le client ont été lancés sur un même ordinateur, le client peut à présent faire des requêtes au serveur et notamment faire fonctionner l'assistant.