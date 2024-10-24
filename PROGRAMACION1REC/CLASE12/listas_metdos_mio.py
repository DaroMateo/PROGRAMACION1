def mostrar_lista(lista:list)->None:
    for elem in lista:
        print(elem, end ="-")
    print(" ")
carga_alumnos = []
carga_alumnos_2 = []
# 1) Agregar 3 nombres de alumnos (ingresados por el usuario) al final de la lista.
def completar_lista(lista: list, cantidad: int, mensaje: str) -> None:
    """
    Agregar nombres de lista al final de la lista.

    Args:
        cantidad (int): Cantidad de lista a registrar
        Lista (list): Lista de nombres de los alumno

    Returns:
        list: Lista de nombres de los alumno
    """
    for _ in range(cantidad):
        nombre = input(mensaje)
        lista.append(nombre)
    return lista


carga_alumnos = completar_lista(carga_alumnos, 3, "Ingrese el nombre del alumno: ")
#mostrar_lista(carga_alumnos)
# 2) Insertar un 4to nombre de alumno (ingresado por el usuario) al principio de la lista.
print("PUNTO 2")

def insertar_elemento(carga_alumnos: list, indice: int, mensaje: str) -> None:
    """
    Insertar un elemento en una lista.

    Args:
        carga_alumnos (list): Lista de nombres de los alumno
        indice (int): Indice de la lista
        mensaje (str): Mensaje a mostrar para pedir el nombre.

    Returns:
        list: Lista de nombres de los alumno
    """
    nombre = input(mensaje)
    carga_alumnos.insert(indice, nombre)
    return carga_alumnos

carga_alumnos = insertar_elemento(carga_alumnos, 0, "Ingrese el nombre del alumno: ")
#mostrar_lista(carga_alumnos)

# 3) Extender la lista agregando 2 nombres adicionales al principio de la misma.
print("PUNTO 3")

def extender_lista(lista_uno:list, lista_dos:list) -> None:
    lista_uno.extend(lista_dos)
    return lista_uno

lista_dos = []
completar_lista(carga_alumnos_2, 2, "Ingrese un nombre: ")
extender_lista(carga_alumnos_2, carga_alumnos)
mostrar_lista(carga_alumnos_2)
print("-"*50)

# 4) Contar e informar cuántas veces aparece un nombre ingresado por el usuario.

print("Punto 4")
nombre = input("Ingrese el nombre del alumno: ")
repeticiones = carga_alumnos_2.count(nombre)
print(f"El nombre {nombre} aparece {repeticiones} veces")

# 5) Eliminar de la lista un nombre ingresado por el usuario.
def eliminar_elemento(lista:list, mensaje: str) -> None:
    """
    Eliminar un elemento de una lista.

    Args:
        lista (list): Lista de nombres de los alumno
        mensaje (str): Mensaje a mostrar para pedir el nombre.

    Returns:
        list: Lista de nombres de los alumno
    """
    nombre = input(mensaje)
    lista.remove(nombre)
    return lista
print("Punto 5")
carga_alumnos_2 = eliminar_elemento(carga_alumnos_2, "Ingrese el nombre del alumno: ")
mostrar_lista(carga_alumnos_2)

# 6) Eliminar el penúltimo nombre de la lista e informar que nombre se eliminó.
def eliminar_penultimo_elemento(lista:list) -> None:
    """
    Eliminar el penúltimo elemento de una lista.

    Args:
        lista (list): Lista de nombres de los alumno

    Returns:
        list: Lista de nombres de los alumno
    """
    lista.pop()
    return lista
print("Punto 6")
carga_alumnos_2 = eliminar_penultimo_elemento(carga_alumnos_2)
mostrar_lista(carga_alumnos_2)
# 7) Ingresar un nombre por consola, buscarlo e informar su índice.
# 8) Ordenar los nombres descendentemente.
# 9) Crear una copia de la lista.
# 10) Limpiar la lista original eliminando todos sus elementos, mostrar la lista original y la copia.
