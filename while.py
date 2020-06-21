import math
print("Raiz Cuadrada")
numero=int(input("Ingrese Numero: "))
intentos=0
while numero<0:
	print("Numero negativo")
	if intentos==2:
		print("Programa termino")
		break; #termina el programa
	numero=int(input("Ingrese Numero: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de " +str(numero)+ "es "+str(solucion))
