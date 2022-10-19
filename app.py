from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import mlib

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.DEBUG)


@app.route("/")
def home():
    html = f"<h3>Predict the Height From Weight of MLB Players. CD</h3>"
    return html.format(format)

@app.route("/train")
def train():
    html = f"<h3>Retraining model ....</h3>"
    mlib.retrain()
    return html.format(format)
    

@app.route("/predict", methods=["GET","POST"])
def predict():
    """Predicts the Height of MLB Players"""

    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    prediction = mlib.predict(json_payload["Weight"])
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)