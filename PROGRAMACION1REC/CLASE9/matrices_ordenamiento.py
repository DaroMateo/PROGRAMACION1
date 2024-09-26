import random
lista = [3, 8 ,1 , 5, 4]
def ordenar_lista_ascendente(lista:list)-> list: 
    """
    Ordena una lista de enteros en forma ascendente.

    Args:
        lista (list): La lista de enteros a ordenar.

    Returns:
        list: La lista ordenada en forma ascendente.
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista
    
# print(ordenar_lista_ascendente(lista))

def swap(lista, indice_uno, indice_dos):
    """
    Intercambia los valores en dos posiciones de una lista.
    
    Args:
        lista (list): La lista en la que se realizar  el intercambio.
        indice_uno (int): El primer ndice a intercambiar.
        indice_dos (int): El segundo ndice a intercambiar.
    
    Returns:
        list: La lista con los valores intercambiados.
    """
    auxiliar = lista[indice_uno]
    lista[indice_uno] = lista[indice_dos]
    lista[indice_dos] = auxiliar
    
    return lista

def ordenar_array(lista:list, criterio:str = "ASC")-> list: 
    """
    Ordena una lista de enteros en forma ascendente o descendente.
    
    Args:
        lista (list): La lista de enteros a ordenar.
        criterio (str): El criterio de ordenamiento. Puede ser "ASC" o "DESC".
            Por defecto es "ASC".
    
    Returns:
        list: La lista ordenada seg n el criterio seleccionado.
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (criterio == "ASC" and lista[i] > lista[j]) or (criterio == "DESC" and lista[i] < lista[j]):
                swap(lista, i, j)
                #swap
                #auxiliar = lista[i]
                #lista[i] = lista[j]
                #lista[j] = auxiliar
    
    return lista

def mostrar_lista(lista:list)->None:
    """
    Muestra los elementos de una lista.

    Parameters:
    lista (list): la lista a mostrar
    """
    for elem in lista:
        print(elem, end=" ")

def mostrar_listas_paralelas (lista_principal:list, lista_a:list)->None:
    """
    Muestra los elementos de las listas paralelas.

    Parameters:
    lista_principal (list): la lista principal
    lista_a (list): la lista a
    """
    for i in range(len(lista_principal)):
        print(f"{lista_principal[i]}, {lista_a[i]}")

def mostrar_listas_paralelas (lista_principal:list, lista_a:list, lista_b:list)->None:
    """
    Muestra los elementos de las listas paralelas.

    Parameters:
    lista_principal (list): la lista principal
    lista_a (list): la lista a
    lista_b (list): la lista b
    """
    for i in range(len(lista_principal)):
        print(f"{lista_principal[i]}, {lista_a[i]}, {lista_b[i]} ")



# lista_ordenada = ordenar_array(lista, "ASC")
# mostrar_lista(lista_ordenada)

# lista_nombre = ["Pedro", "Alba", "Zacarias", "Monica","Eduardo"]
# lista_apellidos = ["Garcia", "Lopez", "Lima", "Garcia","Perez"]
# lista_edades = [20, 19, 21, 25,30]

def ordenar_listas_paralelas(lista_principal:list, lista_a:list, lista_b:list, criterio:str = "ASC")->bool:
    flag = False
    for i in range (len(lista_principal)-1):
        for j in range (i + 1, len(lista_principal)):
            if (criterio == "asc" and lista_principal[i] > lista_principal[j]) or (criterio == "dsc" and lista_principal[i] < lista_principal[j]):
                aux = lista_principal[i]
                lista_principal[i] = lista_principal[j]
                lista_principal[j] = aux
                
                aux = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = aux

                aux = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = aux

                flag = True

    return  flag


# ordenar_listas_paralelas(lista_nombre, lista_apellidos, lista_edades, "dsc")

# mostrar_lista (lista_nombre)
# mostrar_lista (lista_apellidos)
# mostrar_lista (lista_edades)

# nombres_alumnos = ["Pedro", "Zacarias", "Elias", "Monica","Eduardo"]
# calificaciones = [6, 5, 6, 8,10]

def ordenar_doble_criterio(lista_principal:list, lista_a:list, criterio_principal:str = "ASC")->bool:
    flag = False
    for i in range (len(lista_principal)-1):
        for j in range (i + 1, len(lista_principal)):
            if (criterio_principal == "asc" and lista_principal[i] > lista_principal[j]) or (criterio_principal == "dsc" and lista_principal[i] < lista_principal[j]):
                aux = lista_principal[i]
                lista_principal[i] = lista_principal[j]
                lista_principal[j] = aux

                aux = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = aux

                flag = True
                
            elif lista_principal[i] == lista_principal[j]:
                if (criterio_principal == "asc" and lista_a[i] > lista_a[j]) or (criterio_principal == "dsc" and lista_a[i] < lista_a[j]):
                    aux = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = aux

                    flag = True

    return  flag

# ordenar_doble_criterio(nombres_alumnos, calificaciones, "asc")

# mostrar_listas_paralelas (calificaciones, nombres_alumnos)


mi_matriz = [[4,2,8,6] , [5,1,7,3]]

for i in range(len(mi_matriz)): 
    for j in range(len(mi_matriz[i])): 
        for k in range(len(mi_matriz)-1): 
                for l in range(i+1 , len(mi_matriz)): 
                    for m in range(len(mi_matriz[i])): 
                        if mi_matriz[i][j] > mi_matriz[l][m]: 
                            auxiliar = mi_matriz[i][j]
                            mi_matriz[i][j] = mi_matriz[l][m] 
                            mi_matriz[l][m] = auxiliar 


for i in range(len(mi_matriz)):  
    for j in range(len(mi_matriz[i])-1): 
        for k in range(j+1,len(mi_matriz[i])): 
            if mi_matriz[i][j] > mi_matriz[i][k]: 
                auxiliar = mi_matriz[i][j]
                mi_matriz[i][j] = mi_matriz[i][k]  
                mi_matriz[i][k] = auxiliar  
    
print(mi_matriz)
