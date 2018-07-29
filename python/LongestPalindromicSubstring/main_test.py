from main import longetst_Palindrome
from main import palendrome_length
import pytest

def test_empty_input():
    assert longetst_Palindrome("") == "", "Value should be empty string"

def test_single_length_input():
    assert longetst_Palindrome("a") == "a", "should return the input string"

def test_two_char_input():
    assert longetst_Palindrome("ab") == "a" or longest_substring("ab") == "b", \
        "should retunrn one of the two characters from the input"

def test_two_length_palendrom_input():
    assert longetst_Palindrome("aa") == "aa", "Should return the complete palendrome"

def test_check_palendrome():
    assert palendrome_length("nitin", 2,2) == 5, "Should return 5"

def test_palindrome_fail():
    assert palendrome_length("vishal", 2,2) == 1, "should return 1"
