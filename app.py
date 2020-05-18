import logging
from typing import Any, cast, Dict

from flask import Flask, jsonify, abort
from flask import request

from apps.acckerman.schema import AcckermanInputSchema
from apps.acckerman.service import AcckermanService

from apps.factorial.schema import FactorialInputSchema
from apps.factorial.service import FactorialService

from apps.fibonacci.schema import FibonacciInputSchema
from apps.fibonacci.service import FibonacciService

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

acckerman_schema = AcckermanInputSchema()
acckerman_service = AcckermanService()

fib_service = FibonacciService()
fibonacci_schema = FibonacciInputSchema()

factorial_service = FactorialService()
factorial_schema = FactorialInputSchema()


@app.route('/api/v1/acckerman', methods=['POST'])
def get_acckerman_of_two_inputs() -> Any:
    errors = acckerman_schema.validate(request.json)

    if errors:
        logger.error(errors)
        abort(400, str(errors))

    data: Dict[str, int] = request.json
    logger.info("Requested data is %s", str(data))

    end: int = cast(int, data.get("end"))
    start: int = cast(int, data.get("start"))
    result = acckerman_service.get_acckerman_result_of_numbers(start=start,
                                                               end=end)

    if isinstance(result, str):
        abort(400, result)
    return jsonify({'result': result})


@app.route('/api/v1/factorial', methods=['POST'])
def get_factorial_of_number() -> Any:
    errors = factorial_schema.validate(request.json)

    if errors:
        logger.error(errors)
        abort(400, str(errors))

    data: Dict[str, int] = request.json
    logger.info("Requested data is %s", str(data))
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
    logger.info("Requested data is: %s", str(data))
    target: int = cast(int, data.get("target"))
    result = fib_service.get_fibonacci_of_number(target=target)
    if isinstance(result, str):
        abort(400, result)
    return jsonify({'result': result})


@app.route('/')
def index() -> str:
    """
    Demo view
    :return: str
    """
    return "Hello, World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
