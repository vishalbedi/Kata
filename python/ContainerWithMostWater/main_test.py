from main import maxArea
import pytest

def test_two_inputs():
    assert maxArea([2,2]) == 2, "max area = 2x1=2"

def test_case_given():
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49, "max area = 2x1=2"
