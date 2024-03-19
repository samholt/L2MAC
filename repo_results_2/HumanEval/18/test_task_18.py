import pytest
from task_18 import how_many_times


def test_how_many_times():
	assert how_many_times('', 'a') == 0
	assert how_many_times('aaa', 'a') == 3
	assert how_many_times('aaaa', 'aa') == 3
	assert how_many_times('abcabcabc', 'abc') == 3
	assert how_many_times('abcabcabc', 'abcd') == 0
	assert how_many_times('abcabcabc', 'ab') == 3
	assert how_many_times('abcabcabc', 'bc') == 3
	assert how_many_times('abcabcabc', 'ca') == 2
	assert how_many_times('abcabcabc', 'abcabcabc') == 1
	assert how_many_times('abcabcabc', 'abcabcabcd') == 0
	assert how_many_times('abcabcabc', 'abcabcabca') == 0
	assert how_many_times('abcabcabc', 'abcabcab') == 1
	assert how_many_times('abcabcabc', 'abcabc') == 2
	assert how_many_times('abcabcabc', 'abcab') == 2
	assert how_many_times('abcabcabc', 'abca') == 2
	assert how_many_times('abcabcabc', 'abc') == 3
	assert how_many_times('abcabcabc', 'ab') == 3
	assert how_many_times('abcabcabc', 'a') == 3
	assert how_many_times('abcabcabc', '') == 9
	assert how_many_times('', '') == 0
