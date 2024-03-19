def select_words(s, n):
	"""Given a string s and a natural number n, this function returns a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
	If the string s is empty then the function should return an empty list.
	Note: you may assume the input string contains only letters and spaces.
	"""
	if not s:
		return []
	
	words = s.split()
	result = []
	
	for word in words:
		consonants = sum(1 for char in word if char.lower() not in 'aeiou')
		if consonants == n:
			result.append(word)
	
	return result
