import pytest
from task_143 import words_in_sentence

def test_words_in_sentence():
	assert words_in_sentence('This is a test') == 'is'
	assert words_in_sentence('lets go for swimming') == 'go for'
	assert words_in_sentence('I love to code in Python') == 'to in'
	assert words_in_sentence('ChatGPT is an AI model developed by OpenAI') == 'ChatGPT is an AI model by'
	assert words_in_sentence('') == ''
