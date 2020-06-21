class Coche():
	def __init__(self): #creacion de constructor
		self.largoChasis=250
		self.anchoChasis=100
		self.ruedas=4
		self.enmarcha=False

	def arrancar(self):
		self.enmarcha=True
	def estado(self):
		if(self.enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta detenido"
miCoche = Coche()
print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene: ",miCoche.ruedas," ruedas")
miCoche.arrancar()
print(miCoche.estado())

miCoche2=Coche()
print("El largo del coche2 es: ",miCoche.largoChasis)
print("El coche2 tiene: ",miCoche.ruedas," ruedas")
print(miCoche2.estado())