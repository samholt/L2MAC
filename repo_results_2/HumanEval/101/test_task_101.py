import pytest
from task_101 import words_string

def test_words_string():
	assert words_string('Hi, my name is John') == ['Hi', 'my', 'name', 'is', 'John']
	assert words_string('One, two, three, four, five, six') == ['One', 'two', 'three', 'four', 'five', 'six']
	assert words_string('Hello, world') == ['Hello', 'world']
	assert words_string('Hello , world') == ['Hello', 'world']
	assert words_string('Hello  world') == ['Hello', 'world']
	assert words_string(' ,Hello, ,world, ') == ['Hello', 'world']
	assert words_string('  Hello  world  ') == ['Hello', 'world']
	assert words_string('') == []
	assert words_string(' ') == []
	assert words_string(',') == []
