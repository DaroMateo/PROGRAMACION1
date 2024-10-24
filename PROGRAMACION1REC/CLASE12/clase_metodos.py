def extender_lista(lista_uno:list, lista_dos:list) -> None:
    lista_uno.extend(lista_dos)

def completar_lista(lista:list, largo_lista:int, mensaje:str) -> None:
    for _ in range(largo_lista):
        dato = input(mensaje)
        lista.append(dato) 

def mostrar_lista(lista:list)->None:
    '''
    Recibe una lista y la imprime
    '''
    for elemento in lista:
        print(elemento)
        
def insertar_dato_en_lista(lista:list, mensaje:str, indice:int) -> None:
    dato = input(mensaje)
    lista.insert(indice, dato)


# 5) Eliminar de la lista un nombre ingresado por el usuario.
def eliminar_dato(lista:list, mensaje:str):
    dato = input(mensaje)
    lista.remove(dato)

# # 6) Eliminar el penúltimo nombre de la lista e informar que nombre se eliminó.
def eliminar_indice(lista:list, mensaje:str) -> str: 
    indice = int(input(mensaje))
    while indice < 0 or indice >= len(lista) :
        indice = int(input('error: '+ mensaje))
    dato_eliminado = lista.pop(indice)
    return dato_eliminado

'''
Declarar una lista vacía, y manipularla mediante métodos de listas, mostrando los resultados después de cada operación:
'''
#  1) Agregar 3 nombres de alumnos (ingresados por el usuario) al final de la lista.
lista = []
print("Punto 1")
completar_lista(lista, 3, "Ingrese un nombre: ")
mostrar_lista(lista)
print("-"*50)    

# 2) Insertar un 4to nombre de alumno (ingresado por el usuario) al principio de la lista.
print("Punto 2")
insertar_dato_en_lista(lista, "Ingrese el dato: ", 0)
mostrar_lista(lista)
print("-"*50)    

# 3) Extender la lista agregando 2 nombres adicionales al principio de la misma.
print("Punto 3")

lista_dos = []
completar_lista(lista_dos, 2, "Ingrese un nombre: ")
extender_lista(lista_dos, lista)
mostrar_lista(lista_dos)
print("-"*50)    

# 4) Contar e informar cuántas veces aparece un nombre ingresado por el usuario.
print("Punto 4")
nombre = input("Ingrese el nombre a buscar: ")
repeticiones = lista_dos.count(nombre)
print(f"El nombre '{nombre}' se repite {repeticiones} veces")
print("-"*50)  

# 5) Eliminar de la lista un nombre ingresado por el usuario.
print('punto 5')
eliminar_dato(lista_dos,"ingrese dato a eliminar")
mostrar_lista(lista_dos)

# 6) Eliminar el penúltimo nombre de la lista e informar que nombre se eliminó.
print('punto 6')
dato_eliminado = eliminar_indice(lista_dos,'ingrese el indice al dato a eliminar')
mostrar_lista(lista_dos)
print(f'se elimino {dato_eliminado}')

# 7) Ingresar un nombre por consola, buscarlo e informar su índice.
# 8) Ordenar los nombres descendentemente.
# 9) Crear una copia de la lista.
# 10) Limpiar la lista original eliminando todos sus elementos, mostrar la lista original y la copia.