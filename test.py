import unittest
import random

from problemset import parse
from problemset import generate


class ParseTests(unittest.TestCase):

    decimalString = '12312312'
    floatString = '12312.323210'
    sampleString = 'bla bla'

    def test_normalize(self):
        assert int is type(parse.normalize(self.decimalString))
        assert float is type(parse.normalize(self.floatString))
        assert str is type(parse.normalize(self.sampleString))

    def test_parse_dataset(self):
        itemsets = parse.parse_dataset()
        assert itemsets and type(itemsets) is list
        itemset = itemsets[0]
        assert itemset and type(itemset) is frozenset
        item = random.choice(tuple(itemset))
        assert item and type(item) is tuple


class AprioriTests(unittest.TestCase):

    def test_frequent_itemsets(self):
        dataset = parse.parse_dataset()
        frequent_itemsets = generate.frequent_itemsets(0.05, dataset)
        assert frequent_itemsets
        assert len(frequent_itemsets) is len(dataset[0])
        assert type(frequent_itemsets) is list
        one_itemsets = frequent_itemsets[0]
        assert type(one_itemsets) is set
        assert len(one_itemsets) is 0 or type(random.sample(one_itemsets, 1)[0]) is frozenset

    def test_association_rules(self):
        pass


if __name__ == '__main__':

    unittest.main()
