from flask import Flask, render_template, request, redirect
import json
import os.path
from datetime import datetime

app = Flask(__name__)

def load_messages():
    if not os.path.exists("messages.json"):
        with open("messages.json", "w") as f:
            json.dump([], f)
    with open("messages.json") as f:
        messages = json.load(f)
    return sorted(messages, key=lambda x: x['date'])

def created_message(name, message):
    messages = load_messages()
    messages.append({
        "name": name,
        "message": message,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    with open("messages.json", "w") as f:
        json.dump(messages, f)

@app.route("/")
def index():
    messages = load_messages()
    return render_template("index.html", messages=messages)

@app.route("/post", methods=["POST"])
def post():
    name = request.form["name"]
    message = request.form["message"]
    created_message(name, message)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)