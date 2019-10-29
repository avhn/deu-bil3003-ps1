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
        return value


def parse_dataset(filename='dataset.csv'):

    """
    Parse .csv file.

    Args:
        filename: name of the .csv file

    Returns:
        Parsed dataset as list of lists with first index being the indicator of column.
        For example:
            [[ind1, ...], [ind2, ...], [ind3, ...] ...]
    """

    dataset = list()
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if len(dataset) == 0:
                dataset = [[item] for item in line]
            else:
                for i, item in enumerate(line):
                    if item == '?':
                        item = None
                    dataset[i].append(normalize(item))
    return dataset
