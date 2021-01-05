# Author: Melanie Huynh
# Date: 4/15/2020
# Description: This program asks the user to enter an integer greater than or equal to 1 and then prints a list of all positive integers that divide that number evenly, including itself and 1, in ascending order.

# Begin by prompting the user to input an integer greater than or equal to 1.
print("Please enter a positive integer:")
num_int = int(input())

# Then display the factors of the user's input.
print("The factors of", num_int, "are:")

# This for-loop checks to see from a range of 1 to the user's input (including itself) if the number is divisible without any remainders. If it has no remainders, the number is a factor of the input.
for each_int in range(1, num_int + 1):
	if num_int % each_int == 0:
		print(each_int)

