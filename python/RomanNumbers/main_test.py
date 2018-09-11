from main import intToRoman
import pytest

def test_single_digit():
    assert intToRoman(1) == "I", "One converted to roman I"

def test_two():
    assert intToRoman(2) == "II", "Two converted to II"

def test_three():
    assert intToRoman(3) == "III", "3 to III"

def test_eight():
    assert intToRoman(8) == "VIII", "8 to VIII"

def test_eighteen():
    assert intToRoman(18) == "XVIII", "18 to XVIII"

def test_nine():
    assert intToRoman(9) == "IX" , "9 is IX"

def test_long_nine_based_number():
    assert intToRoman(1994) == "MCMXCIV" , "test passed"
