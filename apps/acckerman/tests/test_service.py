import pytest
from apps.acckerman.service import AcckermanService

acckerman_service = AcckermanService()


@pytest.mark.parametrize("start, end, expected", ((3, 2, 29), (3, 3, 61), ))
def test_various_known_acckerman_results(start: int, end: int, expected: int) -> None:
    assert acckerman_service.get_acckerman_result_of_numbers(start, end) == expected


@pytest.mark.parametrize("start, end", ((4, 3), (5, 3), (8, 3)))
def test_fails_when_too_big_input_supplied(start: int, end: int) -> None:
    with pytest.raises(Exception):
        assert acckerman_service.get_acckerman_result_of_numbers(start=start, end=end)
