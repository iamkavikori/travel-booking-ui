from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# ✅ Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    duration = data['duration']
    stops = data['stops']
    
    # Example: model expects features [duration, stops]
    features = np.array([[duration, stops]])
    prediction = model.predict(features)[0]
    
    return jsonify({'predicted_price': float(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
