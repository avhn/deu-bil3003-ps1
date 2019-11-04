from enum import Enum


class Metric(Enum):
    Confidence = 1
    Lift = 2
    Leverage = 3


def support(D: list, a: frozenset, b: frozenset = None):
    """Calculate support value of given itemset/s in D."""

    if b:
        a = a.union(b)

    count = 0
    for t in D:
        if a <= t:
            count += 1
    return count / len(D)


def confidence(D: list, a: frozenset, b: frozenset):
    """Calculate confidence value. Range: [0, 1]"""
    return support(D, a, b) / support(D, a)


def leverage(D: list, a: frozenset, b: frozenset):
    """Calculate leverage value. Range: [-1, 1]"""

    return support(D, a, b) - support(D, a) * support(D, b)


def lift(D: list, a: frozenset, b: frozenset):
    """Calculate lift value. Range: [0, inf]"""

    return confidence(D, a, b) / support(D, b)
