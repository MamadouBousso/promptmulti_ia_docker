# PromptMulti_IA Docker

Un assistant multi-IA intelligent développé avec Flask et une interface web moderne utilisant Tailwind CSS, intégrant les APIs OpenAI (GPT-4o), Claude (Anthropic) et Groq (Llama) pour des réponses intelligentes et comparatives. **Version Dockerisée pour un déploiement facile.**

## 📋 Description

PromptMulti_IA Docker est une application web qui permet aux utilisateurs d'interagir avec plusieurs assistants IA via un formulaire textuel. L'application supporte trois fournisseurs d'IA majeurs et permet de comparer leurs réponses en temps réel. **L'application est entièrement containerisée avec Docker pour un déploiement simplifié.**

## 🚀 Fonctionnalités

- **Interface Web Moderne** : Interface utilisateur responsive avec Tailwind CSS
- **Multi-IA Support** : Intégration OpenAI (GPT-4o), Claude (Anthropic) et Groq (Llama)
- **Comparaison en Temps Réel** : Compare les réponses des trois modèles simultanément
- **Rendu Markdown** : Affichage riche avec support complet du formatage markdown
- **Sélection de Modèles** : Choix spécifique des modèles Llama pour Groq
- **Formulaire Interactif** : Zone de saisie pour les prompts textuels
- **API REST Complète** : Endpoints pour chaque fournisseur d'IA
- **Gestion des Erreurs** : Interface utilisateur avec gestion des erreurs robuste
- **Indicateur de Chargement** : Feedback visuel pendant la génération
- **Architecture Modulaire** : Structure organisée avec séparation des responsabilités
- **Docker Ready** : Containerisation complète avec Docker et Docker Compose
- **Gestion des Dépendances** : Utilisation de uv pour une installation rapide

## 🛠️ Technologies Utilisées

- **Backend** : Flask (Python)
- **Frontend** : HTML5, JavaScript, Tailwind CSS
- **IA** : 
  - OpenAI API (GPT-4o)
  - Anthropic API (Claude 3.5 Sonnet)
  - Groq API (Llama 3.1, Llama 4 Scout)
- **Markdown** : marked.js pour le rendu
- **Gestion des Dépendances** : uv
- **Variables d'Environnement** : python-dotenv
- **Architecture** : Pattern MVC (Model-View-Controller)
- **Containerisation** : Docker, Docker Compose

## 📁 Structure du Projet

```
promptmulti_ia_docker/
├── src/
│   ├── application/     # Couche application (logique métier)
│   ├── domaine/         # Couche domaine (entités et règles métier)
│   └── infrastructure/  # Couche infrastructure (base de données, API externes)
│       ├── openai_client.py   # Client pour l'API OpenAI
│       ├── claude_client.py   # Client pour l'API Claude
│       └── groq_client.py     # Client pour l'API Groq
├── templates/           # Templates HTML Flask
│   └── index.html       # Page principale de l'application
├── static/              # Fichiers statiques (CSS, JS, images)
├── test/               # Tests unitaires et d'intégration
├── app.py              # Point d'entrée de l'application Flask
├── Dockerfile          # Configuration Docker
├── docker-compose.yml  # Orchestration Docker Compose
├── docker-build.sh     # Script de déploiement Docker
├── .dockerignore       # Fichiers exclus du build Docker
├── env.example         # Exemple de variables d'environnement
├── pyproject.toml      # Configuration du projet et dépendances
├── DOCKER.md           # Documentation Docker
└── README.md           # Documentation du projet
```

## 🐳 Déploiement avec Docker (Recommandé)

### Prérequis

- Docker installé sur votre machine
- Variables d'environnement configurées (optionnel)

### Déploiement Rapide

#### Option 1: Script automatique

```bash
# Cloner le repository
git clone https://github.com/MamadouBousso/promptmulti_ia_docker.git
cd promptmulti_ia_docker

# Rendre le script exécutable
chmod +x docker-build.sh

# Lancer le script
./docker-build.sh
```

#### Option 2: Docker Compose (recommandé)

```bash
# Cloner le repository
git clone https://github.com/MamadouBousso/promptmulti_ia_docker.git
cd promptmulti_ia_docker

# Construire et lancer avec docker-compose
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter
docker-compose down
```

#### Option 3: Docker manuel

```bash
# Cloner le repository
git clone https://github.com/MamadouBousso/promptmulti_ia_docker.git
cd promptmulti_ia_docker

# Construire l'image
docker build -t promptmulti_ia_docker .

# Lancer le conteneur
docker run -d \
  --name promptmulti_ia_docker-container \
  -p 8000:8000 \
  -e OPENAI_API_KEY="votre_clé_openai" \
  -e ANTHROPIC_API_KEY="votre_clé_claude" \
  -e GROQ_API_KEY="votre_clé_groq" \
  promptmulti_ia_docker
```

### Configuration des variables d'environnement

#### Option 1: Fichier .env

Créez un fichier `.env` à la racine du projet :

```env
OPENAI_API_KEY=votre_clé_openai_ici
ANTHROPIC_API_KEY=votre_clé_claude_ici
GROQ_API_KEY=votre_clé_groq_ici
```

