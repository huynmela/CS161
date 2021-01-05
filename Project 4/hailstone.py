# Author: Melanie Huynh
# Date: 4/22/2020
# Description: This program takes a positive integer as the initial number of a hailstone sequence and returns how many steps it takes to reach 1. 

def hailstone(num):
	"""Returns the number of steps required for a positive integer to reach 1 in a hailstone sequence."""
	steps = 0 # Number of steps required to reach 1 in hailstone sequence.
	if num == 1: # Defines the base line special case where 1 requires 0 steps
		return steps
	while num != 1: # If num is not 1, require a while loop until 1 is reached
		if num % 2 == 0: # Check if num is even
			num = num / 2 # If even, apply the correct mathematical process
			steps += 1 # Add a step
		else: # if num is odd
			num = num * 3 + 1 #apply the correct mathematical process
			steps += 1 # Add a step
	return steps # Give steps required in while loop to reach 1

