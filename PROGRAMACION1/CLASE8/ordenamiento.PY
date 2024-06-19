#lista = [3, 8 ,1 , 5, 4]
#lista_dos = ["Pedro", "Alba", "Zacarias", "Monica"]

#sort ordena en base a numeros ASCII

#lista_dos.sort()

#print(lista_dos)

#65 = A
#97 = a

#2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0
#128 64   32  16  8   4   2   1
#0   1     0   0  0   0   0   1


#128 64 32 16 8 4 2 1
#0   1  1  0  0 0 0 1

#01000001
#01100001

#19| 1 = DECENA | 9 = UNIDAD

#ORD NUESTRA POCISION DE LA TABLA ASCII
#BIN MUESTRA EL VALOR BINARIO

#print(bin(ord("a")))

#ana
#ZOE

#----------------------------------------------------------
#BUBBLE SORT

lista = [3, 8 ,1 , 5, 4]
lista_dos = ["Pedro", "Alba", "Zacarias", "Monica"]


#ASCENDENTE:
#Si fuera letras seria de la A a la z.
#Si fueran numeros serian del 0 al 9.

print(lista)

"""
def ordenar_lista_ascendente(lista:list)-> list: 
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista
    
print(ordenar_lista_ascendente(lista))
"""

#print(ordenar_lista_ascendente(lista))

def swap(lista, indice_uno, indice_dos):
    auxiliar = lista[indice_uno]
    lista[indice_uno] = lista[indice_dos]
    lista[indice_dos] = auxiliar
    
    return lista

def ordenar_array(lista:list, criterio:str = "ASC")-> list: 
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (criterio == "ASC" and lista[i] > lista[j]) or (criterio == "DESC" and lista[i] < lista[j]):
                swap(lista, i, j)
                #swap
                #auxiliar = lista[i]
                #lista[i] = lista[j]
                #lista[j] = auxiliar
    
    return lista

print(ordenar_array(lista, "DESC"))

lista.sort()

#(5 . 3) + (3 . 5)

#DESENDENTE
#Si fuera letra de la z a la A
#si fuera nuermos seria del 9 al 0

#lista = [3, 8, 1, 5, 4]
#lista = [3, 8, 1, 5, 4] i = 0| j = 1
#lista = [3, 8, 1, 5, 4] i = 0 | j = 2
#lista = [1, 8, 3, 5, 4] i = 0 | j = 3
#lista = [1, 8, 3, 5, 4] i = 0 | j = 4

#lista = [1, 8, 3, 5, 4] i = 1 | j = 2
#lista = [1, 3, 8, 5, 4] i = 1 | j = 3
#lista = [1, 3, 8, 5, 4] i = 1 | j = 4

#lista = [1, 3, 5, 8, 4] i = 2 | j = 3
#lista = [1, 3, 4, 8, 5] i = 1 | j = 4

#lista = [1, 3, 4, 5, 8] i = 1 | j = 4