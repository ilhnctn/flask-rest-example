import pytest

from apps.fibonacci.service import FibonacciService

fb_service = FibonacciService()


def test_fib_number_in_list_if_number_between_zero_and_two() -> None:
    assert fb_service.get_fibonacci_of_number(0) in [0, 1, 1]
    assert fb_service.get_fibonacci_of_number(2) in [0, 1, 1]
    assert fb_service.get_fibonacci_of_number(3) not in [0, 1, 1]


def test_various_known_fibonacci_results() -> None:
    assert fb_service.get_fibonacci_of_number(3) == 2
    assert fb_service.get_fibonacci_of_number(11) == 89


def test_fails_when_unsupported_input_sent() -> None:
    with pytest.raises(Exception):
        assert fb_service.get_fibonacci_of_number(target="asdf")
