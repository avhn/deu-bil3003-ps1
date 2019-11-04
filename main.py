# -*- coding: utf-8 -*-

from problemset import interact
from problemset import parse
from problemset import generate
from problemset.utils import Metric


def dev_test():
    dataset = parse.parse_dataset()
    frequent_itemsets = generate.frequent_itemsets(0.1, dataset)
    for i, l in enumerate(frequent_itemsets):
        print("LEVEL {}".format(i + 1))
        for itemset in l:
            print(itemset)
    
    association_rules = generate.association_rules(dataset, frequent_itemsets, Metric.Confidence, 0.97)
    for i in association_rules:
        print(i[0], '->', i[1])


def main():
    LOG_FILE = 'out.txt'
    support_threshold, metric, metric_threshold, filepath = interact.get_input()
    dataset = parse.parse_dataset(filepath)
    frequent_itemsets = generate.frequent_itemsets(support_threshold, dataset)
    interact.print_frequent_itemsets(frequent_itemsets, LOG_FILE)
    association_rules = generate.association_rules(dataset, frequent_itemsets, metric, metric_threshold)
    interact.print_association_rules(association_rules, LOG_FILE, metric)


if __name__ == '__main__':
    main()
