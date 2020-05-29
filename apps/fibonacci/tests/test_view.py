from unittest import TestCase
from unittest.mock import patch

import pytest

from flask import json

from app import app


class FibonacciViewTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @pytest.mark.parametrize("target, expected", ((12, 144), (2, 1)))
    def test_get_factorial(self, target: int, expected: int) -> None:
        response = app.test_client().post(
            '/api/v1/fibonacci',
            data=json.dumps({'target': target}),
            content_type='application/json',
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['result'] == expected

    def test_fails_with_unsupported_param(self) -> None:
        response = app.test_client().post(
            '/api/v1/fibonacci',
            data=json.dumps({'target': "target"}),
            content_type='application/json',
        )

        assert response.status_code == 400
