from unittest import TestCase
import pytest

from core.service import CacheService
from core.test_utils import get_fake_redis
from apps.fibonacci.service import FibonacciService


class FibonacciServiceTestCase(TestCase):
    def setUp(self) -> None:
        cache_service = CacheService(r_client=get_fake_redis())
        self.fib_service = FibonacciService(cache_service=cache_service)

    def tearDown(self) -> None:
        pass

    def test_fib_number_in_list_if_number_between_zero_and_two(self) -> None:
        assert self.fib_service.get_fibonacci_of_number(0) in [0, 1, 1]
        assert self.fib_service.get_fibonacci_of_number(2) in [0, 1, 1]
        assert self.fib_service.get_fibonacci_of_number(3) not in [0, 1, 1]

    def test_various_known_fibonacci_results(self) -> None:
        assert self.fib_service.get_fibonacci_of_number(3) == 2
        assert self.fib_service.get_fibonacci_of_number(11) == 89

    def test_fails_when_unsupported_input_sent(self) -> None:
        with pytest.raises(Exception):
            assert self.fib_service.get_fibonacci_of_number(target="asdf")  # type: ignore
