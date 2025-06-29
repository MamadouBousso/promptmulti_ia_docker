#!/bin/bash

# Script pour construire et lancer l'application Docker

echo "🐳 Construction de l'image Docker..."
docker build -t promptmulti_ia_docker .

if [ $? -eq 0 ]; then
    echo "✅ Image construite avec succès!"
    
    echo "🚀 Lancement du conteneur..."
    docker run -d \
        --name promptmulti_ia_docker-container \
        -p 8000:8000 \
        -e OPENAI_API_KEY="$OPENAI_API_KEY" \
        -e ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
        -e GROQ_API_KEY="$GROQ_API_KEY" \
        promptmulti_ia_docker
    
    if [ $? -eq 0 ]; then
        echo "✅ Conteneur lancé avec succès!"
        echo "🌐 Application accessible sur: http://localhost:8000"
        echo ""
        echo "📋 Commandes utiles:"
        echo "  - Voir les logs: docker logs promptmulti_ia_docker-container"
        echo "  - Arrêter: docker stop promptmulti_ia_docker-container"
        echo "  - Redémarrer: docker restart promptmulti_ia_docker-container"
        echo "  - Supprimer: docker rm promptmulti_ia_docker-container"
    else
        echo "❌ Erreur lors du lancement du conteneur"
    fi
else
    echo "❌ Erreur lors de la construction de l'image"
fi 