import unittest
from problemset import parse


class ParseTests(unittest.TestCase):

    decimalString = '12312312'
    floatString = '12312.323210'
    sampleString = 'bla bla'
    
    def test_normalize(self):
        assert int == type(parse.normalize(self.decimalString))
        assert float == type(parse.normalize(self.floatString))
        assert str == type(parse.normalize(self.sampleString))

    def test_parse_dataset(self):
        dataset = parse.parse_dataset()
        # may do more extensive test later
        if not dataset or len(dataset[0]) < 2:
            raise ValueError('Dataset is not parsed properly.')


if __name__ == '__main__':
    
    unittest.main()
