# Courtsey : https://www.geeksforgeeks.org/python-design-patterns/?ref=lbp

#############   Monostate/Borg Singleton Design pattern ################

""" The Singleton pattern is a design pattern that restricts the instantiation of a class to one object
Singleton behavior can be implemented by Borg's pattern but instead of having only one instance of the class there are multiple instances that share the same state. """

class Borg:

	# state shared by each instance (Basically it contains all the attributes which describe the object in question. It can be used to alter or read the attributes.)
	__shared_state = dict()

	# constructor method
	def __init__(self):
		self.__dict__ = self.__shared_state
		self.state = 'GeeksforGeeks'

	def __str__(self):
		return self.state

if __name__ == '__main__':
	person1 = Borg() # object of class Borg
	person2 = Borg() # object of class Borg
	person3 = Borg() # Object of class Borg

	print(person1.__dict__)  # answer : {'state': 'GeeksforGeeks'}

	print(person1) # answer -- > GeeksforGeeks

	person1.state = 'DataStructures' # person1 changed the state
	person2.state = 'Algorithms' # person2 changed the state

	print(person1) # answer -- > Algorithms
	print(person2) # answer --- > Algorithms

	person3.state = 'Geeks' # person3 changed the shared state

	print(person1) # answer --- > Geeks
	print(person2) # answer --- > Geeks
	print(person3) # answer --- > Geeks

	print(person1.__dict__) # {'state': 'Geeks'}

