# Courtsey : https://www.geeksforgeeks.org/python-design-patterns/?ref=lbp

""" In the Classic implementation of the Singleton Design Pattern, 
	1. we simply use the staticmethod for creating the getInstance method which has the ability to return the shared resource.
	2. We also make use of so called Virtual private constructor to raise the exception against it. """

class Singleton:

	__shared_instance = 'GeeksforGeeks'

	@staticmethod
	def getInstance():

		""" Static Access Method """
		if Singleton.__shared_instance == 'GeeksforGeeks':
			Singleton()
		return Singleton.__shared_instance

	def __init__(self):

		""" virtual private constructor """
		if Singleton.__shared_instance != 'GeeksforGeeks':
			raise Exception ("This class is a Singleton class !")
		else:
			Singleton.__shared_instance = self

if __name__ == '__main__':
	# create object of the singleton class
	obj = Singleton()
	print(obj)

	# pick the instance of the class 
	obj = Singleton.getInstance()
	print(obj)

""" Singleton patterns are generally used in providing the logging, caching, thread pools 
and configuration settings and oftenly used in conjuction with Factory design pattern. """

