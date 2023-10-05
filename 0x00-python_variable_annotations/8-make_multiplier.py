#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns function that multiplies a float by multiplier """

    def multiply_by_multiplier(num: float) -> float:
        """ Returns num multiplied by multiplier """
        return num * multiplier

    return multiply_by_multiplier
