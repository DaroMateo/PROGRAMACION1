matriz =  [ [1, 5, 3, 7],  #3x4
            [2, 6, 4, 8], 
            [12, 10, 11, 9] ] 

print(matriz)

#Redistribuye cada elemento de cada array dentro del arrary que corresponda
#para luego orproceder a ordenar cada array dentro de la matriz

#Primera parte, ordena las listas para reubicar los elemntos de la lista
for i in range(len(matriz)): #2 #0,1,2
    #print(i)
    for j in range(len(matriz[i])): #3 #0,1,2,3
        #print (i,j)
        for k in range(len(matriz[i])): # 0,1,2,3
            #print(i,j,k)
            if k == len(matriz[i])-1: #3 #0,1,2,3
                #print(k)
                for l in range(i+1, len(matriz)): #1 
                    for m in range(len(matriz[i])): #3
                        if matriz[i][j] > matriz[l][m]:
                            #Swap 
                            aux = matriz[i][j]
                            matriz[i][j] = matriz[l][m]
                            matriz[l][m] = aux
                            

print(matriz)

#Segunda parte, ordena cada elemento de las lista de forma ASX

#Ordena cada array dentro de la matriz
for i in range(len(matriz)): #2 
    for j in range(len(matriz[i])-1): #3 
        for k in range(j+1, len(matriz[i])):
            if matriz[i][j] > matriz[i][k]:
                aux = matriz[i][j]
                matriz[i][j] = matriz[i][k]
                matriz[i][k] = aux

print(matriz)