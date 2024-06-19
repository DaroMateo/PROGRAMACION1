matriz=[[20, 19, 21, 25],[23, 24, 26, 22],[30,20,15,9]]
lista = [8, 5, 2, 6, 9]

print(matriz)

def ordenar_matriz(matrix):
    #obtiene el numero de filas
    filas = len(matrix)
    #Obtiene el numero de columnas
    cols = len(matrix[0])  
    for i in range(filas):
        for j in range(cols):
            for k in range(filas):
                for l in range(cols - 1):
                    print(i, j, k, l)
                    if matrix[k][l] > matrix[k][l + 1]:
                        print("IF SWAP INT", matrix[k][l], matrix[k][l + 1])
                        matrix[k][l], matrix[k][l + 1] = matrix[k][l + 1], matrix[k][l]
                        print("SWAPEADO INT", matrix[k][l], matrix[k][l + 1])
                if k < filas - 1 and matrix[k][cols - 1] > matrix[k + 1][0]:
                    print("IF FILA", i, j, k, l)
                    print("SWAP +FILA", matrix[k][cols - 1], matrix[k + 1][0])
                    matrix[k][cols - 1], matrix[k + 1][0] = matrix[k + 1][0], matrix[k][cols - 1]
                    print("SWAPEADO +FILA", matrix[k][cols - 1], matrix[k + 1][0])
            
ordenar_matriz(matriz)

print(matriz)
