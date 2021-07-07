# Author: Melanie Huynh
# Date: 4/22/2020
# Description: This program calculates the distance in meters that an object has fallen based off an input amount of time in seconds. 

g = 9.8 # acceleration of gravity in m/s^2

def fall_distance(t):
	"""Returns the distance an object falls with the given time."""
	return (1 / 2) * g * t ** 2 # Mathematical equation for distance an object in free fall travels in m

