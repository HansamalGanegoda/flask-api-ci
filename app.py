# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    a = 2
    b = 3
    result = a + b
    return jsonify({'result': result})

@app.route('/subtract', methods=['GET'])
def subtract():
    a = 5
    b = 3
    result = a - b
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
