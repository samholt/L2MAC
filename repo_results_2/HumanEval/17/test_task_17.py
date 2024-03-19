import pytest
from task_17 import parse_music

def test_parse_music():
	# Test case from the prompt
	music_string = 'o o| .| o| o| .| .| .| .| o o'
	expected_output = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
	assert parse_music(music_string) == expected_output

	# Additional test cases
	# Test case with only whole notes
	music_string = 'o o o'
	expected_output = [4, 4, 4]
	assert parse_music(music_string) == expected_output

	# Test case with only half notes
	music_string = 'o| o| o|'
	expected_output = [2, 2, 2]
	assert parse_music(music_string) == expected_output

	# Test case with only quarter notes
	music_string = '.| .| .|'
	expected_output = [1, 1, 1]
	assert parse_music(music_string) == expected_output

	# Test case with a mix of all note types
	music_string = 'o o| .| o| o .| o o| .|'
	expected_output = [4, 2, 1, 2, 4, 1, 4, 2, 1]
	assert parse_music(music_string) == expected_output
