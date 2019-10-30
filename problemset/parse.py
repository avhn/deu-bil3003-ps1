# -*- coding: utf-8 -*-


def normalize(value):
    """Convert a String object to floating or decimal if possible."""

    try:
        if value.isdigit():
            result = int(value)
        else:
            result = float(value)
        return result

    except (ValueError, AttributeError):
        return value.strip()


def parse_dataset(filename='dataset.csv'):
    """
    Parse .csv file.

    Args:
        filename: name of the .csv file

    Returns:
        Parsed dataset as list of itemsets, where items are tuples.
        Pseudo representation as below:
            list[set{tuple(ind, val), ...}, set{tuple(ind, val), ...}, ...]
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
                itemsets.append(itemset)
    return itemsets
