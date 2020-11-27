# Courtsey : https://www.geeksforgeeks.org/python-design-patterns/?ref=lbp

# Abstract Course

class Course:
	def __init__(self):
		self.Fee()
		self.available_batches()

	def Fee(self):
		raise NonImplementedError

	def available_batches(self):
		raise NonImplementedError

	def __repr__(self):
		return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)

# Concrete Course

class DSA(Course):
	def Fee(self):
		self.fee = 8000

	def available_batches(self):
		self.batches = 5

	def __str__(self):
		return 'DSA'

class SDE(Course):
	def Fee(self):
		self.fee = 10000

	def available_batches(self):
		self.batches = 4

	def __str__(self):
		return 'SDE'

class STL(Course):
	def Fee(self):
		self.fee = 5000

	def available_batches(self):
		self.batches = 7

	def __str__(self):
		return 'STL'

# Complex Course
class ComplexCourse:
	def __repr__(self):
		return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)

# Complex course
class Complexcourse(ComplexCourse):
	def Fee(self):
		self.fee = 7000

	def available_batches(self):
		self.batches = 6

# construct course -
def contruct_course(cls):
	course = cls()
	course.Fee()
	course.available_batches()

	return course   # return the course object

if __name__ == '__main__':
	dsa = DSA()
	sde = SDE()
	stl = STL()

	complex_course = contruct_course(Complexcourse)
	print(complex_course)