nombre = "Dario"
nombres = [["Maia","Sebastiana" ,"Alan" ,"Daniela" ,"Pedro" ,"Leandro", "Alan", "Luisa"]]
numero = [[20, 19, 21, 25] , [23, 24, 26, 22]]

"""for letra in nombre:
    print (letra)"""

"""for i in range(len(nombre)):
    print(nombre[i])"""

"""for i in range(len(nombres)):
    for j in range(len(nombres[i])):
        print(nombres[i][j])"""

matriz = [[2, 1, 3, 7] , [5, 8, 6, 4]]

"""bandera = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if bandera == False or matriz[i][j] > numero_max:
            numero_max = matriz[i][j]    
        if bandera == False or matriz[i][j] < numero_min:
            numero_min = matriz[i][j]
            bandera = True


print(numero_max, numero_min)"""
print(matriz)

#ORDENAMIENTO DE CADA FILA DE LA MATRIZ

"""for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        for k in range(len(matriz[i])):
            if matriz[i][j] < matriz[i][k]:
                auxiliar = matriz[i][j]
                matriz[i][j] = matriz[i][k] 
                matriz[i][k] = auxiliar
        
print(matriz)"""
matriz = [[2, 1, 3, 7] , [5, 8, 6, 4]]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        for k in range(len(matriz[i])):
            if k == len(matriz) - 1:
                for l in range(i+1 , len(matriz)):
                    for m in range(len(matriz[i])):
                        if matriz[i][j] > matriz[l][m]:
                            auxiliar = matriz[i][j]
                            matriz[i][j] = matriz[l][m] 
                            matriz[l][m] = auxiliar


for i in range(len(matriz)):
    for j in range(len(matriz[i])-1):
        for k in range(j+1,len(matriz[i])):
            if matriz[i][j] > matriz[i][k]:
                auxiliar = matriz[i][j]
                matriz[i][j] = matriz[i][k] 
                matriz[i][k] = auxiliar
    
print(matriz)
