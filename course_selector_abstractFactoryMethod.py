# Courtsey : https://www.geeksforgeeks.org/python-design-patterns/?ref=lbp

import random

class DSA:
	""" Class for Data Structure and Algorithms """

	def price(self):
		return 11000

	def __str__(self):
		return "DSA"

class STL:
	""" Class for Standard Template Library """

	def price(self):
		return 8000

	def __str__(self):
		return "STL"

class SDE:
	""" Class for Software Development Engineer """

	def price(self):
		return 15000

	def __str__(self):
		return 'SDE'

def random_course():
	""" A random class for choosing the course """

	return random.choice([SDE, STL, DSA])()

class Course_At_GFG:
	""" GeeksforGeeks portal for courses """
	def __init__(self, courses_factory = None):
		""" course factory is our abstract factory """
		self.courses_factory = courses_factory()

	def show_course(self):
		""" creates and shows courses using the abstract factory """
		course = self.courses_factory

		print(f'We have a course named {course}')
		print(f'The price is {course.price()}')

if __name__ == '__main__':
	course = Course_At_GFG(random_course)

	for i in range(5):
		course.show_course()

