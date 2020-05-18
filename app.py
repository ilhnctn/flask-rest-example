from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/api/v1/fibonacci', methods=['POST'])
def get_fibo():
    """
    Sample request
        curl -H "Content-Type: application/json" \
            -X POST http://localhost:8080/api/v1/fibonacci \
            -d '{"username":"xyz","password":"xyz"}'
    """
    data = request.json
    return jsonify({'tasks': data})


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
