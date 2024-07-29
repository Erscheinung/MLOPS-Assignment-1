# predict.py

from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

def load_model():
    # Load the saved model
    model = joblib.load("random_forest_model.pkl")
    return model

model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        prediction = model.predict([data["features"]])
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
