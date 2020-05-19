import logging
from typing import Any, cast, Dict

from http import HTTPStatus

from flask import request, Blueprint, make_response

from apps.fibonacci.schema import FibonacciInputSchema
from apps.fibonacci.service import FibonacciService

fib_bp: Blueprint = Blueprint('fibonacci', __name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@fib_bp.route('/')
@fib_bp.route('/home')
def home() -> str:
    return "Welcome to the library Home."


fibonacci_service = FibonacciService()
fibonacci_schema = FibonacciInputSchema()


@fib_bp.route("/api/v1/fibonacci", methods=["POST"])
def post() -> Any:
    errors = fibonacci_schema.validate(request.json)

    if errors:
        logger.error(errors)
        return make_response({"message": errors}, HTTPStatus.BAD_REQUEST)

    data: Dict[str, int] = request.json
    logger.info("Requested data is: %s", str(data))
    target: int = cast(int, data.get("target"))
    result = fibonacci_service.get_fibonacci_of_number(target=target)

    if isinstance(result, str):
        return make_response({"message": result}, HTTPStatus.BAD_REQUEST)

    return make_response({'result': result}, HTTPStatus.OK)
