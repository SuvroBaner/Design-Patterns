class FrenchLocalizer:
	""" it simply returns the french version """

	def __init__(self):
		self.translations = {'car': 'voiture', 'bike': 'bicyclette', 'cycle': 'cyclette'}

	def localize(self, message):
		""" change the message using translations """
		return self.translations.get(message, message)

class SpanishLocalizer:
	""" it simply returns the Spanish version """

	def __init__(self):
		self.translations = {'car': 'coche', 'bike': 'bicicleta', 'cycle': 'ciclo'}

	def localize(self, message):
		return self.translations.get(message, message)

class EnglishLocalizer:
	""" simply return the same (English) message """
	def localize(self, message):
		return message

if __name__ == "__main__":
	# main method to call others
	f = FrenchLocalizer()
	e = EnglishLocalizer()
	s = SpanishLocalizer()

	# list of strings -
	message = ['car', 'bike', 'cycle', 'scooter']

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))
		print('\n')