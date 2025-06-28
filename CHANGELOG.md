# Changelog

Tous les changements notables de ce projet seront documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [2.0.0] - 2025-06-28

### Ajouté
- Support complet pour l'API Claude (Anthropic)
- Support complet pour l'API Groq (Llama)
- Interface de comparaison en temps réel des trois modèles
- Rendu markdown complet avec marked.js
- Sélecteur de modèles Llama pour Groq
- Styles CSS personnalisés pour le formatage markdown
- Documentation complète mise à jour
- Configuration avancée des modèles
- Gestion d'erreurs robuste pour tous les fournisseurs
- Support des listes à puces et formatage riche
- Architecture modulaire avec clients API séparés

### Modifié
- Interface utilisateur modernisée avec sélecteurs d'IA
- API endpoints restructurés pour supporter plusieurs fournisseurs
- Documentation complètement réécrite
- Configuration des variables d'environnement améliorée
- Structure du projet optimisée

### Supprimé
- Ancienne fonction de nettoyage markdown manuel
- Dépendance sur les classes prose de Tailwind (remplacées par CSS personnalisé)

## [1.1.0] - 2025-06-XX

### Ajouté
- Support initial pour l'API OpenAI
- Interface web avec Tailwind CSS
- Endpoint API `/api/chat`
- Gestion des erreurs basique
- Indicateur de chargement

### Modifié
- Amélioration de l'interface utilisateur
- Optimisation des performances

## [1.0.0] - 2025-06-XX

### Ajouté
- Version initiale du projet
- Structure de base Flask
- Configuration de base
- Documentation initiale

---

## Types de changements

- **Ajouté** : pour les nouvelles fonctionnalités
- **Modifié** : pour les changements dans les fonctionnalités existantes
- **Déprécié** : pour les fonctionnalités qui seront bientôt supprimées
- **Supprimé** : pour les fonctionnalités supprimées
- **Corrigé** : pour les corrections de bugs
- **Sécurité** : pour les corrections de vulnérabilités 