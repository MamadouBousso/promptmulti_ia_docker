import os
import groq
from dotenv import load_dotenv
from typing import Optional, Dict, Any

# Charger les variables d'environnement
load_dotenv()

class GroqClient:
    """Client pour interagir avec l'API Groq (Llama models)."""
    
    def __init__(self):
        """Initialise le client Groq avec la clé API."""
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            raise ValueError("GROQ_API_KEY non trouvée dans les variables d'environnement")
        
        self.client = groq.Groq(api_key=api_key)
    
    def generate_response(self, prompt: str, model: str = "llama3-8b-8192") -> Optional[str]:
        """
        Génère une réponse à partir d'un prompt en utilisant l'API Groq.
        
        Args:
            prompt (str): Le prompt à envoyer à l'API
            model (str): Le modèle à utiliser (défaut: llama3-8b-8192)
            
        Returns:
            Optional[str]: La réponse générée ou None en cas d'erreur
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Vous êtes un assistant vocal intelligent et utile. Répondez de manière claire et concise."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7,
                top_p=1,
                stream=False
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Erreur lors de l'appel à l'API Groq: {e}")
            return None
    
    def generate_voice_response(self, prompt: str,model: str = "llama3-8b-8192") -> Dict[str, Any]:
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
                    "model": model,
                    "provider": "groq"
                }
            else:
                return {
                    "success": False,
                    "error": "Impossible de générer une réponse",
                    "prompt": prompt,
                    "provider": "groq"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "prompt": prompt,
                "provider": "groq"
            }
    
    def generate_streaming_response(self, prompt: str, model: str = "llama3-8b-8192"):
        """
        Génère une réponse en streaming pour une expérience plus fluide.
        
        Args:
            prompt (str): Le prompt à envoyer à l'API
            model (str): Le modèle à utiliser
            
        Yields:
            str: Fragments de la réponse au fur et à mesure
        """
        try:
            stream = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Vous êtes un assistant vocal intelligent et utile. Répondez de manière claire et concise."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7,
                top_p=1,
                stream=True
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            yield f"Erreur: {str(e)}"
    
    def get_available_models(self) -> list:
        """
        Récupère la liste des modèles disponibles sur Groq.
        
        Returns:
            list: Liste des modèles disponibles
        """
        try:
            models = self.client.models.list()
            return [model.id for model in models.data]
        except Exception as e:
            print(f"Erreur lors de la récupération des modèles: {e}")
            return []
    
    def generate_with_model_selection(self, prompt: str, model: str = "llama3-8b-8192") -> Dict[str, Any]:
        """
        Génère une réponse avec sélection de modèle spécifique.
        
        Args:
            prompt (str): Le prompt à envoyer à l'API
            model (str): Le modèle spécifique à utiliser
            
        Returns:
            Dict[str, Any]: Dictionnaire contenant la réponse et les métadonnées
        """
        try:
            text_response = self.generate_response(prompt, model)
            
            if text_response:
                return {
                    "success": True,
                    "text": text_response,
                    "prompt": prompt,
                    "model": model,
                    "provider": "groq"
                }
            else:
                return {
                    "success": False,
                    "error": "Impossible de générer une réponse",
                    "prompt": prompt,
                    "model": model,
                    "provider": "groq"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "prompt": prompt,
                "model": model,
                "provider": "groq"
            } 