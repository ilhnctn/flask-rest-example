import logging
from typing import Any, cast, Dict

from flask import Flask, jsonify, abort
from flask import request

from apps.factorial.service import FactorialService
from apps.factorial.schema import FactorialInputSchema

from apps.fibonacci.service import FibonacciService
from apps.fibonacci.schema import FibonacciInputSchema

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

fib_service = FibonacciService()
fibonacci_schema = FibonacciInputSchema()

factorial_service = FactorialService()
factorial_schema = FactorialInputSchema()


@app.route('/api/v1/factorial', methods=['POST'])
def get_factorial_of_number() -> Any:
    errors = factorial_schema.validate(request.json)

    if errors:
        logger.error(errors)
        abort(400, str(errors))

    data: Dict[str, int] = request.json
    logger.info(f"Requested data is {data}")
    target: int = cast(int, data.get("target"))
    result = factorial_service.get_factorial_of_number(target=target)

    return jsonify({'result': result})


@app.route('/api/v1/fibonacci', methods=['POST'])
def get_fibonacci_of_number() -> Any:
    errors = fibonacci_schema.validate(request.json)

    if errors:
        logger.error(errors)
        abort(400, str(errors))

    data: Dict[str, int] = request.json
    logger.info(f"Requested data is {data}")
    target: int = cast(int, data.get("target"))
    result = fib_service.get_fibonacci_of_number(target=target)

    return jsonify({'result': result})


@app.route('/')
def index() -> str:
    return "Hello, World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
