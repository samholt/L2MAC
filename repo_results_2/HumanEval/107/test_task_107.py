import pytest
from task_107 import even_odd_palindrome

def test_even_odd_palindrome():
	assert even_odd_palindrome(3) == (1, 2)
	assert even_odd_palindrome(12) == (4, 6)
	assert even_odd_palindrome(1) == (0, 1)
	assert even_odd_palindrome(22) == (5, 6)
