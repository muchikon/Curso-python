class Vehiculos():
	def __init__(self,marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
	def arrancar(self):
		self.enmarcha=True
	def acelerar(self):
		self.acelera=True
	def frenar(self):
		self.frena=True
	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\En marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrena: ",self.frena)
class Moto(Vehiculos): #hereda de vehiculos
	pass # para no construir nada dentro de Moto

miMoto=Moto("Honda","CBR")
miMoto.estado()	