def ordenar_lista(lista:list, criterio:str = "asc") -> bool: # Parametros Formales: variables vacias |  Parametros Opcional
    """
    Ordena una lista de enteros en forma ascendente o descendente.
    
    Args:
        lista (list): La lista de enteros a ordenar.
        criterio (str): El criterio de ordenamiento. Puede ser "asc" o "desc".
            Por defecto es "asc".
    
    Returns:
        bool: True si hubo al menos un intercambio de elementos, False en caso contrario.
    """
    flag = False
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (criterio == "asc" and lista[i] > lista[j]) or (criterio == "dsc" and lista[i] < lista[j]):
                #SwaP
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                flag = True
    return flag

def ordenar_doble_criterio (lista_principal:list, lista_a:list, criterio:str = "asc")-> bool:
    """
    Ordena dos listas de enteros en forma ascendente o descendente.
    
    Args:
        lista_principal (list): La lista principal de enteros a ordenar.
        lista_a (list): La segunda lista de enteros a ordenar.
        criterio (str): El criterio de ordenamiento. Puede ser "asc" o "desc".
            Por defecto es "asc".
    
    Returns:
        bool: True si hubo al menos un intercambio de elementos, False en caso contrario.
    """
    flag = False 
    for i in range (len(lista_principal)-1):
        for j in range (i + 1, len (lista_principal)):
            if (criterio == "asc" and lista_principal [i] > lista_principal [j]) or (criterio == "dsc" and lista_principal [i] < lista_principal [j]):
                
                aux = lista_principal [i]
                lista_principal [i] = lista_principal [j]
                lista_principal [j] = aux

                aux = lista_a [i]
                lista_a [i] = lista_a [j]
                lista_a [j] = aux
                flag = True

            elif lista_principal [i] == lista_principal [j] :
                if (criterio == "asc" and lista_a [i] > lista_a [j]) or (criterio == "dsc" and lista_a [i] < lista_a [j]):
                
                    aux = lista_a [i]
                    lista_a [i] = lista_a [j]
                    lista_a [j] = aux
                    flag = True
    return flag

def ordenar_matriz(matriz:list, criterio:str= "asc")-> bool:  
    """
    Ordena una matriz de enteros en forma ascendente o descendente.
    
    Args:
        matriz (list): La matriz de enteros a ordenar.
        criterio (str): El criterio de ordenamiento. Puede ser "asc" o "desc".
            Por defecto es "asc".
    
    Returns:
        bool: True si hubo al menos un intercambio de elementos, False en caso contrario.
    """
    
    flag = False
    for i in range(len(matriz)): #2
        for j in range(len(matriz[i])): #3
            for k in range(len(matriz[i])):
                if k == len(matriz[i])-1: #3
                    for l in range(i+1, len(matriz)): #1
                        for m in range(len(matriz[i])): #3
                            if (matriz[i][j] > matriz[l][m] and criterio == "asc") or (matriz[i][j] < matriz[l][m] and criterio == "desc" ):
                                aux = matriz[i][j]
                                matriz[i][j] = matriz[l][m]
                                matriz[l][m] = aux
                                flag = True
    #Ordena cada array dentro de la matriz
    for i in range(len(matriz)): #2
        for j in range(len(matriz[i])-1): #3
            for k in range(j+1, len(matriz[i])):
                if (matriz[i][j] > matriz[i][k] and criterio == "asc") or (matriz[i][j] < matriz[i][k] and criterio == "desc"):
                    aux = matriz[i][j]
                    matriz[i][j] = matriz[i][k]
                    matriz[i][k] = aux
                    flag = True

    return flag