from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_API = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_message():
    user_message = request.json["message"]

    response = requests.post(
        RASA_API,
        json={"sender": "user", "message": user_message}
    )

    bot_responses = response.json()

    if bot_responses:
        return jsonify({"reply": bot_responses[0]["text"]})
    else:
        return jsonify({"reply": "Sorry, I didn't understand."})

if __name__ == "__main__":
    app.run(port=5000)