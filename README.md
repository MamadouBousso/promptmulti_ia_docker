# VoixAssistant1

Un assistant vocal intelligent développé avec Flask et une interface web moderne utilisant Tailwind CSS.

## 📋 Description

VoixAssistant1 est une application web qui permet aux utilisateurs d'interagir avec un assistant vocal via un formulaire textuel. L'application est construite avec une architecture modulaire et utilise les technologies modernes pour offrir une expérience utilisateur fluide.

## 🚀 Fonctionnalités

- **Interface Web Moderne** : Interface utilisateur responsive avec Tailwind CSS
- **Formulaire Interactif** : Zone de saisie pour les prompts vocaux
- **Gestion des Réponses** : Affichage dynamique des réponses de l'assistant
- **Architecture Modulaire** : Structure organisée avec séparation des responsabilités
- **Environnement Virtuel** : Gestion des dépendances avec uv

## 🛠️ Technologies Utilisées

- **Backend** : Flask (Python)
- **Frontend** : HTML5, JavaScript, Tailwind CSS
- **Gestion des Dépendances** : uv
- **Architecture** : Pattern MVC (Model-View-Controller)

## 📁 Structure du Projet

```
VoixAssistant1/
├── src/
│   ├── application/     # Couche application (logique métier)
│   ├── domaine/         # Couche domaine (entités et règles métier)
│   └── infrastructure/  # Couche infrastructure (base de données, API externes)
├── templates/           # Templates HTML Flask
│   └── index.html       # Page principale de l'application
├── test/               # Tests unitaires et d'intégration
├── app.py              # Point d'entrée de l'application Flask
├── pyproject.toml      # Configuration du projet et dépendances
└── README.md           # Documentation du projet
```

## 🚀 Installation et Configuration

### Prérequis

- Python 3.12+
- uv (gestionnaire de paquets Python)

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
   uv pip install flask
   ```

4. **Lancer l'application**
   ```bash
   python app.py
   ```

5. **Accéder à l'application**
   Ouvrez votre navigateur et allez à `http://localhost:5000`

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

### Fonctionnement

1. Saisissez votre question dans le champ de texte
2. Cliquez sur "Envoyer" ou appuyez sur Entrée
3. La réponse de l'assistant s'affiche automatiquement sous le formulaire

## 🔧 Configuration

### Variables d'Environnement

Aucune variable d'environnement requise pour le moment.

### Configuration Flask

L'application Flask est configurée avec :
- Mode debug activé pour le développement
- Port par défaut : 5000
- Templates dans le dossier `templates/`

## 🧪 Tests

Pour exécuter les tests (à implémenter) :
```bash
# Tests unitaires
python -m pytest test/

# Tests d'intégration
python -m pytest test/integration/
```

## 📝 API Documentation

### Routes Disponibles

#### GET/POST `/`
- **Description** : Page principale avec le formulaire d'assistant
- **Méthodes** : GET, POST
- **Paramètres** : Aucun
- **Réponse** : Page HTML avec formulaire et réponse

## 🔄 Développement

### Ajout de Nouvelles Fonctionnalités

1. **Backend** : Ajoutez la logique dans `src/application/`
2. **Frontend** : Modifiez `templates/index.html`
3. **Tests** : Créez les tests correspondants dans `test/`

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
- uv pour la gestion des dépendances

## 📞 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Contactez l'équipe de développement

---

**Version** : 1.0.0  
**Dernière mise à jour** : $(date)  
**Statut** : En développement
