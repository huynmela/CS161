# Author: Melanie Huynh
# Date: 4/15/2020
# Description: This program asks the user how many integers they would like to enter, assuming the initial input is greater than or equal to 1. The program then asks the user to input that many integers, and outputs the largest and smallest of those numbers.

# Begin by prompting the user how many integers they would like to enter.
print("How many integers would you like to enter?:")
num_int = int(input())

# Prompt the user to input that number of integers.
print("Please enter", num_int, "integers")

# As a baseline, we must ensure if the user were to input 1 for variable num_int, the program will not enter the for loop.
minimum = int(input())
maximum = minimum

# If variable num_int is greater than 1, we enter the for loop to redefine the minimum and maximum integers from the given list. 
for each_num in range(1, num_int):
	num = int(input())
	if num <= minimum:
		minimum = num
	if num >= maximum:
		maximum = num

print("min:", minimum)
print("max:", maximum)
