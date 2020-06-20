#Lista
miLista=["Juan","Edwin","Arturo","Jose"]
miLista.append("Sandra") #Agrega al final Sandra en la Lista
miLista.extend(["Maria","Ana"]) #Agrega Maria y Ana
print(miLista)
miLista.remove("Maria")
print(miLista)
miLista.pop() #retira el ultimo de la lista
print("miLista: ",miLista)
miLista1=[5,2,4]
miLista4=miLista+miLista1
print("MiLista4: ",miLista4)
print("miLista1*3: ",miLista1*3)
print("miLista.index(Sandra): ",miLista.index("Sandra"))
print("Luis" in miLista)
print(miLista[:])
print(miLista)
print(miLista[-2])
print(miLista[:2])
print(miLista[1:3])
print(miLista[2:])