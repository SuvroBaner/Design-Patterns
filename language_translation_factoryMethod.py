class FrenchLocalizer:
	""" It simply returns the French version """
	def __init__(self):
		self.translations = {"car": "voiture", "bike": "bicyclette", "cycle": "cyclette"}

	def localize(self, message):
		""" change the message using translations """
		return self.translations.get(message, message)

class SpanishLocalizer:
	""" it simply returns the Spanish version """
	def __init__(self):
		self.translations = {'car': "coche", "bike": "bicicleta", "cycle": "ciclo"}

	def localize(self, message):
		""" change the message using translations """
		return self.translations.get(message, message)

class EnglishLocalizer:
	""" simply return the same message """
	def localize(self, message):
		return message

class HindiLocaliser:
	def __init__(self):
		self.translations = {'car': 'gari', 'bike': 'bambookat', 'cycle': 'dopaiya'}

	def localize(self, message):
		return self.translations.get(message, message)

def Factory(language = 'English'):
	""" Factory Method """
	localizers = {
	"French": FrenchLocalizer,
	"English": EnglishLocalizer,
	"Spanish": SpanishLocalizer,
	'Hindi': HindiLocaliser
	}

	return localizers[language]()

if __name__ == '__main__':
	f = Factory("French")
	e = Factory("English")
	s = Factory("Spanish")
	h = Factory('Hindi')

	message = ["car", "bike", "cycle", 'scooter']

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))
		print(h.localize(msg))
		print('\n')
