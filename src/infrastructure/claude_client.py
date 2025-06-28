import os
import anthropic
from dotenv import load_dotenv
from typing import Optional, Dict, Any

# Charger les variables d'environnement
load_dotenv()

class ClaudeClient:
    """Client pour interagir avec l'API Claude (Anthropic)."""
    
    def __init__(self):
        """Initialise le client Claude avec la clé API."""
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY non trouvée dans les variables d'environnement")
        
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def generate_response(self, prompt: str, model: str = "claude-3-5-sonnet-20241022") -> Optional[str]:
        """
        Génère une réponse à partir d'un prompt en utilisant l'API Claude.
        
        Args:
            prompt (str): Le prompt à envoyer à l'API
            model (str): Le modèle à utiliser (défaut: claude-3-5-sonnet-20241022)
            
        Returns:
            Optional[str]: La réponse générée ou None en cas d'erreur
        """
        try:
            response = self.client.messages.create(
                model=model,
                max_tokens=500,
                temperature=0.7,
                system="Vous êtes un assistant vocal intelligent et utile. Répondez de manière claire et concise.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return response.content[0].text
            
        except Exception as e:
            print(f"Erreur lors de l'appel à l'API Claude: {e}")
            return None
    
    def generate_voice_response(self, prompt: str) -> Dict[str, Any]:
        """
        Génère une réponse vocale à partir d'un prompt.
        
        Args:
            prompt (str): Le prompt à envoyer à l'API
            
        Returns:
            Dict[str, Any]: Dictionnaire contenant la réponse textuelle et les métadonnées
        """
        try:
            # Générer la réponse textuelle
            text_response = self.generate_response(prompt)
            
            if text_response:
                return {
                    "success": True,
                    "text": text_response,
                    "prompt": prompt,
                    "model": "claude-3-5-sonnet-20241022",
                    "provider": "anthropic"
                }
            else:
                return {
                    "success": False,
                    "error": "Impossible de générer une réponse",
                    "prompt": prompt,
                    "provider": "anthropic"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "prompt": prompt,
                "provider": "anthropic"
            }
    
    def generate_streaming_response(self, prompt: str, model: str = "claude-3-5-sonnet-20241022"):
        """
        Génère une réponse en streaming pour une expérience plus fluide.
        
        Args:
            prompt (str): Le prompt à envoyer à l'API
            model (str): Le modèle à utiliser
            
        Yields:
            str: Fragments de la réponse au fur et à mesure
        """
        try:
            with self.client.messages.stream(
                model=model,
                max_tokens=500,
                temperature=0.7,
                system="Vous êtes un assistant vocal intelligent et utile. Répondez de manière claire et concise.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            ) as stream:
                for text in stream.text_stream:
                    yield text
                    
        except Exception as e:
            yield f"Erreur: {str(e)}" 