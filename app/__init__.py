from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Elite Cyber Plex is running!"
