

class FactorialService:
    def get_factorial_of_number(self, target: int) -> int:
        result: int = 1

        for mid in range(1, target + 1):
            result *= mid

        return result
