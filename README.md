# PromptMulti_IA Docker

Un assistant multi-IA intelligent développé avec Flask et une interface web moderne utilisant Tailwind CSS, intégrant les APIs OpenAI (GPT-4o), Claude (Anthropic) et Groq (Llama) pour des réponses intelligentes et comparatives. **Version Dockerisée avec historique des conversations.**

## 📋 Description

PromptMulti_IA Docker est une application web complète qui permet aux utilisateurs d'interagir avec plusieurs assistants IA via un formulaire textuel. L'application supporte trois fournisseurs d'IA majeurs et permet de comparer leurs réponses en temps réel. **L'application est entièrement containerisée avec Docker et inclut un système d'historique des conversations persistant.**

## 🚀 Fonctionnalités

### 🤖 **Multi-IA Support**
- **OpenAI (GPT-4o)** : Intégration complète avec l'API OpenAI
- **Claude (Anthropic)** : Support de Claude 3.5 Sonnet
- **Groq (Llama)** : Support de multiples modèles Llama (3.1 8B, 70B, 4 Scout)
- **Mode Comparaison** : Comparaison simultanée des réponses des trois fournisseurs

### 💾 **Système d'Historique**
- **Base de données SQLite** : Stockage persistant des conversations
- **Recherche avancée** : Recherche par mot-clé dans l'historique
- **Statistiques en temps réel** : Métriques d'utilisation et de performance
- **Gestion des conversations** : Visualisation, suppression, détails complets
- **Métadonnées enrichies** : Temps de réponse, tokens utilisés, modèles

### 🎨 **Interface Utilisateur**
- **Design moderne** : Interface responsive avec Tailwind CSS
- **Rendu Markdown** : Support complet du formatage Markdown
- **Mode sombre/clair** : Interface adaptative
- **Indicateurs de chargement** : Feedback visuel en temps réel
- **Gestion d'erreurs** : Messages d'erreur clairs et informatifs

### 🐳 **Containerisation Docker**
- **Déploiement simplifié** : Une seule commande pour lancer l'application
- **Volumes persistants** : Base de données et fichiers de configuration
- **Variables d'environnement** : Configuration sécurisée des clés API
- **Docker Compose** : Orchestration complète avec health checks

## 🛠️ Installation et Configuration

### Prérequis
- Docker et Docker Compose installés
- Clés API pour au moins un fournisseur IA (OpenAI, Claude, ou Groq)

### 1. Cloner le dépôt
```bash
git clone https://github.com/MamadouBousso/promptmulti_ia_docker.git
cd promptmulti_ia_docker
```

### 2. Configurer les clés API
```bash
# Copier le fichier d'exemple
cp env.example .env

# Éditer le fichier .env avec vos clés API
nano .env
```

**Clés API requises :**
- `OPENAI_API_KEY` : Obtenez sur [OpenAI Platform](https://platform.openai.com/api-keys)
- `ANTHROPIC_API_KEY` : Obtenez sur [Anthropic Console](https://console.anthropic.com/)
- `GROQ_API_KEY` : Obtenez sur [Groq Console](https://console.groq.com/)

### 3. Lancer l'application

#### Option A : Docker Compose (Recommandé)
```bash
docker-compose up -d
```

#### Option B : Docker manuel
```bash
# Construire l'image
docker build -t promptmulti_ia_docker .

# Lancer le conteneur
docker run -d \
  --name promptmulti_ia_docker-container \
  -p 9000:8000 \
  -v $(pwd)/data:/app/data \
  --env-file .env \
  promptmulti_ia_docker
```

#### Option C : Script automatisé
```bash
chmod +x docker-build.sh
./docker-build.sh
```

### 4. Accéder à l'application
Ouvrez votre navigateur et allez sur : **http://localhost:9000**

## 📊 Utilisation

### Interface Principale
1. **Choisissez un fournisseur IA** : OpenAI, Claude, Groq, ou "Comparer tous"
2. **Saisissez votre question** dans le champ de texte
3. **Cliquez sur "Envoyer"** pour obtenir une réponse
4. **Consultez l'historique** en bas de page

### Fonctionnalités Avancées
- **Recherche** : Utilisez la barre de recherche pour trouver des conversations
- **Statistiques** : Consultez les métriques d'utilisation en temps réel
- **Détails** : Cliquez sur "Voir" pour afficher les détails d'une conversation
- **Suppression** : Supprimez les conversations inutiles

### API REST
L'application expose plusieurs endpoints API :

```bash
# Historique des conversations
GET /api/history

# Détails d'une conversation
GET /api/history/{id}

# Recherche dans l'historique
GET /api/history/search?q={term}

# Statistiques
GET /api/stats

# Supprimer une conversation
DELETE /api/history/{id}

# Nettoyer l'historique ancien
POST /api/cleanup
```

## 🏗️ Architecture

```
promptmulti_ia_docker/
├── app.py                 # Application Flask principale
├── Dockerfile            # Configuration Docker
├── docker-compose.yml    # Orchestration Docker
├── .env                  # Variables d'environnement
├── src/
│   └── infrastructure/
│       ├── database.py   # Gestionnaire de base de données SQLite
│       ├── openai_client.py
│       ├── claude_client.py
│       └── groq_client.py
├── templates/
│   └── index.html        # Interface utilisateur
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js        # Logique frontend
└── data/                 # Base de données SQLite (volume Docker)
```

## 🔧 Configuration Avancée

### Variables d'Environnement
```bash
# Configuration Flask
FLASK_ENV=production
FLASK_PORT=8000

# Modèles par défaut
OPENAI_MODEL="gpt-4o"
CLAUDE_MODEL="claude-3-5-sonnet-20241022"
GROQ_MODEL="llama3-8b-8192"

# Paramètres de génération
MAX_TOKENS=500
TEMPERATURE=0.7
```

### Base de Données
L'application utilise SQLite pour stocker :
- **Conversations** : prompts, timestamps, modèles utilisés
- **Réponses** : textes, métadonnées, temps de réponse, tokens
- **Statistiques** : métriques d'utilisation et de performance

### Sécurité
- Les clés API sont stockées dans des variables d'environnement
- Le fichier `.env` est exclu du dépôt Git
- Validation des entrées utilisateur
- Gestion sécurisée des erreurs

## 📈 Statistiques et Monitoring

L'application fournit des statistiques détaillées :
- **Total des conversations**
- **Taux de succès**
- **Conversations par jour**
- **Performance par fournisseur**
- **Utilisation des tokens**

## 🐛 Dépannage

### Problèmes Courants

**1. Clients IA non disponibles**
```bash
# Vérifiez que les clés API sont configurées
cat .env | grep API_KEY
```

**2. Port déjà utilisé**
```bash
# Changez le port dans docker-compose.yml
ports:
  - "9001:8000"  # Au lieu de 9000:8000
```

**3. Base de données corrompue**
```bash
# Supprimez et recréez le volume
docker-compose down
rm -rf data/
docker-compose up -d
```

**4. Problèmes de permissions**
```bash
# Donnez les bonnes permissions au dossier data
chmod 755 data/
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🙏 Remerciements

- **OpenAI** pour GPT-4o
- **Anthropic** pour Claude
- **Groq** pour l'accès aux modèles Llama
- **Flask** pour le framework web
- **Tailwind CSS** pour le design
- **SQLite** pour la base de données

## 📞 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Consultez la documentation dans le code
- Vérifiez les logs Docker : `docker logs promptmulti_ia_docker-container`

---

**🎯 Application prête pour la production avec toutes les fonctionnalités avancées !**
