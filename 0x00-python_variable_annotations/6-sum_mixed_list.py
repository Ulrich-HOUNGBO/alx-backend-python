#!/usr/bin/env python3
""" Module for type-annotated function sum_mixed_list """""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns sum of mixed list """
    return sum(mxd_lst)
