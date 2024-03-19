def even_odd_palindrome(n):
	"""
	Given a positive integer n, return a tuple that has the number of even and odd
	integer palindromes that fall within the range(1, n), inclusive.

	Example 1:

		Input: 3
		Output: (1, 2)
		Explanation:
		Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

	Example 2:

		Input: 12
		Output: (4, 6)
		Explanation:
		Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

	Note:
		1. 1 <= n <= 10^3
		2. returned tuple has the number of even and odd integer palindromes respectively.
	"""
	# Initialize counters for even and odd palindromes
	even_count = 0
	odd_count = 0

	# Iterate over the range from 1 to n inclusive
	for i in range(1, n + 1):
		# Check if the number is a palindrome
		if str(i) == str(i)[::-1]:
			# If the number is a palindrome, check if it is even or odd
			if i % 2 == 0:
				even_count += 1
			else:
				odd_count += 1

	# Return a tuple containing the counts of even and odd palindromes
	return (even_count, odd_count)
