def vowels_count(s):
	"""
	This function takes a string representing a word as input and returns the number of vowels in the string.
	Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.
	"""
	vowels = ['a', 'e', 'i', 'o', 'u']
	s = s.lower()
	count = 0
	for i in range(len(s)):
		if s[i] in vowels:
			count += 1
		if s[i] == 'y' and i == len(s) - 1:
			count += 1
	return count

def test_vowels_count():
	assert vowels_count('abcde') == 2
	assert vowels_count('ACEDY') == 3
	assert vowels_count('y') == 1
	assert vowels_count('Y') == 1
	assert vowels_count('abc') == 1
	assert vowels_count('') == 0
