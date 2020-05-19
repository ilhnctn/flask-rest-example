import logging
from typing import Any, cast, Dict

from http import HTTPStatus
from flask.views import MethodView
from flask import request, make_response

from apps.factorial.service import FactorialService
from apps.factorial.schema import FactorialInputSchema

logger = logging.getLogger(__name__)


class FactorialView(MethodView):
    factorial_service = FactorialService()
    factorial_schema = FactorialInputSchema()

    def post(self) -> Any:

        errors = self.factorial_schema.validate(request.json)
        if errors:
            logger.error(errors)
            return make_response({"message": errors}, HTTPStatus.BAD_REQUEST)

        data: Dict[str, int] = request.json
        logger.info("Requested data is %s", str(data))
        target: int = cast(int, data.get("target"))
        result = self.factorial_service.get_factorial_of_number(target=target)

        if isinstance(result, str):
            return make_response({"message": result}, HTTPStatus.BAD_REQUEST)
        return make_response({'result': result}, HTTPStatus.OK)
