def is_palindrome(text: str) -> bool:
	"""
	Checks if given string is a palindrome
	
	>>> is_palindrome('')
	True
	>>> is_palindrome('aba')
	True
	>>> is_palindrome('aaaaa')
	True
	>>> is_palindrome('zbcd')
	False
	"""
	text = ''.join(ch for ch in text if ch.isalnum()).lower()
	return text == text[::-1]
