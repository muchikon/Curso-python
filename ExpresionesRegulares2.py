#!/usr/bin/python
import re #importar regular expresions

pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.+),(.+),(\d+),(\d+),.*$')
#Clase de 4 digitos 
#res.group(1) es el grupo 1 = ([\d]{4,4}) que es el año 
#res.group(2) es el grupo 2 = (.+) Pais1
#res.group(3) es el grupo 3 = (.+) Pais2
#res.group(4) es el grupo 4 = (\d+) Score1 del pais1
#res.group(5) es el grupo 5 = (\d+) Score2 del pais2
#1879-04-05,England,Scotland,5,4,Friendly,London,England,FALSE

f = open("results.csv", "r", encoding='utf8')

for linea in f:
	res = re.match(pattern, linea)
	if res:
		total=int(res.group(4))+int(res.group(5))
		if total>10:
			print ("%d,%s %s-%s [%d-%d]" % (total,res.group(1),res.group(2),res.group(3),int(res.group(4)),int(res.group(5))))
		#print ("%s\n" % res.group(2))
	#print (linea)

f.close()