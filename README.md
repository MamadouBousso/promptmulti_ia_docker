# PromptingMulti_IA

Un assistant multi-IA intelligent développé avec Flask et une interface web moderne utilisant Tailwind CSS, intégrant les APIs OpenAI (GPT-4o), Claude (Anthropic) et Groq (Llama) pour des réponses intelligentes et comparatives.

## 📋 Description

PromptingMulti_IA est une application web qui permet aux utilisateurs d'interagir avec plusieurs assistants IA via un formulaire textuel. L'application supporte trois fournisseurs d'IA majeurs et permet de comparer leurs réponses en temps réel.

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
- **Environnement Virtuel** : Gestion des dépendances avec uv

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

## 📁 Structure du Projet

```
promptingmulti_ia/
├── src/
│   ├── application/     # Couche application (logique métier)
│   ├── domaine/         # Couche domaine (entités et règles métier)
│   └── infrastructure/  # Couche infrastructure (base de données, API externes)
│       ├── openai_client.py   # Client pour l'API OpenAI
│       ├── claude_client.py   # Client pour l'API Claude
│       └── groq_client.py     # Client pour l'API Groq
├── templates/           # Templates HTML Flask
│   └── index.html       # Page principale de l'application
├── test/               # Tests unitaires et d'intégration
├── static/             # Fichiers statiques (CSS, JS, images)
├── app.py              # Point d'entrée de l'application Flask
├── env.example         # Exemple de variables d'environnement
├── pyproject.toml      # Configuration du projet et dépendances
└── README.md           # Documentation du projet
```

## 🚀 Installation et Configuration

### Prérequis

- Python 3.12+
- uv (gestionnaire de paquets Python)
- Clés API pour au moins un des fournisseurs d'IA

### Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/MamadouBousso/promptingmulti_ia.git
   cd promptingmulti_ia
   ```

2. **Initialiser l'environnement virtuel avec uv**
   ```bash
   uv init
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
    "prompt": "Question originale"
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
    "prompt": "Question originale",
    "model": "claude-3-5-sonnet-20241022",
    "provider": "anthropic"
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
    "prompt": "Question originale",
    "model": "llama3-8b-8192",
    "provider": "groq"
  }
  ```

#### POST `/api/compare`
- **Description** : API endpoint pour comparer les trois fournisseurs
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
    "prompt": "Question originale",
    "responses": {
      "openai": {
        "success": true,
        "text": "Réponse OpenAI"
      },
      "claude": {
        "success": true,
        "text": "Réponse Claude"
      },
      "groq": {
        "success": true,
        "text": "Réponse Groq"
      }
    }
  }
  ```

### Exemples d'utilisation de l'API

#### Test OpenAI
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explique-moi l'intelligence artificielle en 3 points"}'
```

#### Test Claude
```bash
curl -X POST http://localhost:8000/api/claude \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Quels sont les avantages du machine learning ?"}'
```

#### Test Groq
```bash
curl -X POST http://localhost:8000/api/groq \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Comment fonctionne un réseau de neurones ?", "model": "llama3-8b-8192"}'
```

#### Comparaison des trois
```bash
curl -X POST http://localhost:8000/api/compare \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explique la différence entre l'IA et le machine learning"}'
```

## 🔧 Configuration

### Configuration Flask

L'application Flask est configurée avec :
- Mode debug activé pour le développement
- Port par défaut : 8000 (configurable via FLASK_PORT)
- Templates dans le dossier `templates/`
- Gestion automatique des variables d'environnement

### Configuration des Modèles

#### OpenAI
- **Modèle par défaut** : gpt-4o
- **Max tokens** : 500
- **Temperature** : 0.7
- **Messages système** : Assistant vocal intelligent et utile

#### Claude
- **Modèle par défaut** : claude-3-5-sonnet-20241022
- **Max tokens** : 500
- **Temperature** : 0.7
- **Messages système** : Assistant vocal intelligent et utile

#### Groq
- **Modèle par défaut** : llama3-8b-8192
- **Max tokens** : 500
- **Temperature** : 0.7
- **Messages système** : Assistant vocal intelligent et utile

## 🎨 Formatage Markdown

L'application supporte le rendu complet du markdown avec :

- **Titres** : `# ## ###` → Titres HTML formatés
- **Listes** : `- * +` → Listes à puces visibles
- **Listes numérotées** : `1. 2.` → Listes ordonnées
- **Gras** : `**texte**` → Texte en gras
- **Italique** : `*texte*` → Texte en italique
- **Code inline** : `` `code` `` → Code avec fond gris
- **Blocs de code** : ```...``` → Blocs de code formatés
- **Liens** : `[texte](url)` → Liens cliquables
- **Citations** : `> texte` → Citations avec bordure
- **Séparateurs** : `---` → Lignes de séparation

