# Author: Melanie Huynh
# Date: 4/15/2020
# Description: This program prompts the user for an integer which a second person (or the user) will try to guess. If the player's guess is higher than the target number, the program displays "too high". If the guess is lower than the target number, the program displays "too low". If the user guesses the number, the program will display how many guesses it took.

# Variable Section
answer = 0
guess = 0
times_tried = 0

# Prompt the first player to input an integer.
print("Enter the number for the player to guess.")
answer = int(input())

# Prompt the second player to input a guess.
print("Enter your guess.")
times_tried = 1
guess = int(input())

# If the guess is correct on the first try, a special case message is given.
if guess == answer:
	print("You guessed it in 1 try.")

# If the guess is incorrect, the attempt is counted and the guess is checked against the answer to see if it is higher or lower. Once the guess matches the answer, the player is prompted on their success and how many attempts it required to succeed.
if guess != answer:
	while guess != answer:
		times_tried += 1
		if guess > answer:
			print("Too high - try again:")
		if guess < answer:
			print("Too low - try again:")
		guess = int(input())
	print("You guessed it in", times_tried, "tries.") 		 
