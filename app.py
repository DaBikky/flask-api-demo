import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Intentionally hard-coded for the first commit.
# This is a fake credential for the case study.
API_KEY = "AKIAIOSFODNN7EXAMPLE"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/analyze", methods=["POST"])
def analyze():
    if request.headers.get("X-API-Key") != API_KEY:
        return jsonify({"error": "Invalid or missing API key"}), 401

    data = request.get_json(silent=True)

    if not data or "text" not in data:
        return jsonify({"error": "JSON body with 'text' is required"}), 400

    text = data["text"]

    if not isinstance(text, str):
        return jsonify({"error": "'text' must be a string"}), 400

    if not text.strip():
        return jsonify({"error": "'text' cannot be empty"}), 400

    if len(text) > 1000:
        return jsonify({"error": "'text' cannot exceed 1000 characters"}), 400

    words = text.split()

    return jsonify({
        "text": text,
        "characters": len(text),
        "words": len(words),
        "uppercase": text.upper()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
