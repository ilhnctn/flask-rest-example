from typing import List


class FibonacciService(object):
    computed: List[int] = [0, 1, 1]

    def get_fibonacci_of_number(self, target: int) -> int:
        if not isinstance(target, int):
            raise Exception(f"Unsupported input type. int expected")

        if target < len(self.computed):
            return self.computed[target]

        for f in range(2, target):

            self.computed.append(self.computed[-1] + self.computed[-2])

        return self.computed[target]
