# Author: Melanie Huynh
# Date: 5/6/2020
# Description: This program takes a list of Person objects and returns the standard deviation of all their ages.

class Person:
    """Represents a person with a name and age"""
    def __init__(self, name, age):
        """Creates the name and age of a Person object."""
        self._name = name
        self._age = age

    def get_age(self):
        """Returns the age of the Person object."""
        return self._age

def std_dev(people):
    """Returns the population standard deviation of the ages of a list of Person"""
    ages = [] # an empty list
    total = 0 # initial sum of ages
    for i in range(0, len(people)):
        ages = ages + [people[i].get_age()] # attain the ages of each Person
        total += people[i].get_age() # sum the ages of all People

    mean = total / len(people) # calculate the mean of the ages

    numerator_sum = 0 # intial numerator for the population standard deviation equation
    for age in ages:
      numerator_sum += (age - mean)**2 # numerator for the population standard deviation equation

    return (numerator_sum / len(people)) ** 0.5 # calculate population standard deviation

