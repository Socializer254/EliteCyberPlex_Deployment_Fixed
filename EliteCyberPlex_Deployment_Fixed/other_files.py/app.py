import os
from flask import Flask

app = Flask(__name__)

# Load environment variables
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_key")
app.config["API_KEY"] = os.getenv("API_KEY", "default_api_key")

@app.route("/")
def home():
    return "Elite Cyber Plex is running with secured environment variables!"

if __name__ == "__main__":
    app.run()
