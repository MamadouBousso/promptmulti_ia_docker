# 🐳 Déploiement avec Docker

Ce guide explique comment déployer l'application multi-IA avec Docker.

## Prérequis

- Docker installé sur votre machine
- Variables d'environnement configurées (optionnel)

## 🚀 Déploiement rapide

### Option 1: Script automatique

```bash
# Rendre le script exécutable (si pas déjà fait)
chmod +x docker-build.sh

# Lancer le script
./docker-build.sh
```

### Option 2: Docker Compose (recommandé)

```bash
# Construire et lancer avec docker-compose
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter
docker-compose down
```

### Option 3: Docker manuel

```bash
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

## 🔧 Configuration des variables d'environnement

### Option 1: Fichier .env

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

### Option 2: Variables d'environnement système

```bash
export OPENAI_API_KEY="votre_clé_openai"
export ANTHROPIC_API_KEY="votre_clé_claude"
export GROQ_API_KEY="votre_clé_groq"
```

## 📋 Commandes utiles

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

## 🌐 Accès à l'application

Une fois le conteneur lancé, l'application est accessible sur :
- **URL locale** : http://localhost:8000
- **URL réseau** : http://votre_ip:8000

## 🔍 Dépannage

### Problème de port déjà utilisé

Si le port 8000 est déjà utilisé, changez-le dans `docker-compose.yml` :

```yaml
ports:
  - "8080:8000"  # Port externe:Port interne
```

### Problème de permissions

```bash
# Donner les bonnes permissions au script
chmod +x docker-build.sh
```

### Reconstruire l'image

```bash
# Supprimer l'ancienne image
docker rmi promptmulti_ia_docker

# Reconstruire
docker build -t promptmulti_ia_docker .
```

### Vérifier les logs

```bash
# Logs en temps réel
docker logs -f promptmulti_ia_docker-container

# Derniers logs
docker logs --tail 50 promptmulti_ia_docker-container
```

## 🏗️ Architecture Docker

```
promptmulti_ia_docker/
├── Dockerfile          # Configuration de l'image
├── docker-compose.yml  # Orchestration des services
├── .dockerignore       # Fichiers exclus du build
├── docker-build.sh     # Script de déploiement
└── app.py             # Application Flask
```

## 🔒 Sécurité

- Les clés API sont passées via des variables d'environnement
- L'application écoute sur toutes les interfaces (0.0.0.0) pour Docker
- Le mode debug est désactivé en production
- Les fichiers sensibles sont exclus via `.dockerignore` 