Puis lancez avec :

```bash
docker-compose --env-file .env up -d
```

#### Option 2: Variables d'environnement système

```bash
export OPENAI_API_KEY="votre_clé_openai"
export ANTHROPIC_API_KEY="votre_clé_claude"
export GROQ_API_KEY="votre_clé_groq"
```

### Accès à l'application

Une fois le conteneur lancé, l'application est accessible sur :
- **URL locale** : http://localhost:8000 (ou le port configuré)
- **URL réseau** : http://votre_ip:8000

## 🚀 Installation Locale (Sans Docker)

### Prérequis

- Python 3.12+
- uv (gestionnaire de paquets Python)
- Clés API pour au moins un des fournisseurs d'IA

### Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/MamadouBousso/promptmulti_ia_docker.git
   cd promptmulti_ia_docker
   ```

2. **Initialiser l'environnement virtuel avec uv**
   ```bash
   uv venv .venv
   source .venv/bin/activate  # Sur macOS/Linux
   # ou
   .venv\Scripts\activate     # Sur Windows
   ```

3. **Installer les dépendances**
   ```bash
   uv pip install flask openai anthropic groq python-dotenv
   ```

4. **Configurer les variables d'environnement**
   ```bash
   # Copier le fichier d'exemple
   cp env.example .env
   
   # Éditer le fichier .env et ajouter vos clés API
   # Voir la section Configuration des APIs ci-dessous
   ```

5. **Lancer l'application**
   ```bash
   python app.py
   ```

6. **Accéder à l'application**
   Ouvrez votre navigateur et allez à `http://localhost:8000`

## 🔑 Configuration des APIs

### Obtenir les clés API

