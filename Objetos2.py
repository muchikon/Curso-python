class Coche():
	def __init__(self): #creacion de constructor
		self.largoChasis=250
		self.anchoChasis=100
		self.__ruedas=4 # con esto ya no se puede modificar el valor de ruedas desde fuera (Encapsulamiento)
		self.enmarcha=False

	def arrancar(self,arrancamos):
		self.enmarcha=arrancamos
		if(self.enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta detenido"
	def estado(self):
		print("El coche tiene ",self.__ruedas," ruedas. Un ancho de: ",self.anchoChasis," y un largo de: ",self.largoChasis)
		
miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

miCoche2=Coche()
print(miCoche.arrancar(False))
miCoche2.__ruedas=2
miCoche2.estado()