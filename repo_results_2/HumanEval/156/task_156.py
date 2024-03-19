def int_to_mini_roman(number):
	"""
	Given a positive integer, obtain its roman numeral equivalent as a string,
	and return it in lowercase.
	Restrictions: 1 <= num <= 1000

	Examples:
	>>> int_to_mini_roman(19) == 'xix'
	>>> int_to_mini_roman(152) == 'clii'
	>>> int_to_mini_roman(426) == 'cdxxvi'
	"""

	# Check if the number is within the valid range
	if not 1 <= number <= 1000:
		raise ValueError('Input number must be between 1 and 1000')

	# Mapping of integer to roman numerals
	int_to_roman = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}

	roman_numeral = ''

	# List of keys in descending order
	keys = sorted(int_to_roman.keys(), reverse=True)

	for key in keys:
		while number >= key:
			number -= key
			roman_numeral += int_to_roman[key]

	return roman_numeral
