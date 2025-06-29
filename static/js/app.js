/**
 * Assistant Multi-IA - Module JavaScript Principal
 * Gère l'interface utilisateur et les interactions avec l'API
 */

// Configuration globale
const CONFIG = {
    ENDPOINTS: {
        OPENAI: '/api/chat',
        CLAUDE: '/api/claude',
        GROQ: '/api/groq',
        COMPARE: '/api/compare',
        HISTORY: '/api/history',
        STATS: '/api/stats',
        SEARCH: '/api/history/search'
    },
    MARKDOWN_OPTIONS: {
        breaks: true,
        gfm: true,
        sanitize: false
    }
};

// Classe principale de l'application
class AssistantApp {
    constructor() {
        this.response = '';
        this.initializeMarkdown();
        this.bindEvents();
        this.loadStatistics();
    }

    /**
     * Initialise la configuration de marked.js
     */
    initializeMarkdown() {
        if (typeof marked !== 'undefined') {
            marked.setOptions(CONFIG.MARKDOWN_OPTIONS);
        }
    }

    /**
     * Lie les événements DOM
     */
    bindEvents() {
        // Gestion du changement de fournisseur d'IA
        document.querySelectorAll('input[name="aiProvider"]').forEach(radio => {
            radio.addEventListener('change', (e) => this.handleProviderChange(e));
        });

        // Gestion de la soumission du formulaire
        const form = document.getElementById('queryForm');
        if (form) {
            form.addEventListener('submit', (e) => this.handleQuery(e));
        }

        // Gestion de l'historique
        this.bindHistoryEvents();
    }

