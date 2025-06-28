# VoixAssistant1

Un assistant vocal intelligent développé avec Flask et une interface web moderne utilisant Tailwind CSS, intégrant l'API OpenAI pour des réponses intelligentes.

## 📋 Description

VoixAssistant1 est une application web qui permet aux utilisateurs d'interagir avec un assistant vocal via un formulaire textuel. L'application utilise l'API OpenAI pour générer des réponses intelligentes et contextuelles.

## 🚀 Fonctionnalités

- **Interface Web Moderne** : Interface utilisateur responsive avec Tailwind CSS
- **Formulaire Interactif** : Zone de saisie pour les prompts vocaux
- **Intégration OpenAI** : Génération de réponses intelligentes via l'API OpenAI
- **API REST** : Endpoint `/api/chat` pour les appels programmatiques
- **Gestion des Erreurs** : Interface utilisateur avec gestion des erreurs
- **Indicateur de Chargement** : Feedback visuel pendant la génération
- **Architecture Modulaire** : Structure organisée avec séparation des responsabilités
- **Environnement Virtuel** : Gestion des dépendances avec uv

## 🛠️ Technologies Utilisées

- **Backend** : Flask (Python)
- **Frontend** : HTML5, JavaScript, Tailwind CSS
- **IA** : OpenAI API (GPT-3.5-turbo)
- **Gestion des Dépendances** : uv
- **Variables d'Environnement** : python-dotenv
- **Architecture** : Pattern MVC (Model-View-Controller)

## 📁 Structure du Projet

```
VoixAssistant1/
├── src/
│   ├── application/     # Couche application (logique métier)
│   ├── domaine/         # Couche domaine (entités et règles métier)
│   └── infrastructure/  # Couche infrastructure (base de données, API externes)
│       └── openai_client.py  # Client pour l'API OpenAI
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
- Clé API OpenAI

### Installation

1. **Cloner le repository**
   ```bash
   git clone <url-du-repo>
   cd VoixAssistant1
   ```

2. **Initialiser l'environnement virtuel avec uv**
   ```bash
   uv init
   ```

3. **Installer les dépendances**
   ```bash
   uv pip install flask openai python-dotenv
   ```

4. **Configurer les variables d'environnement**
   ```bash
   # Copier le fichier d'exemple
   cp env.example .env
   
   # Éditer le fichier .env et ajouter votre clé OpenAI
   # OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

5. **Lancer l'application**
   ```bash
   python app.py
   ```

6. **Accéder à l'application**
   Ouvrez votre navigateur et allez à `http://localhost:5000`

## 🔑 Configuration OpenAI

### Obtenir une clé API OpenAI

1. Allez sur [OpenAI Platform](https://platform.openai.com/)
2. Créez un compte ou connectez-vous
3. Allez dans la section "API Keys"
4. Créez une nouvelle clé API
5. Copiez la clé et ajoutez-la dans votre fichier `.env`

### Variables d'Environnement

Créez un fichier `.env` à la racine du projet :

```env
# Configuration OpenAI
OPENAI_API_KEY=sk-your-actual-api-key-here

# Configuration Flask
FLASK_ENV=development
FLASK_DEBUG=True
```

## 🎯 Utilisation

### Interface Utilisateur

L'interface se compose de :

1. **Zone de saisie** : Champ de texte pour entrer vos questions/prompts
   - Bordure couleur slate-800
   - Largeur 100%
   - Coins arrondis
   - Padding de 0.5rem

2. **Bouton d'envoi** : Pour soumettre votre requête
   - Style moderne avec hover effect
   - Couleur slate-800

3. **Zone de réponse** : Affichage de la réponse de l'assistant
   - Marge supérieure de 1rem
   - Fond gris clair
   - Bordure subtile

4. **Indicateur de chargement** : Animation pendant la génération
5. **Zone d'erreur** : Affichage des messages d'erreur

### Fonctionnement

1. Saisissez votre question dans le champ de texte
2. Cliquez sur "Envoyer" ou appuyez sur Entrée
3. L'application appelle l'API OpenAI
4. La réponse intelligente s'affiche automatiquement

## 📝 API Documentation

### Routes Disponibles

#### GET/POST `/`
- **Description** : Page principale avec le formulaire d'assistant
- **Méthodes** : GET, POST
- **Paramètres** : Aucun
- **Réponse** : Page HTML avec formulaire et réponse

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
- **Codes d'erreur** :
  - 400 : Prompt manquant ou OpenAI non configuré
  - 500 : Erreur serveur

### Exemple d'utilisation de l'API

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Quel est le temps qu'il fait aujourd'hui ?"}'
```

## 🔧 Configuration

### Configuration Flask

L'application Flask est configurée avec :
- Mode debug activé pour le développement
- Port par défaut : 5000
- Templates dans le dossier `templates/`
- Gestion automatique des variables d'environnement

### Configuration OpenAI

Le client OpenAI est configuré avec :
- Modèle par défaut : gpt-3.5-turbo
- Max tokens : 500
- Temperature : 0.7
- Messages système pour définir le comportement de l'assistant

## 🧪 Tests

Pour exécuter les tests (à implémenter) :
```bash
# Tests unitaires
python -m pytest test/

# Tests d'intégration
python -m pytest test/integration/
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
   ```

### Docker (à implémenter)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contribution

1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteurs

- **Mamadou Bousso** - Développement initial

## 🙏 Remerciements

- Flask pour le framework web
- Tailwind CSS pour les styles
- OpenAI pour l'API d'intelligence artificielle
- uv pour la gestion des dépendances

## 📞 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Contactez l'équipe de développement

---

**Version** : 1.1.0  
**Dernière mise à jour** : $(date)  
**Statut** : En développement avec intégration OpenAI
