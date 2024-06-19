""" 1) Crear una lista de entre 10 a 15 numeros, todos los numeros tiene se ser de forma ramdom
    2) Recorrer la lista imprimiendo por consola la lista, de la siguiente manera ([indice] valor)
    3) Determinar cuál es el numero mas grande, imprimiendo por consola de la siguiente manera ([indice] valor)
    4) Determinar cuál es el numero mas chico, imprimiendo por consola de la siguiente manera ([indice] valor)
    5) Calcular promedio
Para todo usar funciones, con "nombres claros y representativos"
"""

import random

#1 1) Crear una lista de entre 10 a 15 numeros, todos los numeros tiene se ser de forma ramdom

def crear_lista_numeros_random(tope):
    numeros = []
    for i in range (tope):
        numeros.append(random.randint(0, 99))

    return numeros

tope = random.randint(10,15)
lista = crear_lista_numeros_random(5)

#2 2) Recorrer la lista imprimiendo por consola la lista, de la siguiente manera ([indice] valor)

def mostrar_lista(lista):
    for i in range(len(lista)):
        return (f"([{i}] {lista[i]})" )

#mostrar_lista(lista)


#3 3) Determinar cuál es el numero mas grande, imprimiendo por consola de la siguiente manera ([indice] valor)

def buscar_num_max(lista):
    numero_max = lista[0]
    for i in range(len(lista)):
        if lista[i] > numero_max:
            numero_max = lista[i]
    return numero_max

def buscar_indice(lista, numero):
    retorno = -1
    for i in range(len(lista)):
        if numero == lista[i]:
            retorno = i
    return retorno
            
def mostrar_informacion(indice, valor):
    print(f"([{indice}] {valor})")

#valor = buscar_num_max(lista)
#indice = buscar_indice(lista, valor)

#mostrar_informacion(indice, valor)

            
#print(lista)
#print(buscar_num_max(lista))

# 4) Determinar cuál es el numero mas chico, imprimiendo por consola de la siguiente manera ([indice] valor)

def buscar_num_min(lista):
    numero_min = lista[0]
    for i in range(len(lista)):
        if lista[i] < numero_min:
            numero_min = lista[i]
    return numero_min

#valor = buscar_num_min(lista)
#indice = buscar_indice(lista, valor)

#mostrar_informacion(indice, valor)

#5) Calcular promedio

def sumar_elementos_lista(lista):
    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    return acumulador

def calcular_promedio(lista):
    promedio = 0
    acumulador = sumar_elementos_lista(lista)
    if len(lista) > 0:
        promedio = acumulador / len(lista)
    
    return promedio

print(lista)
print(calcular_promedio(lista))