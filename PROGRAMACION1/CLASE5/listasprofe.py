import random
datosPersonales = ['leo', "messi", 37, "argentino"]

def mostrarDatos(datos:list):
    """_summary_

    Args:
        datos (list): _description_
    """
    for i in range(len(datos)):
        print(datos[i])

datosPersonales.append('miami')

#mostrarDatos(datosPersonales)

numeros = []

for numero in range(10):
    numeroRandom = random.randint(1, 1000)
    numeros.append(numeroRandom)
    
#mostrarDatos(numeros)


def buscarDato(lista, indice):
    retorno = False    
    if indice >= 0 and indice < len(lista):
        retorno = lista[indice]
    return retorno
        
#buscarDato(numeros, 0)
#buscarDato(numeros, 9)

#mostrarDatos(datosPersonales)
#datosPersonales.remove(37)
#mostrarDatos(datosPersonales)

itemBorrado = datosPersonales.pop()
#mostrarDatos(datosPersonales)
#print(f" fue borrado {itemBorrado}")


numerosAux = []

contador = 0

'''
for i in range(len(numeros2)):
    if numeros2[i - contador] == 5:
        numeros2.pop(i - contador)
        contador += 1

'''

"""for numero in numeros2:
    if numero != 5:
        numerosAux.append(numero)"""

#mostrarDatos(numerosAux)

numerosMinimo = None

numeros2 = [0, 2, 4, 5, 8, 9]

for i in range(len(numeros2)):
    for j in range(len(numeros2)-i):
        if i > 0 and numeros2[j] > numeros2[j+1]:
            aux = numeros2[j + 1]
            numeros2[j + 1] = numeros2[j]
            numeros2[j] = aux
        
mostrarDatos(numeros2)




