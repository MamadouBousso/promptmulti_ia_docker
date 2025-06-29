import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional
import os

class DatabaseManager:
    def __init__(self, db_path: str = "data/conversations.db"):
        # Créer le dossier data s'il n'existe pas
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialise la base de données avec les tables nécessaires."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Table pour les conversations
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prompt TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    user_session TEXT,
                    model_used TEXT,
                    response_success BOOLEAN DEFAULT 1
                )
            ''')
            
            # Table pour les réponses détaillées
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS responses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id INTEGER,
                    provider TEXT NOT NULL,
                    model TEXT,
                    response_text TEXT,
                    success BOOLEAN DEFAULT 1,
                    error_message TEXT,
                    response_time REAL,
                    tokens_used INTEGER,
                    FOREIGN KEY (conversation_id) REFERENCES conversations (id)
                )
            ''')
            
            conn.commit()
    
    def save_conversation(self, prompt: str, user_session: str = None, 
                         model_used: str = None, response_success: bool = True) -> int:
        """Sauvegarde une nouvelle conversation et retourne son ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO conversations (prompt, user_session, model_used, response_success)
                VALUES (?, ?, ?, ?)
            ''', (prompt, user_session, model_used, response_success))
            
            conversation_id = cursor.lastrowid
            conn.commit()
            return conversation_id
    
    def save_response(self, conversation_id: int, provider: str, model: str = None,
                     response_text: str = None, success: bool = True, 
                     error_message: str = None, response_time: float = None,
                     tokens_used: int = None):
        """Sauvegarde une réponse pour une conversation."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO responses 
                (conversation_id, provider, model, response_text, success, 
                 error_message, response_time, tokens_used)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (conversation_id, provider, model, response_text, success,
                  error_message, response_time, tokens_used))
            
            conn.commit()
    
    def get_conversation_history(self, limit: int = 50, offset: int = 0) -> List[Dict]:
        """Récupère l'historique des conversations."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT c.id, c.prompt, c.timestamp, c.model_used, c.response_success,
                       GROUP_CONCAT(r.provider) as providers,
                       GROUP_CONCAT(r.success) as response_successes
                FROM conversations c
                LEFT JOIN responses r ON c.id = r.conversation_id
                GROUP BY c.id
                ORDER BY c.timestamp DESC
                LIMIT ? OFFSET ?
            ''', (limit, offset))
            
            conversations = []
            for row in cursor.fetchall():
                conversation = {
                    'id': row['id'],
                    'prompt': row['prompt'],
                    'timestamp': row['timestamp'],
                    'model_used': row['model_used'],
                    'response_success': bool(row['response_success']),
                    'providers': row['providers'].split(',') if row['providers'] else [],
                    'response_successes': [bool(int(s)) for s in row['response_successes'].split(',')] if row['response_successes'] else []
                }
                conversations.append(conversation)
            
            return conversations
    
    def get_conversation_details(self, conversation_id: int) -> Optional[Dict]:
        """Récupère les détails d'une conversation spécifique avec ses réponses."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Récupérer la conversation
            cursor.execute('''
                SELECT id, prompt, timestamp, model_used, response_success
                FROM conversations
                WHERE id = ?
            ''', (conversation_id,))
            
            conversation_row = cursor.fetchone()
            if not conversation_row:
                return None
            
            # Récupérer les réponses
            cursor.execute('''
                SELECT provider, model, response_text, success, error_message,
                       response_time, tokens_used
                FROM responses
                WHERE conversation_id = ?
                ORDER BY id
            ''', (conversation_id,))
            
            responses = []
            for row in cursor.fetchall():
                response = {
                    'provider': row['provider'],
                    'model': row['model'],
                    'response_text': row['response_text'],
                    'success': bool(row['success']),
                    'error_message': row['error_message'],
                    'response_time': row['response_time'],
                    'tokens_used': row['tokens_used']
                }
                responses.append(response)
            
            conversation = {
                'id': conversation_row['id'],
                'prompt': conversation_row['prompt'],
                'timestamp': conversation_row['timestamp'],
                'model_used': conversation_row['model_used'],
                'response_success': bool(conversation_row['response_success']),
                'responses': responses
            }
            
            return conversation
    
    def search_conversations(self, search_term: str, limit: int = 20) -> List[Dict]:
        """Recherche dans les conversations par mot-clé."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT c.id, c.prompt, c.timestamp, c.model_used, c.response_success
                FROM conversations c
                WHERE c.prompt LIKE ?
                ORDER BY c.timestamp DESC
                LIMIT ?
            ''', (f'%{search_term}%', limit))
            
            conversations = []
            for row in cursor.fetchall():
                conversation = {
                    'id': row['id'],
                    'prompt': row['prompt'],
                    'timestamp': row['timestamp'],
                    'model_used': row['model_used'],
                    'response_success': bool(row['response_success'])
                }
                conversations.append(conversation)
            
            return conversations
    
    def delete_conversation(self, conversation_id: int) -> bool:
        """Supprime une conversation et ses réponses associées."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Supprimer d'abord les réponses
                cursor.execute('DELETE FROM responses WHERE conversation_id = ?', (conversation_id,))
                
                # Puis supprimer la conversation
                cursor.execute('DELETE FROM conversations WHERE id = ?', (conversation_id,))
                
                conn.commit()
                return cursor.rowcount > 0
        except Exception:
            return False
    
    def get_statistics(self) -> Dict:
        """Récupère des statistiques sur les conversations."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Total des conversations
            cursor.execute('SELECT COUNT(*) FROM conversations')
            total_conversations = cursor.fetchone()[0]
            
            # Conversations réussies
            cursor.execute('SELECT COUNT(*) FROM conversations WHERE response_success = 1')
            successful_conversations = cursor.fetchone()[0]
            
            # Réponses par fournisseur
            cursor.execute('''
                SELECT provider, COUNT(*) as count, 
                       AVG(response_time) as avg_time,
                       SUM(tokens_used) as total_tokens
                FROM responses
                GROUP BY provider
            ''')
            
            provider_stats = {}
            for row in cursor.fetchall():
                provider_stats[row[0]] = {
                    'count': row[1],
                    'avg_time': row[2],
                    'total_tokens': row[3] or 0
                }
            
            # Conversations par jour (7 derniers jours)
            cursor.execute('''
                SELECT DATE(timestamp) as date, COUNT(*) as count
                FROM conversations
                WHERE timestamp >= datetime('now', '-7 days')
                GROUP BY DATE(timestamp)
                ORDER BY date DESC
            ''')
            
            daily_stats = {}
            for row in cursor.fetchall():
                daily_stats[row[0]] = row[1]
            
            return {
                'total_conversations': total_conversations,
                'successful_conversations': successful_conversations,
                'success_rate': (successful_conversations / total_conversations * 100) if total_conversations > 0 else 0,
                'provider_stats': provider_stats,
                'daily_stats': daily_stats
            }
    
    def cleanup_old_conversations(self, days: int = 30) -> int:
        """Nettoie les anciennes conversations (plus de X jours)."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Supprimer les réponses des anciennes conversations
            cursor.execute('''
                DELETE FROM responses 
                WHERE conversation_id IN (
                    SELECT id FROM conversations 
                    WHERE timestamp < datetime('now', '-{} days')
                )
            '''.format(days))
            
            # Supprimer les anciennes conversations
            cursor.execute('''
                DELETE FROM conversations 
                WHERE timestamp < datetime('now', '-{} days')
            '''.format(days))
            
            deleted_count = cursor.rowcount
            conn.commit()
            return deleted_count 