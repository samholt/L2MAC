import pytest
from task_54 import same_chars

def test_same_chars():
	assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
	assert same_chars('abcd', 'dddddddabc') == True
	assert same_chars('dddddddabc', 'abcd') == True
	assert same_chars('eabcd', 'dddddddabc') == False
	assert same_chars('abcd', 'dddddddabce') == False
	assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False
	assert same_chars('abc', 'cba') == True
	assert same_chars('abc', 'def') == False
	assert same_chars('abc', 'abcd') == False
	assert same_chars('abc', 'abcabc') == True
