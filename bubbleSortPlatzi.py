#1.- Comparaciones de elementos adyacentes
#2.- Repetir hasta tener una pasada completa sin ningun swap
def bubbleSort(array):
	n=len(array)
	print("Elementos n:",n)	
	for i in range(n):  #recorre los elementos del array
		#print(array," i:",i)
		print(array)
		contador=0	
		for j in range(0,n-i-1): 
			#print("rango:0,",n-i-1,"j:",j)			
			if array[j]>array[j+1]:
				array[j],array[j+1]=array[j+1],array[j]	
				contador=contador+1			
			#print(array[j],array[j+1])
		if contador==0:
			break
			
array=[1,4,2,3]
bubbleSort(array)
print("Arreglo ordenado: ")
for i in range(len(array)):
	print("%d"%array[i])




