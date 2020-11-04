"""
This module defines what will happen in stage-2a.
"""
import sys

import requests
from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route('/v2/predict', methods=['GET', 'POST'])
def predict():
    return make_response(jsonify({'y': 'hello_world'}))


if __name__ == '__main__':
    sys.exit(1)
    app.run(host='0.0.0.0', port=5000)
