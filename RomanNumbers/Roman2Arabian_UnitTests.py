import unittest


values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman2arabian(to_convert):
    result = 0
    if len(to_convert) > 1:
        if values[to_convert[0]] < values[to_convert[1]]:
            result -= values[to_convert[0]]
        else:
            result += values[to_convert[0]]
        return result + roman2arabian(to_convert[1:])
    else:
        return values[to_convert[0]]


class Roman2Arabian(unittest.TestCase):
    def test_I_converts_to_1(self):
        self.assertEquals(roman2arabian("I"), 1)

    def test_V_converts_to_5(self):
        self.assertEquals(roman2arabian("V"), 5)

    def test_II_converts_to_2(self):
        self.assertEquals(roman2arabian("II"), 2)

    def test_IV_converts_to_4(self):
        self.assertEquals(roman2arabian("IV"), 4)

    def test_MCDXLVIII_converts_to_1448(self):
        self.assertEquals(roman2arabian("MCDXLVIII"), 1448)
