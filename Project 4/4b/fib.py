# Author: Melanie Huynh
# Date: 4/22/2020
# Description: This program takes a positive integer and returns the number at that position of the fibonacci sequence.

def fib(n):
	"""Returns the number at the n position of the Fibonacci sequence."""
	# Defines the first two integers of the special cases in the Fibonacci sequence
	n_1 = 0 
	n_2 = 1
	# These first two if statements take care of the special cases where a for loop is not needed to "build" the Fibonacci sequence for n greater than 1. Otherwise, when n is greater than 1, we utilize the for loop.
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n > 1: # When n is greater than 1, we must incrementally increase the base first two integers, summing the previous integers until reaching the desired position.
		for i in range(0, n - 1):
			sum_previous = n_1 + n_2
			n_1 = n_2
			n_2 = sum_previous
		return sum_previous
