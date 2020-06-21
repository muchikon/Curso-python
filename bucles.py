contador=0
miEmail=input("Introduce u direccion de email: ")
for i in miEmail:
	if(i=="@" or i=="."): #recorre el string y revisa si tiene el @
		contador=contador+1
if contador>=2:
	print("Email es correcto")
else:
	print("Email no es correcto")

for i in range(2):
	print("Range")

for i in [1,2,3]:
	print("Hola")
for i in ["Enero","Febrero","Marzo"]:
	print(4)
for meses in ["Enero","Febrero","Marzo"]:
	print(meses)
for meses in ["Enero","Febrero","Marzo"]:
	print(meses,end=" ") #de corrido y no uno a uno
