import pytest
from task_128 import prod_signs

def test_positive_numbers():
    """Test case where all numbers in the array are positive."""
    assert prod_signs([1, 2, 3, 4]) == 10

def test_negative_numbers():
    """Test case where all numbers in the array are negative."""
    assert prod_signs([-1, -2, -3, -4]) == 10

def test_zeros():
    """Test case where the array contains zeros."""
    assert prod_signs([0, 1, 2, 3]) == 6

def test_empty_array():
    """Test case where the array is empty."""
    assert prod_signs([]) == None

def test_mixed_numbers():
    """Test case where the array contains a mix of positive, negative numbers and zeros."""
    assert prod_signs([1, -2, 0, 3]) == -6
