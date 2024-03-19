def fibfib(n: int) -> int:
	"""The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
	fibfib(0) == 0
	fibfib(1) == 0
	fibfib(2) == 1
	fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
	Please write a function to efficiently compute the n-th element of the fibfib number sequence.
	>>> fibfib(1)
	0
	>>> fibfib(5)
	4
	>>> fibfib(8)
	24
	"""
	if n < 3:
		return [0, 0, 1][n]
	fibfib_sequence = [0, 0, 1]
	for i in range(3, n+1):
		fibfib_sequence.append(fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3])
	return fibfib_sequence[n]
