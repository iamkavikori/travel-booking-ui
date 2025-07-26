from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    duration = float(data.get("duration", 200))
    stops = int(data.get("stops", 1))
    
    # Simple price formula instead of ML model
    price = 2500 + duration * 5 + stops * 1000
    return jsonify({"predicted_price": price})

@app.route("/", methods=["GET"])
def home():
    return "🚀 Travel Price Prediction API is running (using dummy logic)!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
