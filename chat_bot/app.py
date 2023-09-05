from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = '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'
OPENAI_API_URL = 'https://api.openai.com/v1/engines/text-davinci-003/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    prompt = f"User: {user_message}\nAI:"
    data = {
        'prompt': prompt,
        'max_tokens': 150,
        'n': 1,
        'stop': None,
        'temperature': 0.8,
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=data)

    # Imprimir la respuesta JSON completa para verificar su contenido
    print(response.json())

    try:
        choices = response.json().get('choices')
        if choices is not None and len(choices) > 0:
            ai_message = choices[0].get('text', '').strip()
        else:
            ai_message = "No se encontraron opciones disponibles en la respuesta."
    except ValueError:
        ai_message = "Error en la respuesta JSON de la API."

    return jsonify({'message': ai_message})

if __name__ == '__main__':
    app.run(debug=True)
