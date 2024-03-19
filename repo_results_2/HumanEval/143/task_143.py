def is_prime(n):
	"""
	Helper function to check if a number is prime.
	"""
	if n < 2:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True


def words_in_sentence(sentence):
	"""
	You are given a string representing a sentence,
	the sentence contains some words separated by a space,
	and you have to return a string that contains the words from the original sentence,
	whose lengths are prime numbers,
	the order of the words in the new string should be the same as the original one.

	Example 1:
		Input: sentence = "This is a test"
		Output: "is"

	Example 2:
		Input: sentence = "lets go for swimming"
		Output: "go for"

	Constraints:
		* 1 <= len(sentence) <= 100
		* sentence contains only letters
	"""
	# Split the sentence into words
	words = sentence.split()

	# Filter out the words whose length is not a prime number
	prime_words = [word for word in words if is_prime(len(word))]

	# Join the prime_words list back into a string
	result = ' '.join(prime_words)

	return result
