from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/generate", methods=['POST'])
def generate():
    url = request.form['url'] 
    qr = qrcode.make(url)
    filename = f"{url.replace('/','_')}.png"
    qr.save(os.path.join(app.root_path, 'static', filename))
    return render_template('generate.html', url=url, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

