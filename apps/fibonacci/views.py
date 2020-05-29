import logging
from typing import Any, cast, Dict

from http import HTTPStatus

from flask import request, Blueprint, make_response
from redis import StrictRedis

from apps.fibonacci.schema import FibonacciInputSchema
from apps.fibonacci.service import FibonacciService
from core.utils import get_redis_client
from core.service import CacheService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

fib_bp: Blueprint = Blueprint('fibonacci', __name__)
redis_client: StrictRedis = get_redis_client()

cache_service: CacheService = CacheService(r_client=get_redis_client())
fibonacci_service = FibonacciService(cache_service=cache_service)
fibonacci_schema = FibonacciInputSchema()


@fib_bp.route("/api/v1/fibonacci", methods=["POST", "GET"])
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
