from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Elite Cyber Plex is running!"

    return app
