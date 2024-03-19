def encrypt(s):
	"""Create a function encrypt that takes a string as an argument and
	returns a string encrypted with the alphabet being rotated. 
	The alphabet should be rotated in a manner such that the letters 
	shift down by two multiplied to two places.
	For example:
	encrypt('hi') returns 'lm'
	encrypt('asdfghjkl') returns 'ewhjklnop'
	encrypt('gf') returns 'kj'
	encrypt('et') returns 'ix'
	"""
	
	# Define the alphabet
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	
	# Initialize an empty string for the encrypted result
	encrypted = ''
	
	# Iterate over each character in the input string
	for c in s:
		# If the character is a lowercase letter
		if c in alphabet:
			# Find its index in the alphabet
			i = alphabet.index(c)
			
			# Calculate the new index by adding 4 and taking the modulus by 26
			j = (i + 4) % 26
			
			# Append the letter at the new index to the encrypted string
			encrypted += alphabet[j]
		else:
			# If the character is not a lowercase letter, append it as is
			encrypted += c
	
	# Return the encrypted string
	return encrypted
