#!/usr/bin/python
import re #importar regular expresions

pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.*),Friendly,.*$')
#Clase de 4 digitos 
#res.group(1) es el grupo 1 = ([\d]{4,4}) que es el año
#res.group(2) es el grupo 2 = (.*) que esta entre año y Friendly Ej "England,Scotland,5,4"

f = open("results.csv", encoding='utf8')
#1879-04-05,England,Scotland,5,4,Friendly,London,England,FALSE

for linea in f:
	res = re.match(pattern, linea)
	if res:
		print ("%s\n" % res.group(2))
	#print (linea)

f.close()