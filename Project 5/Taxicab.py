# Author: Melanie Huynh
# Date: 4/29/2020
# Description: This program moves an object Taxicab along an x and or y axis, while keeping track of the distance driven by the Taxicab.

class Taxicab:
	"""Represents a taxicab with methods to move it along an x and y coordinate and track the distance it has travelled."""
	def __init__(self, x, y):
		"""Creates the directions the Taxicab object can travel with x and y and initializes the Taxicab object's odometer as zero."""
		self._x = x
		self._y = y
		self._odometer = 0

	def move_x(self, new_x):
		"""Moves the Taxicab object left or right while adding distance to the odometer"""
		self._x += new_x # moves the object left or right of the initial x-position
		self._odometer += abs(new_x) # adds distance to the odometer
		return
	def move_y(self, new_y):
		"""Moves the Taxicab object up or down while adding distance to the odometer"""
		self._y += new_y # moves the object up or down of the initial y-position
		self._odometer += abs(new_y) # adds distance to the odometer
		return

	def get_x_coord(self):
		"""Returns the x-coordinate position the Taxicab object is."""
		return self._x
	def get_y_coord(self):
		"""Returns the y-coordinate position the Taxicab object is."""
		return self._y
	def get_odometer(self):
		"""Returns the overall distance the Taxicab object has travelled."""
		return self._odometer

