# Author: Melanie Huynh
# Date: 5/13/2020
# Description: This program takes a list of numbers and replaces each value with
# the square of that value by mutating the original list using slicing.

def square_list(num_list):
    """Returns the squared value of each number in a list """
    for times in range(0, len(num_list)): # specifies number of times needed to run
        cut = num_list[:-1] # removes the last element in the list
        squared = [num_list[len(num_list)-1] ** 2] # squares the last element in the list
        num_list[:] = squared + cut # combines the lists together where the squared value is at the front)
