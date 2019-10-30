# -*- coding: utf-8 -*-

from problemset import interact
from problemset import parse, generate


def dev_test():
    dataset = parse.parse_dataset()
    generate.frequent_itemsets(0.04, dataset)


def main():
    support_value, metric, leverage_value, filepath = interact.get_input()

    indicators, dataset = parse.parse_dataset()
    gen_itemset.gen_freq_itemsets(None, dataset)


if __name__ == '__main__':
    dev_test()
