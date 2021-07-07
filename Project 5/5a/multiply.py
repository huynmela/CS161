# Author: Melanie Huynh
# Date: 4/29/2020
# Description: This program takes two positive integers and returns the product of those two numbers using only addition.

def multiply(num1, num2): 
	"""Returns the product of two positive integers using only addition."""
	if num2 == 0: # This acts as a base case which will force recursion to exit.
		return 0
	if num2 > 0: # As long as either number is not 1, the recursion will continue to add to the call stack.
		return num1 + multiply(num1, num2 - 1)

