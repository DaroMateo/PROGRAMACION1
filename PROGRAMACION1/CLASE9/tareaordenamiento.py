"""from PROGRAMACION1.funcioneslista import funciones

lista_sexo = ["M", "F", "M", "F"]
lista_nombres = ["Pedro", "Alba", "Zacarias", "Monica"]
edades = [20, 19, 21, 25]

def ordenar_lista_ascendente(lista:list)-> list: 
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista
    
print(ordenar_lista_ascendente(lista_nombres))
print(ordenar_lista_ascendente(lista_sexo))


lista_nombres.sort
lista_sexo.sort"""

generos = ["F", "F", "M", "F","M", "M", "M", "F"]
nombres = ["Maia","Sebastiana" ,"Alan" ,"Daniela" ,"Pedro" ,"Leandro", "", "Luisa"]
nombres = ["Maia","Sebastiana" ,"Alan" ,"Daniela" ,"Pedro" ,"Leandro", "Alan", "Luisa"]
edades = [20, 19, 21, 25, 23, 24, 26, 22]
apellido = ["Garcia", "Lopez", "Lima", "Garcia", "Martino", "Lopez", "Martino", "Grandon"]

for i in range(len(generos) - 1):
    auxiliar = None
    for j in range(i + 1, len(generos)):
        if (generos[i] > generos[j]) or (generos[i] == generos[j] and apellido[i] > apellido[j]) or (generos[i] == generos[j] and apellido[i] == apellido[j] and nombres[i] > nombres[j]):
            auxiliar = generos[j]
            generos[j] = generos[i]
            generos[i] = auxiliar

            auxiliar = nombres[j]
            nombres[j] = nombres[i]
            nombres[i] = auxiliar

            auxiliar = edades[j]
            edades[j] = edades[i]
            edades[i] = auxiliar

            auxiliar = apellido[j]
            apellido[j] = apellido[i]
            apellido[i] = auxiliar

for i in range(len(generos)):
    print(generos[i] + " "  + apellido[i] + " " + nombres [i] + " " + str(edades[i]))

