# -*- coding: utf-8 -*-

import os
import math


def contains(itemset: set, eliminated_itemsets: list):
    """Determine if any of the eliminated itemset is subset of the given itemset"""

    for e_itemset in eliminated_itemsets:
        if itemset <= e_itemset:
            return True
    return False


def frequent_itemsets(support_threshold: float, dataset: list):
    """
    Generate frequent itemsets using Apriori algorithm.

    Args:
        support_threshold: Minimum support threshold, floating value
        dataset: Output of parse.parse_dataset

    Returns:
    """

    # Clone to not modify original dataset object
    dataset = dataset.copy()
    dataset_len = len(dataset)
    min_support_count = math.ceil(support_threshold * dataset_len)
    # Maximum length of frequent itemset
    max_itemset_len = len(dataset[0])

    # IMPORTANT: Indexes of C and F starts at 1 for the sake of simplicity,
    # index 0 is empty, and will be disregarded with slicing operator.(e.g. [1:])
    #
    # Candidate itemsets
    # [[itemset, support count], ...]
    C = [[] for i in range(max_itemset_len + 1)]
    # Frequent itemsets
    L = [[] for i in range(max_itemset_len + 1)]

    for k in range(1, max_itemset_len + 1):
        # 1-itemsets
        if k is 1:
            counts = dict()
            for itemset in dataset:
                for item in itemset:
                    counts[item] = counts.get(item, 0) + 1

            for item in counts:
                C[k].append(({item, }, counts[item]))

        # k-itemsets
        else:
            # TODO: Candidate generation
            # Self join
            # Pruning

            print(L[k - 1])
            return None

        for pair in C[k]:  # pair = itemset, support_count
            if not pair[1] < min_support_count:
                L[k].append(pair)
