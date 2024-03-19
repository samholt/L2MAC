import pytest
from task_58 import common

def test_common_1():
	assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

def test_common_2():
	assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

def test_common_3():
	assert common([1, 2, 3], [4, 5, 6]) == []

def test_common_4():
	assert common([], []) == []

def test_common_5():
	assert common([1, 1, 1, 1], [1, 1, 1, 1]) == [1]

