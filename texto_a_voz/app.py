from flask import Flask, render_template, request, jsonify
from gtts import gTTS
from playsound import playsound
import os
import threading

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def speak():
    text = request.form.get("text")
    threading.Thread(target=speak_async, args=(text,)).start()
    return jsonify(success=True)

def speak_async(text):
    language = 'es'  # Cambiar a 'en' si se desea utilizar inglés
    tts = gTTS(text=text, lang=language, slow=False)
    audio_file = "temp_audio.mp3"
    tts.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)

if __name__ == "__main__":
    app.run(debug=True)
