from flask import Flask, render_template, request, jsonify, Response
from dotenv import load_dotenv
import os
import json
import time
from datetime import datetime

# Charger les variables d'environnement
load_dotenv()

# Import de la base de données
try:
    from src.infrastructure.database import DatabaseManager
    db_manager = DatabaseManager()
    DB_AVAILABLE = True
except Exception as e:
    print(f"Base de données non disponible: {e}")
    db_manager = None
    DB_AVAILABLE = False

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

try:
    from src.infrastructure.groq_client import GroqClient
    groq_client = GroqClient()
    GROQ_AVAILABLE = True
except Exception as e:
    print(f"Groq non disponible: {e}")
    groq_client = None
    GROQ_AVAILABLE = False

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    conversation_id = None
    
    # Récupérer l'historique des conversations
    history = []
    if DB_AVAILABLE:
        try:
            history = db_manager.get_conversation_history(limit=10)
        except Exception as e:
            print(f"Erreur lors de la récupération de l'historique: {e}")
    
    if request.method == 'POST':
        if OPENAI_AVAILABLE:
            # Utiliser OpenAI pour générer une réponse
            prompt = request.form.get('query', '')
            if prompt:
                # Sauvegarder la conversation
                if DB_AVAILABLE:
                    try:
                        conversation_id = db_manager.save_conversation(
                            prompt=prompt,
                            model_used="openai",
                            response_success=True
                        )
                    except Exception as e:
                        print(f"Erreur lors de la sauvegarde: {e}")
                
                # Mesurer le temps de réponse
                start_time = time.time()
                ai_response = openai_client.generate_voice_response(prompt)
                response_time = time.time() - start_time
                
                if ai_response['success']:
                    response = ai_response['text']
                    
                    # Sauvegarder la réponse
                    if DB_AVAILABLE and conversation_id:
                        try:
                            db_manager.save_response(
                                conversation_id=conversation_id,
                                provider="openai",
                                model="gpt-4o",
                                response_text=response,
                                success=True,
                                response_time=response_time
                            )
                        except Exception as e:
                            print(f"Erreur lors de la sauvegarde de la réponse: {e}")
                else:
                    response = f"Erreur: {ai_response['error']}"
                    
                    # Sauvegarder l'erreur
                    if DB_AVAILABLE and conversation_id:
                        try:
                            db_manager.save_response(
                                conversation_id=conversation_id,
                                provider="openai",
                                model="gpt-4o",
                                response_text=None,
                                success=False,
                                error_message=ai_response['error'],
                                response_time=response_time
                            )
                        except Exception as e:
                            print(f"Erreur lors de la sauvegarde de l'erreur: {e}")
            else:
                response = "Veuillez saisir une question."
        else:
            # Réponse statique si OpenAI n'est pas disponible
            response = "Merci pour votre question, nous aurons bientôt une réponse pour vous !"
    
    return render_template('index.html', response=response, history=history)

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

@app.route('/api/groq', methods=['POST'])
def groq_api():
    """API endpoint pour les appels Groq (Llama)."""
    if not GROQ_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Groq n'est pas configuré"
        }), 400
    
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        model = data.get('model', 'llama3-8b-8192')
        
        if not prompt:
            return jsonify({
                "success": False,
                "error": "Le prompt est requis"
            }), 400
        
        # Générer la réponse avec Groq
        groq_response = groq_client.generate_with_model_selection(prompt, model)
        
        return jsonify(groq_response)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/groq/stream', methods=['POST'])
def groq_stream_api():
    """API endpoint pour les appels Groq en streaming."""
    if not GROQ_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Groq n'est pas configuré"
        }), 400
    
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        model = data.get('model', 'llama3-8b-8192')
        
        if not prompt:
            return jsonify({
                "success": False,
                "error": "Le prompt est requis"
            }), 400
        
        def generate():
            for chunk in groq_client.generate_streaming_response(prompt, model):
                yield f"data: {json.dumps({'text': chunk, 'success': True})}\n\n"
        
        return Response(generate(), mimetype='text/event-stream')
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/groq/models', methods=['GET'])
def groq_models_api():
    """API endpoint pour récupérer les modèles disponibles sur Groq."""
    if not GROQ_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Groq n'est pas configuré"
        }), 400
    
    try:
        models = groq_client.get_available_models()
        return jsonify({
            "success": True,
            "models": models
        })
        
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
    """API endpoint pour comparer les réponses d'OpenAI, Claude et Groq."""
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
        
        # Réponse Groq
        if GROQ_AVAILABLE:
            groq_response = groq_client.generate_voice_response(prompt)
            responses['groq'] = groq_response
        else:
            responses['groq'] = {"success": False, "error": "Groq non configuré"}
        
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

@app.route('/api/history', methods=['GET'])
def get_history():
    """API endpoint pour récupérer l'historique des conversations."""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Base de données non disponible"
        }), 500
    
    try:
        limit = request.args.get('limit', 50, type=int)
        offset = request.args.get('offset', 0, type=int)
        
        history = db_manager.get_conversation_history(limit=limit, offset=offset)
        
        return jsonify({
            "success": True,
            "history": history
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/history/<int:conversation_id>', methods=['GET'])
def get_conversation_details(conversation_id):
    """API endpoint pour récupérer les détails d'une conversation."""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Base de données non disponible"
        }), 500
    
    try:
        conversation = db_manager.get_conversation_details(conversation_id)
        
        if not conversation:
            return jsonify({
                "success": False,
                "error": "Conversation non trouvée"
            }), 404
        
        return jsonify({
            "success": True,
            "conversation": conversation
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/history/search', methods=['GET'])
def search_history():
    """API endpoint pour rechercher dans l'historique."""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Base de données non disponible"
        }), 500
    
    try:
        search_term = request.args.get('q', '')
        limit = request.args.get('limit', 20, type=int)
        
        if not search_term:
            return jsonify({
                "success": False,
                "error": "Terme de recherche requis"
            }), 400
        
        results = db_manager.search_conversations(search_term, limit=limit)
        
        return jsonify({
            "success": True,
            "results": results
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/history/<int:conversation_id>', methods=['DELETE'])
def delete_conversation(conversation_id):
    """API endpoint pour supprimer une conversation."""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Base de données non disponible"
        }), 500
    
    try:
        success = db_manager.delete_conversation(conversation_id)
        
        if not success:
            return jsonify({
                "success": False,
                "error": "Conversation non trouvée"
            }), 404
        
        return jsonify({
            "success": True,
            "message": "Conversation supprimée avec succès"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_statistics():
    """API endpoint pour récupérer les statistiques."""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Base de données non disponible"
        }), 500
    
    try:
        stats = db_manager.get_statistics()
        
        return jsonify({
            "success": True,
            "statistics": stats
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/cleanup', methods=['POST'])
def cleanup_old_conversations():
    """API endpoint pour nettoyer les anciennes conversations."""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Base de données non disponible"
        }), 500
    
    try:
        days = request.json.get('days', 30)
        deleted_count = db_manager.cleanup_old_conversations(days=days)
        
        return jsonify({
            "success": True,
            "deleted_count": deleted_count,
            "message": f"{deleted_count} conversations supprimées"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 8000))
    app.run(debug=False, host='0.0.0.0', port=port) 