## 🧪 Tests

Pour exécuter les tests (à implémenter) :
```bash
# Tests unitaires
python -m pytest test/

# Tests d'intégration
python -m pytest test/integration/

# Tests des clients API
python -m pytest test/test_clients/
```

## 🔄 Développement

### Ajout de Nouvelles Fonctionnalités

1. **Backend** : Ajoutez la logique dans `src/application/`
2. **Infrastructure** : Ajoutez les clients API dans `src/infrastructure/`
3. **Frontend** : Modifiez `templates/index.html`
4. **Tests** : Créez les tests correspondants dans `test/`

### Standards de Code

- **Python** : PEP 8
- **JavaScript** : ESLint (à configurer)
- **HTML** : Validation W3C
- **CSS** : Tailwind CSS classes

### Architecture

Le projet suit une architecture en couches :

```
┌─────────────────┐
│   Templates     │ ← Interface utilisateur
├─────────────────┤
│   Application   │ ← Logique métier
├─────────────────┤
│   Infrastructure│ ← Clients API externes
└─────────────────┘
```

## 🚀 Déploiement

### Production

1. **Configuration WSGI**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

2. **Variables d'environnement**
   ```bash
   export FLASK_ENV=production
   export FLASK_DEBUG=0
   export OPENAI_API_KEY=your-production-key
   export ANTHROPIC_API_KEY=your-production-key
   export GROQ_API_KEY=your-production-key
   ```

### Docker (à implémenter)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

## 🔒 Sécurité

- **Validation des entrées** : Tous les prompts sont validés
- **Gestion des erreurs** : Erreurs API gérées gracieusement
- **Variables d'environnement** : Clés API sécurisées
- **CORS** : Configuration appropriée pour la production

## 📊 Monitoring

- **Logs** : Logs détaillés des appels API
- **Erreurs** : Gestion et affichage des erreurs
- **Performance** : Temps de réponse des APIs

## 🤝 Contribution

1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Guidelines de Contribution

- Respectez les standards de code
- Ajoutez des tests pour les nouvelles fonctionnalités
- Mettez à jour la documentation
- Testez sur plusieurs fournisseurs d'IA

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteurs

- **Mamadou Bousso** - Développement initial et maintenance

## 🙏 Remerciements

- **Flask** pour le framework web
- **Tailwind CSS** pour les styles
- **OpenAI** pour l'API GPT-4o
- **Anthropic** pour l'API Claude
- **Groq** pour l'API Llama
- **marked.js** pour le rendu markdown
- **uv** pour la gestion des dépendances

## 📞 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Contactez l'équipe de développement
- Consultez la documentation des APIs

## 🔮 Roadmap

- [ ] Support de nouveaux modèles d'IA
- [ ] Interface de chat en temps réel
- [ ] Historique des conversations
- [ ] Export des réponses
- [ ] Interface d'administration
- [ ] Métriques de performance
- [ ] Support multilingue
- [ ] Intégration de modèles locaux

---

**Version** : 2.0.0  
**Dernière mise à jour** : 28 Juin 2025  
**Statut** : Production Ready avec support multi-IA
