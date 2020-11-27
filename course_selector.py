# Courtsey : https://www.geeksforgeeks.org/python-design-patterns/?ref=lbp

class DSA:
	""" Class for Data Structure and Algorithms """

	def price(self):
		return 11000

	def __str__(self):
		return "DSA"

class STL:
	""" Class for Standard template library """

	def price(self):
		return 8000

	def __str__(self):
		return "STL"

class SDE:
	""" Class for Software Development Engineer """

	def price(self):
		return 15000

	def __str__(self):
		return "SDE"

if __name__ == '__main__':
	sde = SDE() # object for SDE class
	dsa = DSA() # object for DSA class
	stl = STL() # object for STL class

	print(f'Name of the course is {sde} and its price is {sde.price()}')
	print(f'Name of the course is {dsa} and its price is {dsa.price()}')
	print(f'Name of the course is {stl} and its price is {stl.price()}')