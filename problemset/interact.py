# -*- coding: utf-8 -*-

import os
from itertools import chain

from .utils import Metric
from .utils import print_and_write
from .utils import format_item
from .utils import round_2

INDENT = ' ' * 4
LINE = '-' * 50

name_switch = {
    Metric.Confidence: 'Confidence',
    Metric.Leverage: 'Leverage',
    Metric.Lift: 'Lift'
}

validation_switch = {
    Metric.Confidence: lambda x: 0 <= x <= 1,
    Metric.Leverage: lambda x: -0.25 <= x <= 0.25,
    Metric.Lift: lambda x: 0 <= x
}

def get_input():
    """
    Get corresponding inputs from user.

    Returns:
        A tuple such as:
            (minimum support value, metric, metric value, filepath to parse)
    """
    
    print(LINE + os.linesep)
    try:
        minsup = float(input('Minimum support value:\t'))
        if not 0 <= minsup <= 1:
            raise ValueError("Invalid support value: " + minsup)

        metric = int(
            input('Choose metric. Confidence[1] / Lift[2] / Leverage[3]:\t'))
        for m in Metric:
            if metric == m.value:
                metric = m
                break
        if metric not in Metric:
            raise ValueError("Invalid metric option -> {}"
                             .format(metric))

        minsup_threshold = float(input('Minimum metric threshold:\t'))
        if not validation_switch[metric](minsup_threshold):
            raise ValueError("Invalid {} value: {}".format(name_switch[metric], minsup_threshold))

        filepath = input(
            'Absolute filepath which contains comma seperated values [Enter for default]:\t')

        return minsup, metric, minsup_threshold, filepath

    except (ValueError, TypeError) as e:
        print("{}Invalid input:{}\t{}"
              .format(os.linesep, os.linesep, e))

    except KeyboardInterrupt:
        print("Keyboard interrupt received, closing.")
        os._exit(0)

    except BaseException as e:
        print("{}Encountered unexpected exception: {}"
              .format(os.linesep, e))
    
    print("Restarting input sequence." + os.linesep)
    return get_input()


def print_frequent_itemsets(frequent_itemsets: list, filepath: str):
    """
    Args:
        frequent_itemset: Output of .generate.frequent_itemsets
        filepath: Name of a file or absolute filepath
    """
    
    with open(filepath, 'a+') as file:
        print_and_write(os.linesep + LINE, file)
        print_and_write("{}Frequent item sets:{}".format(*(os.linesep * 2)), file)
        for itemset in chain.from_iterable(frequent_itemsets):
            string = INDENT + '{ '
            for item in itemset:
                string += format_item(item) + ", "
            string = string[:-2] + " }"
            print_and_write(string, file)


def print_association_rules(association_rules: list, filepath: str, metric: Metric):
    """
    Args:
        association_rules: Output of .generate.association_rules
        filepath: Name of a file or absolute filepath
        metric: Metric enum
    """
    
    with open(filepath, 'a+') as file:
        print_and_write(os.linesep + LINE, file)
        print_and_write("{}Association rules:{}".format(*(os.linesep * 2)), file)
        for i, rule in enumerate(association_rules):
            rule, support, metric_value  = rule

            string = INDENT + '{}. IF '.format(i + 1)
            for item in rule[0]: # antecedent
                string += format_item(item) + ' AND '
            string = string[:-4] + "THEN "
            for item in rule[1]: # consequent
                string += format_item(item) + ' AND '
            string = string[:-4] + os.linesep + INDENT \
                    + '-> with Support: {} and {}: {}' .format(round_2(support), name_switch[metric], round_2(metric_value)) \
                    + os.linesep
            print_and_write(string, file)
