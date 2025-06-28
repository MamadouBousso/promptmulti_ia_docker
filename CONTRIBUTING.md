# Guide de Contribution

Merci de votre intérêt pour contribuer à PromptingMulti_IA ! Ce document fournit des lignes directrices pour contribuer au projet.

## 🚀 Comment Contribuer

### Types de Contributions

Nous accueillons plusieurs types de contributions :

- **Rapports de bugs** : Signalez des problèmes que vous rencontrez
- **Demandes de fonctionnalités** : Proposez de nouvelles idées
- **Améliorations de la documentation** : Aidez à améliorer la documentation
- **Code** : Contribuez du code pour corriger des bugs ou ajouter des fonctionnalités
- **Tests** : Ajoutez ou améliorez les tests
- **Traductions** : Aidez à traduire l'interface

## 🛠️ Configuration de l'Environnement de Développement

### Prérequis

- Python 3.12+
- Git
- uv (gestionnaire de paquets Python)

### Installation

1. **Fork le repository**
   ```bash
   # Allez sur GitHub et fork le projet
   # Puis clonez votre fork
   git clone https://github.com/VOTRE_USERNAME/promptingmulti_ia.git
   cd promptingmulti_ia
   ```

2. **Configurez l'environnement virtuel**
   ```bash
   uv init
   uv pip install -e ".[dev]"
   ```

3. **Configurez les variables d'environnement**
   ```bash
   cp env.example .env
   # Éditez .env avec vos clés API
   ```

4. **Vérifiez l'installation**
   ```bash
   python app.py
   # L'application devrait démarrer sur http://localhost:8000
   ```

## 📝 Standards de Code

### Python

- **Style** : Suivez PEP 8
- **Formatage** : Utilisez Black
- **Linting** : Utilisez Flake8
- **Type hints** : Utilisez MyPy

```bash
# Formater le code
black .

# Vérifier le style
flake8 .

# Vérifier les types
mypy .
```

### JavaScript

- **Style** : Suivez les conventions ES6+
- **Linting** : Utilisez ESLint (à configurer)

### HTML/CSS

- **Validation** : Validez le HTML avec W3C
- **CSS** : Utilisez Tailwind CSS classes

## 🧪 Tests

### Exécuter les Tests

```bash
# Tous les tests
pytest

# Tests avec couverture
pytest --cov=src

# Tests spécifiques
pytest test/test_openai_client.py
```

### Écrire des Tests

- Créez des tests pour chaque nouvelle fonctionnalité
- Utilisez des mocks pour les appels API externes
- Testez les cas d'erreur et les cas limites

Exemple de test :

```python
import pytest
from src.infrastructure.openai_client import OpenAIClient

def test_openai_client_initialization():
    """Test l'initialisation du client OpenAI."""
    client = OpenAIClient()
    assert client is not None
    assert hasattr(client, 'client')
```

## 🔄 Workflow de Contribution

### 1. Créer une Branche

```bash
# Assurez-vous d'être sur main et à jour
git checkout main
git pull origin main

# Créez une nouvelle branche
git checkout -b feature/nouvelle-fonctionnalite
# ou
git checkout -b fix/correction-bug
```

### 2. Développer

- Écrivez votre code
- Ajoutez des tests
- Mettez à jour la documentation si nécessaire
- Vérifiez que tout fonctionne

### 3. Commiter

```bash
# Ajoutez vos changements
git add .

# Committez avec un message descriptif
git commit -m "feat: ajoute le support pour l'API Gemini

- Ajoute le client Gemini
- Implémente l'endpoint /api/gemini
- Ajoute les tests unitaires
- Met à jour la documentation"
```

### 4. Pousser et Créer une Pull Request

```bash
git push origin feature/nouvelle-fonctionnalite
```

Puis allez sur GitHub et créez une Pull Request.

## 📋 Format des Messages de Commit

Nous utilisons [Conventional Commits](https://www.conventionalcommits.org/) :

- `feat:` : Nouvelle fonctionnalité
- `fix:` : Correction de bug
- `docs:` : Changements dans la documentation
- `style:` : Changements de formatage (pas de changement fonctionnel)
- `refactor:` : Refactoring du code
- `test:` : Ajout ou modification de tests
- `chore:` : Tâches de maintenance

Exemples :
```
feat: ajoute le support pour l'API Gemini
fix: corrige l'affichage des listes markdown
docs: met à jour la documentation API
test: ajoute des tests pour le client Claude
```

## 🔍 Revue de Code

### Avant de Soumettre

- [ ] Le code suit les standards du projet
- [ ] Les tests passent
- [ ] La documentation est mise à jour
- [ ] Le code est testé localement
- [ ] Les changements sont documentés dans le CHANGELOG

### Processus de Revue

1. **Soumettez votre PR** avec une description claire
2. **Attendez la revue** d'un mainteneur
3. **Répondez aux commentaires** et faites les modifications nécessaires
4. **Une fois approuvé**, votre PR sera mergé

## 🐛 Signaler des Bugs

### Avant de Signaler

- Vérifiez que le bug n'a pas déjà été signalé
- Testez avec la dernière version
- Vérifiez la documentation

### Template de Rapport de Bug

```markdown
**Description du bug**
Description claire et concise du bug.

**Étapes pour reproduire**
1. Allez à '...'
2. Cliquez sur '...'
3. Faites défiler jusqu'à '...'
4. Voir l'erreur

**Comportement attendu**
Description de ce qui devrait se passer.

**Comportement actuel**
Description de ce qui se passe actuellement.

**Captures d'écran**
Si applicable, ajoutez des captures d'écran.

**Environnement**
- OS: [ex: macOS, Windows, Linux]
- Navigateur: [ex: Chrome, Firefox, Safari]
- Version: [ex: 2.0.0]

**Informations supplémentaires**
Toute autre information pertinente.
```

## 💡 Demander une Fonctionnalité

### Template de Demande de Fonctionnalité

```markdown
**Problème**
Description claire du problème que cette fonctionnalité résoudrait.

**Solution proposée**
Description claire de la solution souhaitée.

**Alternatives considérées**
Description des alternatives que vous avez considérées.

**Contexte supplémentaire**
Toute autre information ou contexte.
```

## 🏷️ Labels et Milestones

### Labels Utilisés

- `bug` : Problème à corriger
- `enhancement` : Amélioration de fonctionnalité
- `documentation` : Amélioration de la documentation
- `good first issue` : Bon point de départ pour les nouveaux contributeurs
- `help wanted` : Besoin d'aide
- `question` : Question sur le projet
- `wontfix` : Ne sera pas corrigé

## 📞 Obtenir de l'Aide

- **Issues** : Utilisez les issues GitHub pour les questions
- **Discussions** : Utilisez les discussions GitHub pour les conversations générales
- **Email** : Contactez directement les mainteneurs si nécessaire

## 🎉 Reconnaissance

Tous les contributeurs seront reconnus dans :
- Le fichier README.md
- Les releases GitHub
- La documentation du projet

## 📄 Licence

En contribuant, vous acceptez que vos contributions soient sous la même licence que le projet (MIT).

---

Merci de contribuer à PromptingMulti_IA ! 🚀 