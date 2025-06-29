# 📁 Dossier Static - Frontend Assets

Ce dossier contient tous les fichiers statiques (CSS, JavaScript, images) de l'application Assistant Multi-IA.

## 📂 Structure des fichiers

```
static/
├── css/
│   └── styles.css          # Styles CSS personnalisés
├── js/
│   └── app.js             # Module JavaScript principal
└── README.md              # Ce fichier
```

## 🎨 CSS (`css/styles.css`)

### Fonctionnalités
- **Styles Markdown** : Formatage complet pour le rendu markdown
- **Animations** : Transitions et animations fluides
- **Responsive Design** : Adaptation mobile et desktop
- **Accessibilité** : Classes pour l'accessibilité
- **États interactifs** : Hover, focus, disabled states

### Classes principales
- `.prose` - Formatage markdown
- `.response-content` - Zones de réponse
- `.ai-provider-option` - Options de sélection d'IA
- `.form-input` - Champs de formulaire
- `.btn-primary` - Boutons principaux
- `.loading-spinner` - Indicateur de chargement
- `.error-message` - Messages d'erreur

## ⚡ JavaScript (`js/app.js`)

### Architecture
Le code JavaScript est organisé en **classe ES6** avec une architecture modulaire :

```javascript
class AssistantApp {
    constructor() {
        // Initialisation
    }
    
    // Méthodes organisées par responsabilité
    bindEvents() { /* ... */ }
    handleQuery() { /* ... */ }
    renderMarkdown() { /* ... */ }
    // ...
}
```

### Fonctionnalités principales

#### 🔧 Configuration
- **CONFIG** : Configuration centralisée des endpoints et options
- **Endpoints API** : URLs des différents services d'IA
- **Options Markdown** : Configuration de marked.js

#### 🎯 Gestion des événements
- **Changement de fournisseur** : Affichage/masquage du sélecteur Groq
- **Soumission de formulaire** : Gestion des requêtes API
- **Validation** : Vérification des données avant envoi

#### 🌐 Appels API
- **makeApiCall()** : Méthode générique pour les requêtes HTTP
- **Gestion d'erreurs** : Traitement des erreurs réseau et API
- **Configuration dynamique** : Adaptation selon le fournisseur sélectionné

#### 📝 Rendu Markdown
- **renderMarkdown()** : Conversion markdown vers HTML
- **Gestion d'erreurs** : Fallback en cas d'échec du rendu
- **Sécurité** : Configuration sécurisée de marked.js

#### 🎨 Interface utilisateur
- **Affichage des réponses** : Gestion des zones de réponse
- **Comparaison** : Affichage des réponses multiples
- **États de chargement** : Indicateurs visuels
- **Messages d'erreur** : Affichage des erreurs utilisateur

## 🔄 Workflow de développement

### Ajout de nouvelles fonctionnalités

1. **CSS** : Ajoutez les styles dans `css/styles.css`
2. **JavaScript** : Étendez la classe `AssistantApp` dans `js/app.js`
3. **HTML** : Ajoutez les éléments dans `templates/index.html`

### Bonnes pratiques

#### CSS
- Utilisez des classes sémantiques
- Respectez la hiérarchie BEM si possible
- Ajoutez des commentaires pour les sections complexes
- Testez la responsivité

#### JavaScript
- Organisez le code en méthodes logiques
- Utilisez des noms de variables/fonctions explicites
- Ajoutez des commentaires JSDoc
- Gérez les erreurs gracieusement
- Testez les différents navigateurs

## 🚀 Optimisations

### Performance
- **CSS** : Minification en production
- **JavaScript** : Minification et bundling
- **Images** : Compression et formats optimisés

### Maintenance
- **Modularité** : Code organisé et réutilisable
- **Documentation** : Commentaires et README
- **Tests** : Validation des fonctionnalités

## 🔧 Configuration

### Variables d'environnement
Le JavaScript peut être configuré via des variables globales :

```javascript
// Dans le HTML
<script>
    window.APP_CONFIG = {
        API_BASE_URL: '{{ config.API_BASE_URL }}',
        DEBUG_MODE: {{ config.DEBUG_MODE|lower }}
    };
</script>
```

### Personnalisation
- **Thèmes** : Modifiez les couleurs dans `styles.css`
- **Animations** : Ajustez les durées et effets
- **Comportement** : Adaptez la logique dans `app.js`

## 📱 Compatibilité

### Navigateurs supportés
- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

### Fonctionnalités utilisées
- **ES6 Classes** : Support moderne
- **Fetch API** : Requêtes HTTP
- **CSS Grid** : Layout responsive
- **CSS Custom Properties** : Variables CSS

## 🐛 Débogage

### Outils recommandés
- **DevTools** : Console et Network
- **Lighthouse** : Audit de performance
- **ESLint** : Qualité du code JavaScript
- **Stylelint** : Qualité du code CSS

### Logs de débogage
Le JavaScript inclut des logs de débogage :

```javascript
console.log('Debug:', data);
console.error('Erreur:', error);
```

## 📚 Ressources

- **Marked.js** : [Documentation](https://marked.js.org/)
- **Tailwind CSS** : [Documentation](https://tailwindcss.com/)
- **Fetch API** : [MDN](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API) 