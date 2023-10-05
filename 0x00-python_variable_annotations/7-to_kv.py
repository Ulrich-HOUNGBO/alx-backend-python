#!/usr/bin/env python3

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns tuple of string and float """
    return k, v * v
