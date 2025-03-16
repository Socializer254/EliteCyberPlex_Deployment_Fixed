import os
from flask import Flask, request

app = Flask(__name__)

# Load environment variables
BOT_API_KEY = os.getenv("BOT_API_KEY")
BOT_WEBHOOK_URL = os.getenv("BOT_WEBHOOK_URL")
DERIV_API_KEY = os.getenv("DERIV_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    # Process bot signals here
    return {"message": "Webhook received"}, 200

if __name__ == "__main__":
    app.run()
