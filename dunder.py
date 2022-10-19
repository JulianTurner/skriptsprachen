# Klasse welche die dunder Methode enthält
class Datenhalter:
	def __init__(self, wert):
		self.wert = wert

	def __toJSON__(self):
		jsonstring = '{"wert":' + str(self.wert) + '}'
		return jsonstring

# Klasse die Aufgerufen wird
class Encoder:
	def __init__(self):
		pass

	def encode(self, obj: Datenhalter): 
		return obj.__toJSON__()
	
# Main Methode
if __name__ == '__main__':
	# Serialisierer erstellen
	encoder = Encoder()
	# Datenhalter erstellen
	datenhalter = Datenhalter(42)
	# Datenhalter serialisieren
	print(encoder.encode(datenhalter))

