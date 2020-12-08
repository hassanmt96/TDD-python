import unittest
from app.roman_numerals import parse


class TestRomanNumerals(unittest.TestCase):
    def test_i(self):
        value = parse("I")
        self.assertEqual(value, 1)

    def test_ii(self):
        value = parse('II')
        self.assertEqual(value, 2)

    def test_iii(self):
        value = parse('III')
        self.assertEqual(value, 3)

    def test_iv(self):
        value = parse('IV')
        self.assertEqual(value, 4)

    def test_v(self):
        value = parse('V')
        self.assertEqual(value, 5)

    def test_vi(self):
        value = parse('VI')
        self.assertEqual(value, 6)

    def test_vii(self):
        value = parse('VII')
        self.assertEqual(value, 7)

    def test_viii(self):
        value = parse('VIII')
        self.assertEqual(value, 8)


# USING PYTEST
def test_xi():
    value = parse('XI')
    assert value == 11


def test_xiv():
    value = parse('XIV')
    assert value == 14


def test_xix():
    value = parse('XIX')
    assert value == 19


def test_xx():
    value = parse('XX')
    assert value == 20


def test_xxxiv():
    value = parse('XXXIV')
    assert value == 34


def test_xli():
    value = parse('XLI')
    assert value == 41


def test_l():
    value = parse('L')
    assert value == 50


def test_xxix():
    value = parse('XCIX')
    assert value == 99


def test_c():
    value = parse('C')
    assert value == 100


def test_cccxxxiii():
    value = parse('CCCXXXIII')
    assert value == 333


def test_dlv():
    value = parse('DLV')
    assert value == 555


def test_cdxlix():
    value = parse('CDXLIX')
    assert value == 449


def test_mcmlxxii():
    value = parse('MCMLXXII')
    assert value == 1972
