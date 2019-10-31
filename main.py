# -*- coding: utf-8 -*-

from problemset import interact
from problemset import parse, generate


def dev_test():
    dataset = parse.parse_dataset()
    frequent_itemsets = generate.frequent_itemsets(0.05, dataset)
    for i, l in enumerate(frequent_itemsets):
        print("LEVEL {}".format(i + 1))
        for itemset in l:
            print(itemset, l[itemset] * len(dataset))


def main():
    support_value, metric, leverage_value, filepath = interact.get_input()

    indicators, dataset = parse.parse_dataset(filepath)
    generate.frequent_itemsets(None, dataset)


if __name__ == '__main__':
    dev_test()
