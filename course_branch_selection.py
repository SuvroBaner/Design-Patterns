# Courtsey : https://www.geeksforgeeks.org/python-design-patterns/?ref=lbp

class DSA:
	""" class for data structures and algorithms """
	def Fee(self):
		self.fee = 8000
		return self.fee

	def available_batches(self):
		self.batches = 5

	def __str__(self):
		return "DSA"

class SDE:
	""" classes for Software Development Engineer """
	def Fee(self):
		self.fee = 10000
		return self.fee

	def available_batches(self):
		self.batches = 4

	def __str__(self):
		return 'SDE'

class STL:
	""" class for standard template library of C++ """
	def Fee(self):
		self.fee = 5000
		return self.fee

	def available_batches(self):
		self.batches = 7

	def __str__(self):
		return "STL"

if __name__ == '__main__':
	sde = SDE()
	dsa = DSA()
	stl = STL()

	print(f'Name of Course: {sde} and its Fee: {sde.Fee()}')
	print(f'Name of Course: {stl} and its Fee: {stl.Fee()}')
	print(f'Name of Course: {dsa} and its Fee: {dsa.Fee()}')