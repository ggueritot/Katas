import unittest
from collections import OrderedDict

values = OrderedDict([(1000, "M"), (500, "D"), (100, "C"), (50, "L"), (10, "X"), (5, "V"), (1, "I")])
prefixes = {5: 1, 10: 1, 50: 10, 100: 10, 500: 100, 1000: 100}


def arabian2roman(to_convert):
    if to_convert in values:
        return values[to_convert]
    converted = ""
    for item in values.items():
        if item[0] < to_convert:
            converted += item[1]
            to_convert -= item[0]
            converted += arabian2roman(to_convert)
            break
        elif item[0] != 1 and item[0] - prefixes[item[0]] <= to_convert:
            converted += values[prefixes[item[0]]] + item[1]
            to_convert -= item[0] - prefixes[item[0]]
            if to_convert > 0:
                converted += arabian2roman(to_convert)
            break
    return converted


class Arabian2RomanUnitTests(unittest.TestCase):
    def test_1_converts_to_I(self):
        self.assertEquals("I", arabian2roman(1))

    def test_5_converts_to_V(self):
        self.assertEquals("V", arabian2roman(5))

    def test_2_converts_to_II(self):
        self.assertEquals("II", arabian2roman(2))

    def test_4_converts_to_IV(self):
        self.assertEquals("IV", arabian2roman(4))

    def test_1448_converts_to_MCDXLVIII(self):
        self.assertEquals("MCDXLVIII", arabian2roman(1448))
