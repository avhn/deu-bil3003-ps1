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
        if value:  # not None
            value = value.strip()
        return value


def parse_dataset(filename='dataset.csv'):
    """
    Parse .csv file.

    Args:
        filename: name of the .csv file

    Returns:
        Parsed dataset as list of lists with first index being the indicator of column.
        For example:
            (ind1, ind2, ...), [(val1, val2, ...), (val1, val2, ...) ...]
    """

    indicators = None
    dataset = list()
    with open(filename, 'r') as file:
        for iter, line in enumerate(file):
            line = line.strip().split(',')
            if iter is 0:
                indicators = tuple([item.strip() for item in line])
            else:
                items = list()
                for item in line:
                    if item == '?':
                        item = None
                    items.append(normalize(item))
                dataset.append(tuple(items))
    return indicators, dataset
