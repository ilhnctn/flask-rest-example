from logging import getLogger

from typing import Any

logger = getLogger(__name__)


class AcckermanService:

    def get_acckerman_result_of_numbers(self,
                                        start: int,
                                        end: int) -> Any:
        # TODO BUG: Doesn't stop on RecursionError, continues.
        if not all([isinstance(x, int) for x in [start, end]]):
            return f"Parameters are: {start} --and-- {end} "

        if start == 0:
            result = end + 1
            return result

        if end == 0:
            result = self.get_acckerman_result_of_numbers(start=start - 1, end=1)
            return result

        try:

            result = self.get_acckerman_result_of_numbers(
                start=start - 1,
                end=self.get_acckerman_result_of_numbers(start=start,
                                                         end=end - 1))
            return result
        except (RecursionError, Exception) as err:
            logger.warning(err)
            return f"Recursion error: {str(err)}"
