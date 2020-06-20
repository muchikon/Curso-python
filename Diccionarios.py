#Diccionarios en Python
miDiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
print(miDiccionario) #imprime el diccionario
print(miDiccionario.keys()) #imprime los Keys
print(miDiccionario.values()) #imprime los valores
print("Longitud de Diccionario: ",len(miDiccionario)) #Longitud del diccionario
print(miDiccionario["Francia"]) #valor asignado a Francia
miDiccionario["Italia"]="Lisboa" #agregar un elemento al diccionario
print(miDiccionario)
miDiccionario["Italia"]="Roma" #sobrescribe el valor
print(miDiccionario)
del miDiccionario["Reino Unido"] #eliminar un valor del diccionario
print(miDiccionario)
miDiccionario2={"Alemania":"Berlin",23:"Jordan"}
print(miDiccionario2)
