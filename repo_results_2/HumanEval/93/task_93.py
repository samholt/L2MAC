def encode(message):
	"""
	Write a function that takes a message, and encodes in such a 
	way that it swaps case of all letters, replaces all vowels in 
	the message with the letter that appears 2 places ahead of that 
	vowel in the english alphabet. 
	Assume only letters. 
	
	Examples:
	>>> encode('test')
	'TGST'
	>>> encode('This is a message')
	'tHKS KS C MGSSCGG'
	"""

	# define mapping for vowels to the letter 2 places ahead
	vowel_mapping = {
		'a': 'c', 'A': 'C',
		'e': 'g', 'E': 'G',
		'i': 'k', 'I': 'K',
		'o': 'q', 'O': 'Q',
		'u': 'w', 'U': 'W',
		'y': 'a', 'Y': 'A'
	}

	encoded_message = ''
	for char in message:
		# replace vowel with the letter 2 places ahead
		if char in vowel_mapping:
			char = vowel_mapping[char]
		
		# swap case of char
		char = char.swapcase()
		
		encoded_message += char
	
	return encoded_message
