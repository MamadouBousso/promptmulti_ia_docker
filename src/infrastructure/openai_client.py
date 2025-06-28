import os
import openai
from dotenv import load_dotenv
from typing import Optional, Dict, Any

# Charger les variables d'environnement
load_dotenv()

class OpenAIClient:
    """Client pour interagir avec l'API OpenAI."""
    
    def __init__(self):
        """Initialise le client OpenAI avec la clé API."""
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY non trouvée dans les variables d'environnement")
        
        openai.api_key = api_key
        self.client = openai.OpenAI(api_key=api_key)
    
    def generate_response(self, prompt: str, model: str = "gpt-4o") -> Optional[str]:
        """
        Génère une réponse à partir d'un prompt en utilisant l'API OpenAI.
        
        Args:
            prompt (str): Le prompt à envoyer à l'API
            model (str): Le modèle à utiliser (défaut: gpt-4o)
            
        Returns:
            Optional[str]: La réponse générée ou None en cas d'erreur
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Vous êtes un assistant vocal intelligent et utile."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Erreur lors de l'appel à l'API OpenAI: {e}")
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
                # Générer l'audio (optionnel - nécessite des crédits supplémentaires)
                # audio_response = self.client.audio.speech.create(
                #     model="tts-1",
                #     voice="alloy",
                #     input=text_response
                # )
                
                return {
                    "success": True,
                    "text": text_response,
                    "prompt": prompt,
                    # "audio_url": "data:audio/mp3;base64," + base64.b64encode(audio_response.content).decode()
                }
            else:
                return {
                    "success": False,
                    "error": "Impossible de générer une réponse",
                    "prompt": prompt
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "prompt": prompt
            } 