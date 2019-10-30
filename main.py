# -*- coding: utf-8 -*-

from problemset import interact
from problemset import parse, gen_itemset


def dev_test():
    indicators, dataset = parse.parse_dataset(None)
    gen_itemset.gen_freq_itemsets(None, dataset)


def main():
    support_value, metric, leverage_value, filepath = interact.get_input()

    indicators, dataset = parse.parse_dataset()
    gen_itemset.gen_freq_itemsets(None, dataset)


if __name__ == '__main__':
    dev_test()
