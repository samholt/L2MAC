def is_bored(S):
	"""
	You'll be given a string of words, and your task is to count the number
	of boredoms. A boredom is a sentence that starts with the word "I".
	Sentences are delimited by '.', '?' or '!'.
	
	For example:
	>>> is_bored("Hello world")
	0
	>>> is_bored("The sky is blue. The sun is shining. I love this weather")
	1
	"""
	
	# Replace all sentence delimiters with a unique delimiter and split the string into sentences
	S = S.replace('.', '|').replace('?', '|').replace('!', '|')
	sentences = S.split('|')
	
	# Initialize a counter for the number of boredoms
	boredom_count = 0
	
	# Iterate over the list of sentences
	for sentence in sentences:
		# Strip leading and trailing whitespace
		sentence = sentence.strip()
		
		# Check if the sentence starts with the word 'I'
		if sentence.startswith('I'):
			# If it does, increment the boredom count
			boredom_count += 1
	
	# Return the boredom count
	return boredom_count
