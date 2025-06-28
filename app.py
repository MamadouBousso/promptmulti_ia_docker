from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    if request.method == 'POST':
        response = "Merci pour votre question, nous aurons bientôt une réponse pour vous !"
    
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True) 