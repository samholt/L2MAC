import pytest
from task_149 import sorted_list_sum

def test_sorted_list_sum():
	assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
	assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
	assert sorted_list_sum(["abc", "a", "abcd", "cd"]) == ["cd", "abcd"]
