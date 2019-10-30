# -*- coding: utf-8 -*-

import os


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
    # Maximum length of frequent itemset
    max_itemset_len = len(dataset[0])
    dataset_len = len(dataset)

    # IMPORTANT: Indexes of C and F starts at 1 for the sake of simplicity,
    # index 0 is empty, and will be disregarded with slicing operator.(e.g. [1:])
    #
    # Candidate itemsets
    # [itemset, ...]
    C = [{} for i in range(max_itemset_len + 1)]
    # Frequent itemsets
    # [{itemset: support value, ...}, ...]
    F = [{} for i in range(max_itemset_len + 1)]

    for k in range(1, max_itemset_len + 1):
        # 1-itemsets
        if k is 1:
            for itemset in dataset:
                for item in itemset:
                    C[k][(item, )] = C[k].get((item, ), 0) + 1
        # k-itemsets
        else:
            ordered = tuple(F[k - 1].keys())
            print(ordered)
            os._exit(0)

        eliminated_itemsets = []  # Eliminated itemsets
        for itemset in C[k].keys():
            support_val = C[k][itemset] / dataset_len
            if support_val < support_threshold:
                # add to remove later from dataset
                eliminated_itemsets.append(itemset)
            else:
                F[k][itemset] = support_val

        dataset = [itemset for itemset in dataset
                   if not contains(itemset, eliminated_itemsets)]
