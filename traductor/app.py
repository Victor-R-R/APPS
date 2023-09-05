from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')
        source_lang = request.form.get('source_lang', 'es')
        target_lang = request.form.get('target_lang', 'en')
        
        # Rest of the code for translation
        
        translations = {
            'source_lang': source_lang,
            'target_lang': target_lang,
            'translation': GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        }
        return render_template('index.html', translations=translations)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
