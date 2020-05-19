import pytest
from flask import json

from app import app


@pytest.mark.parametrize("start, end, expected", ((3, 2, 29), (3, 3, 61)))
def test_get_acckerman_result_of_known_values(start: int, end: int, expected: int) -> None:
    response = app.test_client().post(
        '/api/v1/acckerman',
        data=json.dumps({"start": start, "end": end}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['result'] == expected


def test_fails_with_unsupported_params() -> None:
    response = app.test_client().post(
        '/api/v1/acckerman',
        data=json.dumps({'target': "target"}),
        content_type='application/json',
    )

    assert response.status_code == 400
    assert str(response) == "<Response streamed [400 BAD REQUEST]>"
