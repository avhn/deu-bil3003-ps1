# -*- coding: utf-8 -*-

from problemset import interact
from problemset import parse, generate


def dev_test():
    dataset = parse.parse_dataset(None)
    generate.frequent_itemsets(0.5, dataset)


def main():
    support_value, metric, leverage_value, filepath = interact.get_input()

    indicators, dataset = parse.parse_dataset()
    gen_itemset.gen_freq_itemsets(None, dataset)


if __name__ == '__main__':
    dev_test()
