from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # ✅ allow requests from GitHub Pages

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    duration = float(data.get("duration", 200))
    stops = int(data.get("stops", 1))
    price = 2500 + duration * 5 + stops * 1000
    return jsonify({"predicted_price": price})

@app.route("/", methods=["GET"])
def home():
    return "🚀 Travel Price Prediction API is running with CORS enabled!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
