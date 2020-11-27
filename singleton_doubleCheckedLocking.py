# Courtsey : https://www.geeksforgeeks.org/python-design-patterns/?ref=lbp

####### Double Checked Locking Singleton Design Pattern #############

""" It is easy to notice that once an object is created, the synchronization of the threading is no longer useful because now the object will be equal to None
adn any sequence of operations will lead to consistent results. 
So, when the object will be equal to None, then only we will acquire the Lock on the genInstance method. """

import threading

class SingletonDoubleChecked(object):

	# resources shared by each and every instance

	__singleton_lock = threading.Lock()
	__singleton_instance = None

	# define the classmethod -
	@classmethod
	def instance(cls):

		# check for the singleton instance 
		if not cls.__singleton_instance:
			with cls.__singleton_lock:
				if not cls.__singleton_instance:
					cls.__singleton_instance = cls()

		return cls.__singleton_instance

if __name__ == '__main__':

	# create class X
	class X(SingletonDoubleChecked):
		pass

	# create class Y
	class Y(SingletonDoubleChecked):
		pass

	A1, A2 = X.instance(), X.instance()
	B1, B2 = Y.instance(), Y.instance()

	assert A1 is not B1
	assert A1 is A2
	assert B1 is B2

	print('A1 :  ', A1)
	print('A2 :  ', A2)
	print('B1 :  ', B1)
	print('B2 :  ', B2)