from flask import Flask, jsonify, request
import random

app = Flask(__name__)

compliments = [
    "You are unstoppable!",
    "Your code gets better every day!",
    "Your focus today is 🔥",
]

@app.route("/", methods=["GET"])
def index():
    return jsonify(endpoints=["/compliment (GET, POST)", "/compliments (GET)"])

@app.route("/compliment", methods=["GET"])
def get_random():
    return jsonify(compliment=random.choice(compliments))

@app.route("/compliments", methods=["GET"])
def get_all():
    return jsonify(compliments=compliments)

@app.route("/compliment", methods=["POST"])
def add_one():
    data = request.get_json() or {}
    text = (data.get("text") or "").strip()



    if not text:
        return jsonify(error="Field 'text' is required and cannot be empty"), 400
    if len(text) > 140:
        return jsonify(error="Compliment must be 140 chars or fewer"), 400
    if text in compliments:
        return jsonify(error="This compliment already exists"), 409

    compliments.append(text)
    return jsonify(added=text), 201

if __name__ == "__main__":
    app.run(debug=True, port=5003, use_reloader=False)
