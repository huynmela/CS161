# Author: Melanie Huynh 2
# Date: 5/13/2020
# Description: This program takes a list and reverses the order of the elements
# in that list.

def reverse_list(vals):
    """Returns the reversed order of a list"""
    for i in range(0, len(vals) - 2): # iterates from left to right
        j = len(vals) - i - 1 # iterates from right to left
        temp = vals[i] # stores the current i index value
        vals[i] = vals[j] # swaps indexes i and j
        vals[j] = temp # swaps stored value i and j
        if i > j: # when the indexes pass each other, break the loop to stop swap
            break
