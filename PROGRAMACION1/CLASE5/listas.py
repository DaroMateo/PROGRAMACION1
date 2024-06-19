import random

#TUPLAS (tuple) : son inmutables no se pueden modificar los datos

#recorrer una lista
datospersonales = ['leo', 'messi' , '37', 'argentino']

#creando funcion con un lista
def mostrardatos(datos:list):
    for i in range (len(datospersonales)):
     print(datospersonales(i))

#agregas datos a la lista

datospersonales.append('miami')

#mostrardatos(datospersonales)
    
#busca datos en la lista de 0 en adelante
#print(lista[1])

#recorre la lista de principio a fin y visualisar datos
"""for dato in datospersonales:
    print(dato)"""

numero = []

for numero in range(10):
   numero.append(numero + 1)

#mostrardatos(numero)

for numero in range(10):
   numerorandom = random.radiant(1,1000)
   numero.append(numerorandom)

#mostrardatos(numero)

#funcion si busca un dato fuera de la lista

def buscardato(lista, indice):
   retorno = False
   if indice > 0 and indice < len(lista):
      retorno = lista(indice)
   return retorno

#buscardato(numero, 0)
#buscardato(numero, 9)

#REMUEVE EL ELEMENTO DE LA LISTA, Y CAMBIA LA POSICIONES DE LA LISTA

mostrardatos(datospersonales)
datospersonales.remove(37)
#mostrardatos(datospersonales)

#si no le pasas info en los parentesis borra el ultimo ()

datospersonales.pop(1)
mostrardatos(datospersonales)

'''itemborrado = datospersonales.pop(1)
mostrardatos(datospersonales)
print(f'fue borrado{itemborrado}')'''

'''numero2 = [5,4,8,9,5,7,4]
for numero in numero2:
   if numero == 5:
      numero2.remove(numero)

mostrardatos(numero2)'''

# te aseguras de pasar por toda la lista, vuelve al principio de la lista

numero2 = [5, 5, 5, 9, 5, 7, 4, 5, 8, 10, 7, 9, 5]

numeroaux =[]

contador = 0
'''
for i in range(len(numero2)):
   if numero2[i - contador] == 5:
      numero2.pop(i - contador)
      contador += 1

mostrardatos(numero2)
'''

#LO MAS RECOMENDABLE, PORQUE LO ANTERIOR BORRA LOS DATOS DE LA LISTA
'''
for numero in numero2:
   if numero != 5:
      numeroaux.append(numero)

mostrardatos(numeroaux)
'''
#ORDENAR LA LISTA DE MENOR A MAYOR
numerominimo = None

numero3 = [5, 2, 9, 8, 0, 4]
#suapeo o intercambio
for i in range(len(numero3)):
   for j in range(len(numero3) - i):
      if i > 0 and numero3[j] > numero3[j + 1]:
           aux = numero3 [j + 1]
           numero3 [j + 1] = numero3[j]
           numero3[j] = aux

mostrardatos(numero3)

