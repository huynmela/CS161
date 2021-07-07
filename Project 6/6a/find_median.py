# Author: Melanie Huynh
# Date: 5/6/2020
# Description: This program takes a list of numbers and returns the median of those numbers. 

def find_median(list):
	"""Returns the median of a list of numbers"""
	list.sort() # Sorts the lists from low to high
	length = len(list) # Gets length of the list
	
	if length % 2 != 0: # Checks if the total list is odd to apply correct mathematical equation
		return list[length//2]
	else: # Otherwise, even lists get applied correct mathematical equation
		num1 = list[length//2]
		num2 = list[length//2 -1]
		return (num1 + num2) / 2

	
