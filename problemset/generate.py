# -*- coding: utf-8 -*-

from itertools import combinations
import math

from .metrics import Metric


def self_join(itemsets: set, length: int):
    """
    Self join a list of itemsets to the length.
    Time complexity is O(n^2 * maximum_itemset_length) where n is length of itemsets.

    Returns:
        Self join which maps every item to 0. Representation as below:
            dict{frozenset: 0, ...}
    """
    join = {}
    for itemset1 in itemsets:
        for itemset2 in itemsets:
            union = itemset1.union(itemset2)
            if len(union) == length:
                join[union] = 0
    return join


def apriori_gen(large_itemsets: set, k: int):
    """
    Generates candidate k-itemsets from k-1 large itemsets using a priori algorithm.
    * apriori-gen function described by Rakesh Agrawal and Ramakrishnan Srikant at 1994.


    Args:
        large_itemsets: k-1 large itemsets, set of frozensets
        k: length of itemsets to generate

    Returns:
        New candidate dict which maps to support counts. Initial support count is 0.
        Representation:
            dict{frozenset: 0, ...}
    """

    if not large_itemsets:
        return dict()

    C = self_join(large_itemsets, k)
    # Prune candidates
    deletion_set = set()
    for candidate in C.keys():
        for subset in map(frozenset, combinations(candidate, k - 1)):
            if subset not in large_itemsets:
                deletion_set.add(candidate)
                break
    map(C.pop, deletion_set)
    return C


def frequent_itemsets(support_threshold: float, dataset: list):
    """
    Generate frequent itemsets using Apriori algorithm.

    Args:
        support_threshold: Minimum support threshold
        dataset: Output of parse.parse_dataset

    Returns:
        List of sets of itemsets for 1 to k where k is maximum length of a transaction in dataset.
        Representation:
            list[
                set_1st{frozenset{item, ...}, ...}, 
                ..., 
                set_kth{frozenset{item, ...}, ...}
            ]

    """

    D = dataset.copy()
    minsup_count = math.ceil(support_threshold * len(D))
    k_max = len(D[0])
    # Map [C]andidate to support count
    C = dict()
    # [L]arge itemsets. Index of L starts at 1.
    L = [set() for i in range(k_max + 1)]

    for k in range(1, k_max + 1):

        # 1-itemsets
        if k is 1:
            for t in D:  # D for dataset, t for transaction
                for item in t:
                    item = frozenset({item})
                    C[item] = C.get(item, 0) + 1
        # k-itemsets
        else:
            C = apriori_gen(L[k - 1], k)

            for t in D:
                for c in C.keys():
                    if c <= t:
                        C[c] = C[c] + 1
    
        for c in C.keys():
            if not C[c] < minsup_count:
                L[k].add(c)

    # Normalize before returning
    return L[1:]


def association_rules(large_itemsets: list, metric: Metric, metric_threshold: float):
    pass
