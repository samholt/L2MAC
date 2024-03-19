import pytest
from task_64 import vowels_count

def test_no_vowels():
	assert vowels_count('bcd') == 0

def test_all_vowels():
	assert vowels_count('aeiou') == 5

def test_y_at_end():
	assert vowels_count('sky') == 1

def test_y_not_at_end():
	assert vowels_count('yes') == 1

def test_uppercase_vowels():
	assert vowels_count('AEIOU') == 5

def test_lowercase_vowels():
	assert vowels_count('aeiou') == 5

def test_mixed_case():
	assert vowels_count('AeiOu') == 5

def test_y_at_end_uppercase():
	assert vowels_count('SKY') == 1

def test_y_not_at_end_uppercase():
	assert vowels_count('YES') == 1
