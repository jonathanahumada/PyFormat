
def sacarlineas(archivo):
	foo = open(archivo)
	boo = foo.readlines()
	foo.close()
	return boo  


def buscarporlinea(lista, string):
	results = []
	for linea in lista:
 		print(linea)
 		if linea.find(string) != -1:
 			results.append(linea)

	return results 