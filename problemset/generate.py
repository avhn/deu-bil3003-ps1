# -*- coding: utf-8 -*-

import math
import random


def self_join(itemsets: list, length: int):
    """
    Self join a list of itemsets to the length.
    Time complexity is O(n^2 * maximum_itemset_length) where n is length of itemsets.

    Returns:
        Initial support count is 0. Representation as below:
            dict{frozenset: 0, ...}
    """

    join = {}
    for itemset1 in itemsets:
        for itemset2 in itemsets:
            union = itemset1.union(itemset2)
            if len(union) == length:
                join[union] = 0
    return join


def frequent_itemsets(support_threshold: float, dataset: list):
    """
    Generate frequent itemsets using Apriori algorithm.

    Args:
        support_threshold: Minimum support threshold
        dataset: Output of parse.parse_dataset

    Returns:
    """

    # Clone to not modify original object
    D = dataset.copy()
    dataset_len = len(D)
    minsup_count = math.ceil(support_threshold * dataset_len)
    # Maximum length of frequent itemset
    k_max = len(D[0])

    # Store both candidates and minsup counts in the hashtable.
    C = dict()
    # Index of L start at 1. L stores itemsets every level.
    L = [[] for i in range(k_max + 1)]
    # Representation of L:
    #   L[[], list_1[frozenset(item, ...), ...], ..., list_k[frozenset(item, ...)]]

    k = 1
    # 1-itemsets

    for itemset in dataset:
        for item in itemset:
            C[item] = C.get(item, 0) + 1
    # pair -> frozenset, support_count
    for item in C:
        if not C[item] < minsup_count:
            L[k].append(frozenset({item}))

    # k-itemsets
    for k in range(2, k_max + 1):
        C.clear()
        C = self_join(L[k - 1], k)
        for t in D:
            for c in C.keys():
                if c <= t:
                    C[c] = C[c] + 1

        for c in C.keys():
            if not C[c] < minsup_count:
                L[k].append(c)

    # Index started from 1, normalize before returning
    return L[1:]
