from flask import Flask, render_template, request, jsonify, Response
from dotenv import load_dotenv
import os
import json

# Charger les variables d'environnement
load_dotenv()

# Import des clients IA
try:
    from src.infrastructure.openai_client import OpenAIClient
    openai_client = OpenAIClient()
    OPENAI_AVAILABLE = True
except Exception as e:
    print(f"OpenAI non disponible: {e}")
    openai_client = None
    OPENAI_AVAILABLE = False

try:
    from src.infrastructure.claude_client import ClaudeClient
    claude_client = ClaudeClient()
    CLAUDE_AVAILABLE = True
except Exception as e:
    print(f"Claude non disponible: {e}")
    claude_client = None
    CLAUDE_AVAILABLE = False

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    if request.method == 'POST':
        if OPENAI_AVAILABLE:
            # Utiliser OpenAI pour générer une réponse
            prompt = request.form.get('query', '')
            if prompt:
                ai_response = openai_client.generate_voice_response(prompt)
                if ai_response['success']:
                    response = ai_response['text']
                else:
                    response = f"Erreur: {ai_response['error']}"
            else:
                response = "Veuillez saisir une question."
        else:
            # Réponse statique si OpenAI n'est pas disponible
            response = "Merci pour votre question, nous aurons bientôt une réponse pour vous !"
    
    return render_template('index.html', response=response)

@app.route('/api/chat', methods=['POST'])
def chat_api():
    """API endpoint pour les appels OpenAI."""
    if not OPENAI_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "OpenAI n'est pas configuré"
        }), 400
    
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({
                "success": False,
                "error": "Le prompt est requis"
            }), 400
        
        # Générer la réponse avec OpenAI
        ai_response = openai_client.generate_voice_response(prompt)
        
        return jsonify(ai_response)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/claude', methods=['POST'])
def claude_api():
    """API endpoint pour les appels Claude."""
    if not CLAUDE_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Claude n'est pas configuré"
        }), 400
    
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({
                "success": False,
                "error": "Le prompt est requis"
            }), 400
        
        # Générer la réponse avec Claude
        claude_response = claude_client.generate_voice_response(prompt)
        
        return jsonify(claude_response)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/claude/stream', methods=['POST'])
def claude_stream_api():
    """API endpoint pour les appels Claude en streaming."""
    if not CLAUDE_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Claude n'est pas configuré"
        }), 400
    
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({
                "success": False,
                "error": "Le prompt est requis"
            }), 400
        
        def generate():
            for chunk in claude_client.generate_streaming_response(prompt):
                yield f"data: {json.dumps({'text': chunk, 'success': True})}\n\n"
        
        return Response(generate(), mimetype='text/event-stream')
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/compare', methods=['POST'])
def compare_apis():
    """API endpoint pour comparer les réponses d'OpenAI et Claude."""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({
                "success": False,
                "error": "Le prompt est requis"
            }), 400
        
        responses = {}
        
        # Réponse OpenAI
        if OPENAI_AVAILABLE:
            openai_response = openai_client.generate_voice_response(prompt)
            responses['openai'] = openai_response
        else:
            responses['openai'] = {"success": False, "error": "OpenAI non configuré"}
        
        # Réponse Claude
        if CLAUDE_AVAILABLE:
            claude_response = claude_client.generate_voice_response(prompt)
            responses['claude'] = claude_response
        else:
            responses['claude'] = {"success": False, "error": "Claude non configuré"}
        
        return jsonify({
            "success": True,
            "prompt": prompt,
            "responses": responses
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 