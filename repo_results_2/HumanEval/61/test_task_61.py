import pytest
from task_61 import correct_bracketing

def test_correct_bracketing():
	assert correct_bracketing('(') == False
	assert correct_bracketing('()') == True
	assert correct_bracketing('(()())') == True
	assert correct_bracketing(')(()') == False
