

class FactorialService(object):
    def get_factorial_of_number(self, target: int) -> int:
        result: int = 1

        for x in range(1, target + 1):
            result *= x

        return result
