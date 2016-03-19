import unittest
from collections import OrderedDict
from functools import reduce

orderedValues = OrderedDict([("IV", 4), ("IX", 9), ("XL", 40), ("XC", 90), ("CD", 400), ("CM", 900), ("I", 1), ("V", 5),
                             ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])


def roman2arabianv2(toconvert):
    if toconvert in orderedValues.keys(): return orderedValues[toconvert]
    else:
         for x in orderedValues.keys():
                if x in toconvert: return orderedValues[x] + roman2arabianv2(toconvert.replace(x, "", 1))

        

class Roman2ArabianV2Tests(unittest.TestCase):
    def test_I_should_return_1(self):
        return self.assertEquals(1, roman2arabianv2("I"))

    def test_V_should_return_5(self):
        return self.assertEquals(5, roman2arabianv2("V"))

    def test_IV_should_return_4(self):
        return self.assertEquals(4, roman2arabianv2("IV"))

    def test_II_should_return_2(self):
        return self.assertEquals(2, roman2arabianv2("II"))

    def test_MCDXLVIII_should_return_1448(self):
        return self.assertEquals(1448, roman2arabianv2("MCDXLVIII"))