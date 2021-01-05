# Author: Melanie Huynh
# Date: 5/20/2020
# Description: This program takes in two strings and returns a set of the words contained in both strings.

def words_in_both(first_word, second_word):
    """Returns common words found in two strings"""
    common_words = set() # Empty set to mutate
    first_word_list = first_word.split() # Split both string inputs
    second_word_list = second_word.split()

    lower_first_list = [x.lower() for x in first_word_list] # Ensures both are lowercase
    lower_second_list = [x.lower() for x in second_word_list]

    for word in lower_first_list: # iterates through every word in the first list
        if word in lower_second_list: # checks if word is same in second list
            common_words.add(word) # add common word to the empty set
    return common_words

# first_string = "Shes the jack of all trades"
# second_string = "Jack was tallest of all"
# common_words = words_in_both(first_string, second_string)
# print(common_words)
