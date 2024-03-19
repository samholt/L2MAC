def get_max_triples(n):
	"""
	You are given a positive integer n. You have to create an integer array a of length n.
	For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
	Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
	and a[i] + a[j] + a[k] is a multiple of 3.

	Example :
		Input: n = 5
		Output: 1
		Explanation: 
		a = [1, 3, 7, 13, 21]
		The only valid triple is (1, 7, 13).
	"""
	# Initialize an empty list a
	a = []
	# Generate the list a
	for i in range(1, n + 1):
		a.append(i * i - i + 1)
	# Initialize a variable to keep track of the number of triples
	count = 0
	# Iterate over all possible triples in the list a
	for i in range(n):
		for j in range(i + 1, n):
			for k in range(j + 1, n):
				# Check if the sum of the current triple is a multiple of 3
				if (a[i] + a[j] + a[k]) % 3 == 0:
					# If it is, increment the count variable
					count += 1
	# Return the count variable
	return count
