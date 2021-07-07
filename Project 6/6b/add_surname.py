# Author: Melanie Huynh
# Date: 5/6/2020
# Description: This programs takes a list of first names, returns only a list of names that start with a "K", and appends the last name "Kardashian"

def add_surname(names):
	"""Returns a list of first names starting with "K" and surname "Kardashian"."""
	return [name + " Kardashian" for name in names if name[0] == "K"] # Finds first names starting with "K" and appends "Kardashian, returning the "K" name list.
