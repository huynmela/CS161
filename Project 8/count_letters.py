# Author: Melanie Huynh
# Date: 5/20/2020
# Description: This program takes a string and returns a dictionary that tabulates how many of each letter is in that string.

def count_letters(word):
    """Returns a dictionary with the number of letters in the input string. """
    dictionary = {} # empty dictionary
    alphabet = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    for letter in word.upper(): # ensures all lowercase is uppercased
        if letter in alphabet:
            if letter in dictionary: # checks to see if the letter in already in the dictionary
                dictionary[letter] += 1 # counts the letter
            else:
                dictionary[letter] = 1 # creates a new index in the dictionary
    return dictionary

#word = "Quis custodiet ipsos custodes?"
#test = count_letters(word)
#print(test)
