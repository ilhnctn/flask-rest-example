from json import loads
from typing import cast as Cast, List
from logging import getLogger

from core.service import CacheService

logger = getLogger(__name__)


class FibonacciService:

    def __init__(self, cache_service: CacheService) -> None:
        self.cache_service: CacheService = cache_service
        self.computed: List[int] = [0, 1, 1]

    def get_fibonacci_of_number(self, target: int) -> int:
        if not isinstance(target, int):
            raise Exception(f"Unsupported input type. int expected, got {type(target)}")

        in_cache: bytes = Cast(bytes, self.cache_service.get(key=str(target)))
        if in_cache:
            return int(loads(in_cache))

        if target < len(self.computed):
            return self.computed[target]

        for _ in range(2, target):
            self.computed.append(self.computed[-1] + self.computed[-2])

        return self.computed[target]
