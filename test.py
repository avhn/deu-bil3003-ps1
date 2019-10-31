import unittest
import random

from problemset import parse
from problemset import generate


class ParseTests(unittest.TestCase):

    decimalString = '12312312'
    floatString = '12312.323210'
    sampleString = 'bla bla'

    def test_normalize(self):
        assert int == type(parse.normalize(self.decimalString))
        assert float == type(parse.normalize(self.floatString))
        assert str == type(parse.normalize(self.sampleString))

    def test_parse_dataset(self):
        itemsets = parse.parse_dataset()
        assert itemsets and type(itemsets) is list
        itemset = itemsets[0]
        assert itemset and type(itemset) is frozenset
        item = random.choice(tuple(itemset))
        assert item and type(item) is tuple

    def test_generate_frequent_itemsets(self):
        dataset = parse.parse_dataset()
        frequent_itemsets = generate.frequent_itemsets(0.1, dataset)

        assert frequent_itemsets and len(frequent_itemsets) is len(dataset[0])


if __name__ == '__main__':

    unittest.main()
