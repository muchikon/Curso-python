class Coche():
	largoChasis=250
	anchoChasis=100
	ruedas=4
	enmarcha=False

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