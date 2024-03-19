import pytest
from task_158 import find_max

def test_find_max():
	assert find_max(["name", "of", "string"]) == "string"
	assert find_max(["name", "enam", "game"]) == "enam"
	assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
	assert find_max(["abc", "def", "ghi"]) == "abc"
	assert find_max(["jkl", "mno", "pqr"]) == "jkl"
	assert find_max([]) == None
	assert find_max(["singleword"]) == "singleword"
	assert find_max(["same", "mass", "moss"]) == "same"
	assert find_max(["same", "mass", "moss", "mass"]) == "same"
	assert find_max(['a'*1000000, 'b'*1000000]) == 'a'*1000000
