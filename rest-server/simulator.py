import logging

import counter
import random

logger = logging.getLogger(__name__)


class Simulator(counter.Counter):

    def __init__(self, cnt=1):
        logger.info('Starting simulator module')
        super().__init__(cnt)
        self._blink = False


    @property
    def random(self):
        return round(random.random() * 100, 3)

    @property
    def blink(self):
        if not self._blink:
            self._blink = True
        else:
            self._blink = False
        return self._blink


if __name__ == '__main__':  # pragma: no cover, don't test main
    logging.basicConfig(level=logging.DEBUG)
    s = Simulator()
    print(f'{s.counter=}')
    print(f'{s.random=}')
    print(f'{s.blink=}')