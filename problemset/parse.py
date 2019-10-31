# -*- coding: utf-8 -*-


def normalize(value: str):
    """Convert a String object to floating or decimal and ? to None if possible."""

    value = value.strip()
    try:
        if value.isdigit():
            result = int(value)
        else:
            result = float(value)
        return result

    except (ValueError, AttributeError):
        if value is '?':
            return None
        return value


def parse_dataset(filename: str = 'dataset.csv'):
    """
    Parse .csv file.

    Args:
        filename: name or path of the .csv file

    Returns:
        Parsed dataset as list of itemsets, where items are tuples.
        Pseudo representation as below:
            list[frozenset{tuple(ind, val), ...}, frozenset{tuple(ind, val), ...}, ...]

        Every single record is itemized by making them hashable with tuple(ind, val) to adapt
        market basket problem.
    """

    if not filename:
        return parse_dataset()

    indicators = tuple()
    itemsets = list()
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            line = line.strip().split(',')
            if i is 0:  # get indicators
                indicators = tuple([item.strip() for item in line])
            else:   # create itemset and add to itemsets
                itemset = set()
                for j, item in enumerate(line):
                    itemset.add((indicators[j], normalize(item)))
                itemsets.append(frozenset(itemset))
    return itemsets
