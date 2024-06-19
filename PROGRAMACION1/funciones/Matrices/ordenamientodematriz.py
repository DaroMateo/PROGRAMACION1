def ordenar_matriz(matriz):
    """
    Ordena una matriz en orden ascendente por fila.

    Args:
    matriz (lista[lista[int]]): La matriz a ordenar.

    Returns:
    Ninguno. La matriz está ordenada en su lugar.
    """
    for i in range(len(matriz)): #2
        for j in range(len(matriz[i])): #3
            for k in range(len(matriz[i])):
                if k == len(matriz[i])-1: #3
                    for l in range(i+1, len(matriz)): #1
                        for m in range(len(matriz[i])): #3
                            if matriz[i][j] > matriz[l][m]:
                                aux = matriz[i][j]
                                matriz[i][j] = matriz[l][m]
                                matriz[l][m] = aux
#Ordena cada array dentro de la matriz
    for i in range(len(matriz)): #2
        for j in range(len(matriz[i])-1): #3
            for k in range(j+1, len(matriz[i])):
                if matriz[i][j] > matriz[i][k]:
                    aux = matriz[i][j]
                    matriz[i][j] = matriz[i][k]
                    matriz[i][k] = aux