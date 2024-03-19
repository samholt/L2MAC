def solve(N):
	"""Given a positive integer N, return the total sum of its digits in binary.
	
	Example
		For N = 1000, the sum of digits will be 1 the output should be "1".
		For N = 150, the sum of digits will be 6 the output should be "110".
		For N = 147, the sum of digits will be 12 the output should be "1100".
	
	Variables:
		@N integer
			 Constraints: 0 ≤ N ≤ 10000.
	Output:
		 a string of binary number
	"""
	if not 0 <= N <= 10000:
		raise ValueError('Input out of bounds')
	
	sum_of_digits = sum(int(digit) for digit in str(N))
	return bin(sum_of_digits)[2:]

def test_solve():
	assert solve(1000) == '1'
	assert solve(150) == '110'
	assert solve(147) == '1100'
	assert solve(0) == '0'
	assert solve(10000) == '1'
