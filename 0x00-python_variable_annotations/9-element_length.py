#!/usr/bin/env python3
""" Annotate the below function’s parameters and return values with the"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns list of tuples, one for each element of lst, containing the"""
    return [(i, len(i)) for i in lst]
