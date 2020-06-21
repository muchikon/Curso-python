#Condicional if
print("Evaluacion de alumnos")
nota_alumno=input("Ingrese Nota: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="Suspenso"
	elif nota<10:
		valoracion="Bien"
	else:
		valorarion="Muy bien"
	return valoracion

print(evaluacion(int(nota_alumno)))