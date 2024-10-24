# lista = [1, 2, 3]

# Eliminar un elemento de la lista, algoritmicamente.

# elemento_a_eliminar = 2
# lista_nueva = []
# for i in range(len(lista)):
#     if lista[i] != elemento_a_eliminar:
#         lista_nueva += [lista[i]]

# print(lista, id(lista))
# print(lista_nueva, id(lista_nueva))

# Funciones:
# len()
# print()
# input()

# # Metodos
# lista = [1,2,3]
# lista.append(5)
# saludo = "Hola"
# saludo.capitalize()

# Append (Agrega un elemento que recibe por parametro al final de la lista)
# lista = [1, 2, 3]
# print(lista) # Prohibido
# lista.append(4)
# print(lista) # Prohibido
# lista += [5] # [1, 2, 3, 4, 5]
# print(lista) # Prohibido

# Insert (Agrega un elemento a la lista en el indice donde quiera el usuario)
# lista = [1, 2, 3]
# print(lista) # Prohibido
# lista.insert(1, 4)  # -> [1, 4, 2, 3]
# print(lista) # Prohibido

# Extend (Une dos listas)
# lista = [1, 2, 3]
# lista_2 = [4, 5]
# print(lista, id(lista))
# print(lista_2, id(lista_2))
# lista.extend(lista_2)
# # lista -> [1,2,3,4,5]
# # lista_2 -> [4, 5]
# print("Despues del extend: ")
# print(lista, id(lista))
# print(lista_2, id(lista_2))

# lista = [1, 2, 3]
# saludo = "Hola" # H, o, l ,a
# lista.extend(saludo) # [1, 2, 3, H, o, l, a]
# print(lista)


# Remove (Elimina la primera ocurrencia del VALOR pasado por parametro de la lista)
# lista = ["Pepe", "Luis", "Jorge", "Pepe"]
# print(lista, id(lista))
# lista.remove("Juan") #     -> * ValueError
# print(lista, id(lista))


# Pop (Eliminar un elemento en el INDICE especificado y lo retorna)
# lista = ["Pepe", "Luis", "Jorge"]
# dato_eliminado = lista.pop(1) #     -> * IndexError
# print(lista)
# print("Se elimino:", dato_eliminado)


# Index (Busca un VALOR pasado por parametro y retorna el indice de la primera ocurrencia de ese valor)
# lista = ["Pepe", "Luis", "Jorge", "Pepe"]
# indice_encontrado = lista.index("Luis", 2) #     -> * ValueError
# print("El indice de Pepe es:", indice_encontrado)



# Sort (Ordena la lista, por defecto ASC, mediante parametro podemos ordenar DESC)
# def determinar_criterio(dato):
#     retorno = False
#     if dato % 2 == 0:
#         retorno = True
#     return retorno

# lista = [7, 2, 3, 1, 4, 5]
# lista.sort(key=determinar_criterio, reverse=True)
# print(lista)



# Reverse (Invierte los valores de la lista)
# lista = ["Pepe", "Juan", "Jorge"]
# lista.reverse()
# print(lista)


# Clear (limpia la lista)
# lista = ["Pepe", "Juan", "Jorge"]
# print(lista, id(lista))
# lista.clear()
# print(lista, id(lista))


# Count (Cuenta las ocurrencias del valor pasado por parametro)
# lista = ["Pepe", "Juan", "Jorge", "Pepe"]
# contador_nombres = lista.count("Pedro")
# print(f"Se encontraron {contador_nombres} nombres buscados.")


# Copy (Copia la lista)

# lista = ["Pepe", "Juan", "Jorge"]
# lista_2 = lista
# print(lista, id(lista))
# print(lista_2, id(lista_2))
# lista_2.append("Luis")
# print(lista, id(lista))
# print(lista_2, id(lista_2))


# Shallow Copy -> Copia Superficial
# lista_copia = lista.copy() # A
# lista_copia = lista[:] # B
# lista_copia = [] # C
# for i in range(len(lista)):
#     lista_copia.append(lista[i])
#lista = ["Pepe", "Juan", "Jorge"]
#import copy  # D
# lista_copia = copy.copy(lista)
# Deep Copy -> Copia Profunda
# lista_copia = copy.deepcopy(lista)


# print(lista, id(lista))
# print(lista_copia, id(lista_copia))
# lista_copia.append("Luis")
# print(lista, id(lista))
# print(lista_copia, id(lista_copia))

# matriz = [[1, 2],
#           [3, 4]]

# matriz_copia = matriz.copy() # Superficial o Shallow


# print(matriz, id(matriz))
# print(matriz_copia, id(matriz_copia))

# print("Primera fila de matriz original:", matriz[0], id(matriz[0]))
# print("Primera fila de matriz copia:", matriz_copia[0], id(matriz_copia[0]))

# matriz_copia[0][1] = 5

# print(matriz, id(matriz))
# print(matriz_copia, id(matriz_copia))



# for i in range(len(matriz)):
#     fila = []
#     for j in range(len(matriz[i])):
#         # fila += matriz[i][j]
#         fila.append(matriz[i][j])
#     matriz_copia += [fila]

# import copy
# matriz = [[1, 2],
#           [3, 4]]

# matriz_copia = copy.deepcopy(matriz)

# print(matriz, id(matriz))
# print(matriz_copia, id(matriz_copia))

# matriz[0][1]= 5

# print(matriz, id(matriz))
# print(matriz_copia, id(matriz_copia))



def validar_dato(lista:list, dato:any)->bool:
    retorno = False
    for i in range(len(lista)):
        if lista[i] == dato:
            retorno = True
    return retorno


# Remove (Elimina la primera ocurrencia del VALOR pasado por parametro de la lista)

# Resuelto algoritmicamente
# lista = ["Pepe", "Luis", "Jorge", "Pepe"]
# valor_a_buscar = "Juan"
# print(lista, id(lista))
# if validar_dato(lista, valor_a_buscar) == True:
#     lista.remove(valor_a_buscar) #     -> * ValueError
# else:
#     print(f"{valor_a_buscar} no existe en la lista.")
# print(lista, id(lista))

# Resulto con Exceptions
lista = ["Pepe", "Luis", "Jorge", "Pepe"]
valor_a_buscar = "Juan"
print("Antes:", lista, id(lista))
try: # try
    lista.pop(10) #     -> * ValueError
    print("despues del remove")
except ValueError as mi_error: # catch (en otros lenguajes)
    print("Error u.u:", mi_error)
except IndexError as ind_error:
    print("Error en el indice u.u", ind_error)
finally:
    print("Finally se ejecuta siempre")
print("Despues:", lista, id(lista))

# Forma basica del try-except (NO ES LO MISMO QUE UN IF-ELSE)
try:
    # Bloque Try (algo puede fallar y arrojar un error/excepcion)
    pass
except:
    # Bloque except
    print("Algo se rompio :(")


