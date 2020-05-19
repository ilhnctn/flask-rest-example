import logging
from typing import Any, cast, Dict

from http import HTTPStatus
from flask.views import MethodView
from flask import request, make_response

from apps.acckerman.service import AcckermanService
from apps.acckerman.schema import AcckermanInputSchema

logger = logging.getLogger(__name__)


class AcckermanView(MethodView):
    acckerman_service = AcckermanService()
    acckerman_schema = AcckermanInputSchema()

    def post(self) -> Any:

        errors = self.acckerman_schema.validate(request.json)
        if errors:
            logger.error(errors)
            return make_response({"message": errors}, HTTPStatus.BAD_REQUEST)

        data: Dict[str, int] = request.json
        logger.info("Requested data is %s", str(data))
        end: int = cast(int, data.get("end"))
        start: int = cast(int, data.get("start"))
        result = self.acckerman_service.get_acckerman_result_of_numbers(
            start=start, end=end)

        if isinstance(result, str):
            return make_response({"message": result}, HTTPStatus.BAD_REQUEST)
        return make_response({'result': result}, HTTPStatus.OK)
