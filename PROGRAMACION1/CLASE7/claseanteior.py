"""carga mixta"""
from os import system 

def listar(lista1:list, lista2:list, lista3:list): #se debe pasar 3 listas
    for i in range(len(lista1)):
        if lista1[i] != "LIBRE":
            mostrar(lista2, lista3, i)
            """print(lista[i])"""  

def mostrar(lista:list, lista1:list, indice:int): #2 listas + indice
    print(f"{lista[indice]}, {lista1[indice]}")  

def buscar(lista:list,dato:str)-> int:
    """
    busca un dato en una lista.
    Si lo encuentra retorna el indice.
    Si no lo encuentra retorna -1
    """
    retorno = -1
    for i in range(len(lista)):
        if dato == lista[i]:
            retorno = i
            break
    return retorno

def validar_respuesta(rta:str)-> bool:
    retorno = False
    if rta == "S" or rta == "s" or rta=="N" or rta == "n":
        retorno = True
    return retorno

def alta(mensaje:str):
    dato = input(mensaje)
    return dato

def buscar_libre(lista:list,libre:str)->int:
    retorno=-1
    for i in range(len(lista)):
        if lista[i] == libre:
            retorno=i
            break
    return retorno

def lista_vacia(lista:list,libre:str)->bool:
    retorno=True
    for i in range(len(lista)):
        if lista[i]!=libre:
            retorno=False
            break
    return retorno



nombres = ["A","A","A","A","A"]
estado = ["LIBRE","LIBRE","LIBRE","LIBRE","LIBRE"]
edad=["A","A","A","A","A"]
continuar = True


while continuar == True:
    
    print ("Menu")
    print ("1- alta")
    print ("2- listar")
    print ("3- baja")
    print ("4- modificar")
    print ("5- salir")

    opcion = input("Ingrese una opción: ")
    opcion = int(opcion)
    system("cls")

    match opcion:
        case 1:
            indice = buscar_libre(estado,"LIBRE")
            if indice >= 0:
                nombres[indice] = alta('Ingrese nombre: ')
                edad[indice] = alta('Ingrese edad: ')
                estado[indice] = "OCUPADO"
            else:
                print ("No se encontraron espacios disponibles")
                
        case 2:
            if lista_vacia(estado,"LIBRE") == False:
                listar(estado, nombres, edad)
            else:
                print("No hay datos para listar")
        case 3:
            if lista_vacia(estado, "LIBRE") == False:
                nombre_buscar = input ("Ingrese el nombre a buscar: ")
                indice = buscar(nombres,nombre_buscar)
                if indice >= 0:
                    print("Dato encontrado")
                    mostrar(nombres, edad, indice)
                    confirmar = input("Desea borrar [S | N]? ")
                    while validar_respuesta(confirmar)== False:
                        confirmar = input("Desea borrar [S | N]? ")
                    if confirmar == "S" or confirmar =="s":    
                        estado[indice] = "LIBRE"
                        print("El dato se ha eliminado")                            
                    else:
                        print("El dato no se ha eliminado")
                else:
                    print ("El nombre buscado no se encuentra en la lista")
            else:
                print("No hay datos para eliminar")
        case 4:
            if lista_vacia(estado, "LIBRE") == False:
                nombre_buscar = input ("Ingrese el nombre a buscar: ")
                indice = buscar(nombres,nombre_buscar)
                if indice >= 0:
                    print("Dato encontrado")
                    mostrar(nombres, estado, indice)
                    confirmar = input("Desea modificar [S | N]? ")
                    while validar_respuesta(confirmar)== False:
                        confirmar = input("Desea modificar [S | N]? ")
                    if confirmar == "S" or confirmar == "s":    
                        nombres[indice] = input("ingrese un nuevo nombre: ") 
                        edad[indice] = alta('Ingrese nueva edad: ')
                        print("El dato se ha modificado")                            
                    else:
                        print("El dato no se ha modificado")
                else:
                    print ("El nombre buscado no se encuentra en la lista")
            else:
                print("No hay datos para modificar")
        case 5:
            continuar = False
        case _:
            print ("La opción ingresada no es correcta")








"""carga aleatoria"""
# nombres = ["A","A","A","A","A"]

# for i in range(len(nombres)):
#     nombre = input("Ingrese un nombre: ")
#     indice = input("Ingrese el indice: ")
#     indice = int(indice)

#     while indice < 0 or indice > len(nombres) or nombres[indice] != "A":
#         indice = input("ERROR reingrese el indice: ")
#         indice = int(indice)

#     nombres[indice] = nombre

# # nombres[2] = "burns"

# for i in range(len(nombres)):
#     print(nombres[i])







"""carga secuencial"""
# nombres = ["A","A","A","A","A"]

# for i in range(len(nombres)):
#     nombre = input("Ingrese un nombre: ")
#     nombres[i] = nombre

# nombres[2] = "burns"

# for i in range(len(nombres)):
#     print(nombres[i])
