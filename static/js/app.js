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
        COMPARE: '/api/compare'
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
     * Effectue l'appel API
     */
    async makeApiCall(endpoint, requestBody) {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestBody)
        });
        
        if (!response.ok) {
            throw new Error(`Erreur HTTP: ${response.status}`);
        }
        
        return await response.json();
    }

    /**
     * Gère la soumission de la requête
     */
    async handleQuery(event) {
        event.preventDefault();
        
        const formData = this.getFormData();
        
        if (!formData.prompt) {
            this.showError('Veuillez saisir une question.');
            return;
        }
        
        // Préparer l'affichage
        this.hideAllDisplays();
        this.showLoading();
        
        try {
            const { endpoint, requestBody } = this.getRequestConfig(formData);
            const data = await this.makeApiCall(endpoint, requestBody);
            
            if (data.success) {
                if (formData.provider === 'compare') {
                    this.displayCompareResponses(data.responses);
                } else {
                    this.displaySingleResponse(data.text);
                }
            } else {
                this.showError(data.error || 'Erreur lors de la génération de la réponse');
            }
            
        } catch (error) {
            this.showError('Erreur de connexion au serveur');
            console.error('Erreur:', error);
        } finally {
            this.hideLoading();
        }
    }
}

// Initialisation de l'application quand le DOM est chargé
document.addEventListener('DOMContentLoaded', () => {
    new AssistantApp();
});

// Export pour utilisation dans d'autres modules (si nécessaire)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AssistantApp;
} 