from typing import List
from logging import getLogger

logger = getLogger(__name__)


class FibonacciService:
    computed: List[int] = [0, 1, 1]

    def do_something(self) -> None:
        pass

    def get_fibonacci_of_number(self, target: int) -> int:
        if not isinstance(target, int):
            raise Exception(f"Unsupported input type. int expected, got {type(target)}")

        if target < len(self.computed):
            return self.computed[target]

        for _ in range(2, target):
            self.computed.append(self.computed[-1] + self.computed[-2])

        return self.computed[target]
