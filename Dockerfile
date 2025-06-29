# Utiliser une image Python officielle avec uv préinstallé
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer uv
RUN pip install uv

# Copier les fichiers de configuration
COPY pyproject.toml ./
COPY README.md ./

# Créer un environnement virtuel et installer les dépendances
RUN uv venv .venv
RUN uv pip install flask openai anthropic groq python-dotenv

# Copier le code source
COPY . .

# Exposer le port 8000
EXPOSE 8000

# Définir les variables d'environnement
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Commande pour démarrer l'application
CMD ["uv", "run", "python", "app.py"] 