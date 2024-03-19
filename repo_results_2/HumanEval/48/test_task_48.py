import pytest
from task_48 import is_palindrome

def test_is_palindrome():
	assert is_palindrome('') == True
	assert is_palindrome('aba') == True
	assert is_palindrome('aaaaa') == True
	assert is_palindrome('zbcd') == False
	assert is_palindrome('A man, a plan, a canal: Panama') == True
	assert is_palindrome('race a car') == False
