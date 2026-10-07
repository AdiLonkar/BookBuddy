"""Book Buddy - Flask web app (run: python app.py, open http://127.0.0.1:5000)."""
from flask import Flask, jsonify, render_template, request
from book_logic import QUICK_TOPICS, get_book_buddy_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    return jsonify(get_book_buddy_response(data.get("message", "")))


@app.route("/api/quick-topics")
def quick_topics():
    return jsonify(QUICK_TOPICS)


if __name__ == "__main__":
    app.run(debug=True)