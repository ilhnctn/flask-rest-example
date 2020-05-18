from logging import getLogger

from typing import Union

logger = getLogger(__name__)


class AcckermanService(object):

    def get_acckerman_result_of_numbers(self, start: int, end: int) -> Union[int, str]:
        # TODO BUG: Doesn't stop on RecursionError, continues.
        if not all([isinstance(x, int) for x in [start, end]]):
            return f"Parameters are: {start} --and-- {end} "

        if start == 0:
            result = end + 1
            return result
        elif end == 0:
            result = self.get_acckerman_result_of_numbers(start=start - 1, end=1)
            return result
        else:
            try:

                result = self.get_acckerman_result_of_numbers(start=start - 1,
                                                              end=self.get_acckerman_result_of_numbers(start=start,
                                                                                                       end=end - 1))
                return result
            except (RecursionError, Exception) as r:
                logger.warning(r)
                return f"Recursion error: {str(r)}"
