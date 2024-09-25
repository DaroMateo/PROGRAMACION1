def iniciarlizar_matriz(cant_filas:int, cant_columnas:int)->list:
    '''
    Inicializa una matriz de 2x2
    recibe cantidad de filas y columnas
    Retorna una matriz inicializada en 0s
    '''
    matriz =[]
    for _ in range(cant_filas):
        fila= [0] * cant_columnas
        matriz += [fila]
    return matriz

def imprimir_matriz(matriz:list)->None:
    '''
    Imprime la matriz de 2x2
    Recibe una matriz
    No tiene retorno
    '''
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print(f"{matriz[i][j]:3}", end=" ")
        print("")

def buscar_coordenada_matriz(matriz:list, dato:int)->list: #Print mas lista con coordenada
    '''
    Busca las coordenadas de un dato en una matriz de 2x2
    Recibe una matriz y un dato parametro
    Devuelve una lista con la coordenada
    '''
    coordenada = []
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == dato:
                print(f"La coordenada del elemento {dato} es {i},{j}")
                coordenada += [i]
                coordenada += [j]
    return coordenada

mi_matriz = iniciarlizar_matriz(4,4)                # La inicializo
mi_matriz[0][1] = 8                                 # Le modifico 1 dato
imprimir_matriz(mi_matriz)                          # La imprimo
coordenada = buscar_coordenada_matriz(mi_matriz,8)  # Busco la coordenada