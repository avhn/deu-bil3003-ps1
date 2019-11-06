# -*- coding: utf-8 -*-

import os

from problemset import interact
from problemset import parse
from problemset import generate

LOG_FILE = 'out.txt'


def main():

    support_threshold, metric, metric_threshold, filepath = interact.get_input()
    dataset = parse.parse_dataset(filepath)
    frequent_itemsets = generate.frequent_itemsets(support_threshold, dataset)
    interact.print_frequent_itemsets(frequent_itemsets, LOG_FILE)
    association_rules = generate.association_rules(dataset, frequent_itemsets, metric, metric_threshold)
    interact.print_association_rules(association_rules, LOG_FILE, metric)

    print("Log file written at {}".format(os.path.join(os.getcwd(), LOG_FILE)))


if __name__ == '__main__':
    main()