#### OpenAI (GPT-4o)
1. Allez sur [OpenAI Platform](https://platform.openai.com/)
2. Créez un compte ou connectez-vous
3. Allez dans la section "API Keys"
4. Créez une nouvelle clé API
5. Copiez la clé et ajoutez-la dans votre fichier `.env`

#### Claude (Anthropic)
1. Allez sur [Anthropic Console](https://console.anthropic.com/)
2. Créez un compte ou connectez-vous
3. Allez dans la section "API Keys"
4. Créez une nouvelle clé API
5. Copiez la clé et ajoutez-la dans votre fichier `.env`

#### Groq (Llama)
1. Allez sur [Groq Console](https://console.groq.com/)
2. Créez un compte ou connectez-vous
3. Allez dans la section "API Keys"
4. Créez une nouvelle clé API
5. Copiez la clé et ajoutez-la dans votre fichier `.env`

### Variables d'Environnement

Créez un fichier `.env` à la racine du projet :

```env
# Configuration OpenAI (GPT-4o)
OPENAI_API_KEY=sk-your-actual-openai-api-key-here

# Configuration Anthropic (Claude)
ANTHROPIC_API_KEY=sk-ant-your-actual-anthropic-api-key-here

# Configuration Groq (Llama)
GROQ_API_KEY=gsk-your-actual-groq-api-key-here

# Configuration Flask
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_PORT=8000
```

**Note** : Vous n'avez besoin que d'une seule clé API pour commencer. L'application fonctionnera avec les fournisseurs configurés.

## 🎯 Utilisation

### Interface Utilisateur

L'interface se compose de :

1. **Sélecteur d'IA** : Choisissez entre OpenAI, Claude, Groq ou comparer tous
2. **Sélecteur de Modèle Groq** : Choisissez le modèle Llama spécifique (visible uniquement pour Groq)
3. **Zone de saisie** : Champ de texte pour entrer vos questions/prompts
4. **Bouton d'envoi** : Pour soumettre votre requête
5. **Zone de réponse** : Affichage de la réponse avec formatage markdown
6. **Zone de comparaison** : Affichage côte à côte des réponses des trois modèles
7. **Indicateur de chargement** : Animation pendant la génération
8. **Zone d'erreur** : Affichage des messages d'erreur

### Fonctionnement

1. **Sélection du fournisseur** : Choisissez OpenAI, Claude, Groq ou "Comparer tous"
2. **Sélection du modèle** : Si vous choisissez Groq, sélectionnez le modèle Llama
3. **Saisie du prompt** : Entrez votre question dans le champ de texte
4. **Envoi** : Cliquez sur "Envoyer" ou appuyez sur Entrée
5. **Affichage** : La réponse s'affiche avec un formatage markdown complet

### Modèles Disponibles

#### Groq (Llama)
- **Llama 3.1 8B** : Modèle rapide et efficace
- **Llama 3.1 70B** : Modèle plus puissant
- **Llama 4 Scout 13B** : Modèle équilibré
- **Llama 4 Scout 17B** : Modèle performant
- **Llama 4 Scout 32B** : Modèle haute performance
- **Llama 4 Scout 65B** : Modèle ultra-performant

## 📝 API Documentation

### Routes Disponibles

#### GET `/`
- **Description** : Page principale avec l'interface utilisateur
- **Méthodes** : GET
- **Réponse** : Page HTML avec formulaire et interface

#### POST `/api/chat`
- **Description** : API endpoint pour les appels OpenAI
- **Méthodes** : POST
- **Content-Type** : application/json
- **Paramètres** :
  ```json
  {
    "prompt": "Votre question ici"
  }
  ```
- **Réponse** :
  ```json
  {
    "success": true,
    "text": "Réponse générée par OpenAI",
    "model": "gpt-4o"
  }
  ```

#### POST `/api/claude`
- **Description** : API endpoint pour les appels Claude
- **Méthodes** : POST
- **Content-Type** : application/json
- **Paramètres** :
  ```json
  {
    "prompt": "Votre question ici"
  }
  ```
- **Réponse** :
  ```json
  {
    "success": true,
    "text": "Réponse générée par Claude",
    "model": "claude-3-5-sonnet-20241022"
  }
  ```

#### POST `/api/groq`
- **Description** : API endpoint pour les appels Groq
- **Méthodes** : POST
- **Content-Type** : application/json
- **Paramètres** :
  ```json
  {
    "prompt": "Votre question ici",
    "model": "llama3-8b-8192"
  }
  ```
- **Réponse** :
  ```json
  {
    "success": true,
    "text": "Réponse générée par Groq",
    "model": "llama3-8b-8192"
  }
  ```

#### POST `/api/compare`
- **Description** : API endpoint pour comparer les trois modèles
- **Méthodes** : POST
- **Content-Type** : application/json
- **Paramètres** :
  ```json
  {
    "prompt": "Votre question ici"
  }
  ```
- **Réponse** :
  ```json
  {
    "success": true,
    "prompt": "Votre question ici",
    "responses": {
      "openai": {
        "success": true,
        "text": "Réponse OpenAI",
        "model": "gpt-4o"
      },
      "claude": {
        "success": true,
        "text": "Réponse Claude",
        "model": "claude-3-5-sonnet-20241022"
      },
      "groq": {
        "success": true,
        "text": "Réponse Groq",
        "model": "llama3-8b-8192"
      }
    }
  }
  ```

## 📋 Commandes Docker Utiles

### Gestion des conteneurs

```bash
# Voir les conteneurs en cours
docker ps

# Voir les logs
docker logs promptmulti_ia_docker-container

# Arrêter le conteneur
docker stop promptmulti_ia_docker-container

# Redémarrer le conteneur
docker restart promptmulti_ia_docker-container

# Supprimer le conteneur
docker rm promptmulti_ia_docker-container

# Supprimer l'image
docker rmi promptmulti_ia_docker
```

### Avec Docker Compose

```bash
# Voir les services
docker-compose ps

# Voir les logs
docker-compose logs -f app

# Redémarrer le service
docker-compose restart app

# Arrêter et supprimer
docker-compose down

# Reconstruire l'image
docker-compose build --no-cache
```

## 🔍 Dépannage

### Problèmes Docker

#### Problème de port déjà utilisé
Si le port 8000 est déjà utilisé, changez-le dans `docker-compose.yml` :
```yaml
ports:
  - "8080:8000"  # Port externe:Port interne
```

#### Problème de permissions
```bash
# Donner les bonnes permissions au script
chmod +x docker-build.sh
```

#### Reconstruire l'image
```bash
# Supprimer l'ancienne image
docker rmi promptmulti_ia_docker

# Reconstruire
docker build -t promptmulti_ia_docker .
```

#### Vérifier les logs
```bash
# Logs en temps réel
docker logs -f promptmulti_ia_docker-container

# Derniers logs
docker logs --tail 50 promptmulti_ia_docker-container
```

### Problèmes Généraux

#### Erreur "API non disponible"
- Vérifiez que vos clés API sont correctement configurées
- Assurez-vous que les variables d'environnement sont définies
- Vérifiez la validité de vos clés API

#### Erreur de connexion
- Vérifiez que l'application est bien lancée
- Vérifiez le port utilisé (8000 par défaut)
- Vérifiez les logs pour plus de détails

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. **Fork** le projet
2. **Créez** une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. **Commitez** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Poussez** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrez** une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Mamadou Bousso**
- GitHub: [@MamadouBousso](https://github.com/MamadouBousso)
- Email: mamadou.bousso@example.com

## 🙏 Remerciements

- [OpenAI](https://openai.com/) pour l'API GPT-4o
- [Anthropic](https://www.anthropic.com/) pour l'API Claude
- [Groq](https://groq.com/) pour l'API Llama
- [Flask](https://flask.palletsprojects.com/) pour le framework web
- [Tailwind CSS](https://tailwindcss.com/) pour le styling
- [uv](https://github.com/astral-sh/uv) pour la gestion des dépendances Python

## 📞 Support

Si vous rencontrez des problèmes ou avez des questions :

1. Consultez la section [Dépannage](#dépannage)
2. Vérifiez les [Issues](https://github.com/MamadouBousso/promptmulti_ia_docker/issues) existantes
3. Créez une nouvelle [Issue](https://github.com/MamadouBousso/promptmulti_ia_docker/issues/new) si nécessaire

---

**⭐ N'oubliez pas de donner une étoile au projet si vous l'aimez !**
