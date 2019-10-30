# -*- coding: utf-8 -*-

import math


def frequent_itemsets(support_threshold, dataset):
    """
    Generate frequent itemsets using Apriori algorithm.

    Args:
        support_threshold: Minimum support threshold, floating value
        dataset: Output of parse.parse_dataset

    Returns:


    """

    min_support_count = math.ceil(min_support * len(dataset))

    k = len(dataset[0])
    C = k * []
