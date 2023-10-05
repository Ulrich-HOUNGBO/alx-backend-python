#!/usr/bin/env python3
""" Module for type-annotated function to_kv """
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns tuple of string and float """
    return k, v * v