    /**
     * Lie les événements liés à l'historique
     */
    bindHistoryEvents() {
        // Bouton de recherche
        const searchBtn = document.getElementById('searchBtn');
        if (searchBtn) {
            searchBtn.addEventListener('click', () => this.searchHistory());
        }

        // Recherche avec Entrée
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.searchHistory();
                }
            });
        }

        // Bouton d'actualisation
        const refreshBtn = document.getElementById('refreshHistoryBtn');
        if (refreshBtn) {
            refreshBtn.addEventListener('click', () => this.refreshHistory());
        }

        // Gestion des clics sur les éléments de l'historique
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('view-btn')) {
                e.stopPropagation();
                const conversationId = e.target.closest('.conversation-item').dataset.id;
                this.viewConversation(conversationId);
            } else if (e.target.classList.contains('delete-btn')) {
                e.stopPropagation();
                const conversationId = e.target.closest('.conversation-item').dataset.id;
                this.deleteConversation(conversationId);
            }
        });

        // Fermeture du modal
        const closeModal = document.getElementById('closeModal');
        if (closeModal) {
            closeModal.addEventListener('click', () => this.closeModal());
        }

        // Fermeture du modal en cliquant à l'extérieur
        const modal = document.getElementById('conversationModal');
        if (modal) {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    this.closeModal();
                }
            });
        }
    }

    /**
     * Charge les statistiques
     */
    async loadStatistics() {
        try {
            const response = await fetch(CONFIG.ENDPOINTS.STATS);
            const data = await response.json();
            
            if (data.success) {
                this.updateStatistics(data.statistics);
            }
        } catch (error) {
            console.error('Erreur lors du chargement des statistiques:', error);
        }
    }

    /**
     * Met à jour l'affichage des statistiques
     */
    updateStatistics(stats) {
        const elements = {
            'totalConversations': stats.total_conversations,
            'successfulConversations': stats.successful_conversations,
            'successRate': stats.success_rate.toFixed(1),
            'todayConversations': stats.daily_stats[new Date().toISOString().split('T')[0]] || 0
        };

        Object.entries(elements).forEach(([id, value]) => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
            }
        });
    }

    /**
     * Recherche dans l'historique
     */
    async searchHistory() {
        const searchInput = document.getElementById('searchInput');
        const searchTerm = searchInput ? searchInput.value.trim() : '';
        
        if (!searchTerm) {
            this.refreshHistory();
            return;
        }

        try {
            const response = await fetch(`${CONFIG.ENDPOINTS.SEARCH}?q=${encodeURIComponent(searchTerm)}`);
            const data = await response.json();
            
            if (data.success) {
                this.updateHistoryList(data.results);
            } else {
                this.showError('Erreur lors de la recherche: ' + data.error);
            }
        } catch (error) {
            console.error('Erreur lors de la recherche:', error);
            this.showError('Erreur lors de la recherche');
        }
    }

    /**
     * Actualise l'historique
     */
    async refreshHistory() {
        try {
            const response = await fetch(CONFIG.ENDPOINTS.HISTORY);
            const data = await response.json();
            
            if (data.success) {
                this.updateHistoryList(data.history);
                this.loadStatistics();
            } else {
                this.showError('Erreur lors du chargement de l\'historique: ' + data.error);
            }
        } catch (error) {
            console.error('Erreur lors du chargement de l\'historique:', error);
            this.showError('Erreur lors du chargement de l\'historique');
        }
    }

    /**
     * Met à jour la liste de l'historique
     */
    updateHistoryList(conversations) {
        const historyList = document.getElementById('historyList');
        if (!historyList) return;

        if (conversations.length === 0) {
            historyList.innerHTML = '<p class="text-gray-500 text-center py-4">Aucune conversation trouvée</p>';
            return;
        }

        const html = conversations.map(conversation => `
            <div class="conversation-item p-3 border border-gray-200 rounded hover:bg-gray-50 cursor-pointer" 
                 data-id="${conversation.id}">
                <div class="flex justify-between items-start">
                    <div class="flex-1">
                        <p class="text-sm font-medium text-gray-800 mb-1">
                            ${conversation.prompt.length > 100 ? 
                                conversation.prompt.substring(0, 100) + '...' : 
                                conversation.prompt}
                        </p>
                        <div class="flex items-center gap-2 text-xs text-gray-500">
                            <span>${conversation.timestamp}</span>
                            ${conversation.model_used ? 
                                `<span class="px-2 py-1 bg-blue-100 text-blue-800 rounded">${conversation.model_used}</span>` : 
                                ''}
                            ${conversation.providers ? 
                                conversation.providers.map(provider => 
                                    `<span class="px-2 py-1 bg-green-100 text-green-800 rounded">${provider}</span>`
                                ).join('') : 
                                ''}
                        </div>
                    </div>
                    <div class="flex gap-1">
                        <button class="view-btn px-2 py-1 bg-blue-600 text-white rounded text-xs hover:bg-blue-700">
                            Voir
                        </button>
                        <button class="delete-btn px-2 py-1 bg-red-600 text-white rounded text-xs hover:bg-red-700">
                            Supprimer
                        </button>
                    </div>
                </div>
            </div>
        `).join('');

        historyList.innerHTML = html;
    }

    /**
     * Affiche les détails d'une conversation
     */
    async viewConversation(conversationId) {
        try {
            const response = await fetch(`${CONFIG.ENDPOINTS.HISTORY}/${conversationId}`);
            const data = await response.json();
            
            if (data.success) {
                this.showConversationModal(data.conversation);
            } else {
                this.showError('Erreur lors du chargement des détails: ' + data.error);
            }
        } catch (error) {
            console.error('Erreur lors du chargement des détails:', error);
            this.showError('Erreur lors du chargement des détails');
        }
    }

    /**
     * Affiche le modal avec les détails de la conversation
     */
    showConversationModal(conversation) {
        const modal = document.getElementById('conversationModal');
        const modalContent = document.getElementById('modalContent');
        
        if (!modal || !modalContent) return;

        const responsesHtml = conversation.responses.map(response => `
            <div class="mb-4 p-3 border rounded ${response.success ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}">
                <div class="flex justify-between items-center mb-2">
                    <h4 class="font-semibold text-gray-800">${response.provider}</h4>
                    <span class="text-xs px-2 py-1 rounded ${response.success ? 'bg-green-200 text-green-800' : 'bg-red-200 text-red-800'}">
                        ${response.success ? 'Succès' : 'Erreur'}
                    </span>
                </div>
                ${response.model ? `<p class="text-xs text-gray-600 mb-2">Modèle: ${response.model}</p>` : ''}
                ${response.response_text ? 
                    `<div class="prose prose-sm max-w-none">${this.renderMarkdown(response.response_text)}</div>` : 
                    `<p class="text-red-600">${response.error_message}</p>`
                }
                ${response.response_time ? `<p class="text-xs text-gray-500 mt-2">Temps: ${response.response_time.toFixed(2)}s</p>` : ''}
                ${response.tokens_used ? `<p class="text-xs text-gray-500">Tokens: ${response.tokens_used}</p>` : ''}
            </div>
        `).join('');

        modalContent.innerHTML = `
            <div class="mb-4">
                <h4 class="font-semibold text-gray-800 mb-2">Prompt:</h4>
                <p class="text-gray-700 p-3 bg-gray-50 rounded">${conversation.prompt}</p>
            </div>
            <div class="mb-4">
                <p class="text-sm text-gray-600">Date: ${conversation.timestamp}</p>
                ${conversation.model_used ? `<p class="text-sm text-gray-600">Modèle principal: ${conversation.model_used}</p>` : ''}
            </div>
            <div>
                <h4 class="font-semibold text-gray-800 mb-2">Réponses:</h4>
                ${responsesHtml}
            </div>
        `;

        modal.classList.remove('hidden');
    }

    /**
     * Ferme le modal
     */
    closeModal() {
        const modal = document.getElementById('conversationModal');
        if (modal) {
            modal.classList.add('hidden');
        }
    }

    /**
     * Supprime une conversation
     */
    async deleteConversation(conversationId) {
        if (!confirm('Êtes-vous sûr de vouloir supprimer cette conversation ?')) {
            return;
        }

        try {
            const response = await fetch(`${CONFIG.ENDPOINTS.HISTORY}/${conversationId}`, {
                method: 'DELETE'
            });
            const data = await response.json();
            
            if (data.success) {
                this.refreshHistory();
            } else {
                this.showError('Erreur lors de la suppression: ' + data.error);
            }
        } catch (error) {
            console.error('Erreur lors de la suppression:', error);
            this.showError('Erreur lors de la suppression');
        }
    }

    /**
     * Gère le changement de fournisseur d'IA
     */
    handleProviderChange(event) {
        const groqSelector = document.getElementById('groqModelSelector');
        if (groqSelector) {
            groqSelector.style.display = event.target.value === 'groq' ? 'block' : 'none';
        }
    }

    /**
     * Rend le markdown en HTML
     */
    renderMarkdown(text) {
        if (!text) return '';
        try {
            return marked.parse(text);
        } catch (error) {
            console.error('Erreur lors du rendu markdown:', error);
            return text; // Retourner le texte brut en cas d'erreur
        }
    }

    /**
     * Affiche un message d'erreur
     */
    showError(message) {
        const errorArea = document.getElementById('errorArea');
        const errorText = document.getElementById('errorText');
        const responseArea = document.getElementById('responseArea');
        const compareArea = document.getElementById('compareArea');
        
        if (errorText) errorText.textContent = message;
        if (errorArea) errorArea.style.display = 'block';
        if (responseArea) responseArea.style.display = 'none';
        if (compareArea) compareArea.style.display = 'none';
    }

    /**
     * Masque tous les éléments d'affichage
     */
    hideAllDisplays() {
        const elements = ['responseArea', 'compareArea', 'errorArea'];
        elements.forEach(id => {
            const element = document.getElementById(id);
            if (element) element.style.display = 'none';
        });
    }

    /**
     * Affiche l'indicateur de chargement
     */
    showLoading() {
        const loadingIndicator = document.getElementById('loadingIndicator');
        const submitBtn = document.getElementById('submitBtn');
        
        if (loadingIndicator) loadingIndicator.style.display = 'block';
        if (submitBtn) submitBtn.disabled = true;
    }

    /**
     * Masque l'indicateur de chargement
     */
    hideLoading() {
        const loadingIndicator = document.getElementById('loadingIndicator');
        const submitBtn = document.getElementById('submitBtn');
        
        if (loadingIndicator) loadingIndicator.style.display = 'none';
        if (submitBtn) submitBtn.disabled = false;
    }

    /**
     * Affiche une réponse normale
     */
    displaySingleResponse(text) {
        const responseArea = document.getElementById('responseArea');
        const responseText = document.getElementById('responseText');
        
        if (responseText) responseText.innerHTML = this.renderMarkdown(text);
        if (responseArea) responseArea.style.display = 'block';
    }

    /**
     * Affiche les réponses de comparaison
     */
    displayCompareResponses(responses) {
        const compareArea = document.getElementById('compareArea');
        const openaiResponse = document.getElementById('openaiResponse');
        const claudeResponse = document.getElementById('claudeResponse');
        const groqResponse = document.getElementById('groqResponse');

        if (openaiResponse) {
            openaiResponse.innerHTML = responses.openai.success ? 
                this.renderMarkdown(responses.openai.text) : responses.openai.error;
        }
        
        if (claudeResponse) {
            claudeResponse.innerHTML = responses.claude.success ? 
                this.renderMarkdown(responses.claude.text) : responses.claude.error;
        }
        
        if (groqResponse) {
            groqResponse.innerHTML = responses.groq.success ? 
                this.renderMarkdown(responses.groq.text) : responses.groq.error;
        }
        
        if (compareArea) compareArea.style.display = 'block';
    }

    /**
     * Récupère les données du formulaire
     */
    getFormData() {
        const queryInput = document.getElementById('queryInput');
        const selectedProvider = document.querySelector('input[name="aiProvider"]:checked');
        const groqModel = document.getElementById('groqModel');
        
        return {
            prompt: queryInput ? queryInput.value.trim() : '',
            provider: selectedProvider ? selectedProvider.value : 'openai',
            groqModel: groqModel ? groqModel.value : 'llama3-8b-8192'
        };
    }

    /**
     * Détermine l'endpoint et le corps de la requête
     */
    getRequestConfig(formData) {
        let endpoint = '';
        let requestBody = { prompt: formData.prompt };
        
        switch(formData.provider) {
            case 'openai':
                endpoint = CONFIG.ENDPOINTS.OPENAI;
                break;
            case 'claude':
                endpoint = CONFIG.ENDPOINTS.CLAUDE;
                break;
            case 'groq':
                endpoint = CONFIG.ENDPOINTS.GROQ;
                requestBody.model = formData.groqModel;
                break;
            case 'compare':
                endpoint = CONFIG.ENDPOINTS.COMPARE;
                break;
            default:
                endpoint = CONFIG.ENDPOINTS.OPENAI;
        }
        
        return { endpoint, requestBody };
    }

    /**
     * Effectue un appel API
     */
    async makeApiCall(endpoint, requestBody) {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestBody)
        });
        
        return await response.json();
    }

    /**
     * Gère la soumission d'une requête
     */
    async handleQuery(event) {
        event.preventDefault();
        
        const formData = this.getFormData();
        if (!formData.prompt) {
            this.showError('Veuillez saisir une question.');
            return;
        }
        
        this.hideAllDisplays();
        this.showLoading();
        
        try {
            const { endpoint, requestBody } = this.getRequestConfig(formData);
            const result = await this.makeApiCall(endpoint, requestBody);
            
            if (result.success) {
                if (formData.provider === 'compare') {
                    this.displayCompareResponses(result.responses);
                } else {
                    this.displaySingleResponse(result.text);
                }
                
                // Actualiser l'historique après une nouvelle conversation
                setTimeout(() => this.refreshHistory(), 1000);
            } else {
                this.showError(result.error || 'Une erreur est survenue.');
            }
        } catch (error) {
            console.error('Erreur lors de la requête:', error);
            this.showError('Erreur de connexion. Veuillez réessayer.');
        } finally {
            this.hideLoading();
        }
    }
}

// Initialisation de l'application
document.addEventListener('DOMContentLoaded', () => {
    new AssistantApp();
});

// Export pour utilisation dans d'autres modules (si nécessaire)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AssistantApp;
} 