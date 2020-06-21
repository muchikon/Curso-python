class Coche():
	def desplazamiento(self):
		print("4 ruedas")
class Moto():
	def desplazamiento(self):
		print("2 ruedas")
class Camion():
	def desplazamiento(self):
		print("6 ruedas")
def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()
miVehiculo=Coche()
desplazamientoVehiculo(miVehiculo)