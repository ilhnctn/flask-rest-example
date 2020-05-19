import pytest
from apps.factorial.service import FactorialService

f_srv = FactorialService()


@pytest.mark.parametrize("target, expected", ((1, 1), (2, 2), (3, 6)))
def test_various_known_factorial_results(target: int, expected: int) -> None:
    assert f_srv.get_factorial_of_number(target) == expected


def test_fails_when_unsupported_input_sent() -> None:
    with pytest.raises(Exception):
        assert f_srv.get_factorial_of_number(target="asdf")  # type: ignore
