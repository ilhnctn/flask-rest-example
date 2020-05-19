

class FactorialService:
    def get_factorial_of_number(self, target: int) -> int:
        if not isinstance(target, int):
            raise Exception(f"Unsupported input type. int expected, got {type(target)}")

        result: int = 1

        for mid in range(1, target + 1):
            result *= mid

        return result
