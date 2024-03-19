import pytest
from task_144 import simplify

def test_simplify():
	assert simplify("1/5", "5/1") == True
	assert simplify("1/6", "2/1") == False
	assert simplify("7/10", "10/2") == False
	assert simplify("1/2", "2/1") == True
	assert simplify("3/4", "4/3") == True
	assert simplify("100/200", "200/100") == True
	assert simplify("999/1000", "1000/999") == True
	assert simplify("1/1000000", "1000000/1") == True
