def mostrar_menu():
    print("Menu")
    print("1- alta")
    print("2- listar")
    print("3- baja")
    print("4- modificar")
    print("5- salir")

def alta(nombres, edades, estado):
    indice = buscar_libre(estado, "LIBRE")
    if indice >= 0:
        nombres[indice] = input('Ingrese nombre: ')
        edades[indice] = int(input('Ingrese edad: '))
        estado[indice] = "OCUPADO"
    else:
        print("No se encontraron espacios disponibles")

def listar(nombres, edades, estado):
    if lista_vacia(estado, "LIBRE"):
        print("No hay datos para listar")
    else:
        for i, item in enumerate(estado):
            if item != "LIBRE":
                print(f"Nombre: {nombres[i]}, Edad: {edades[i]}")

def baja(nombres, edades, estado):
    if lista_vacia(estado, "LIBRE"):
        print("No hay datos para eliminar")
    else:
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        indice = buscar(nombres, nombre_buscar)
        if indice >= 0:
            print("Dato encontrado")
            mostrar(nombres, edades, indice)
            confirmar = input("Desea borrar [S | N]? ")
            while not validar_respuesta(confirmar):
                confirmar = input("Desea borrar [S | N]? ")
            if confirmar.upper() == "S":
                estado[indice] = "LIBRE"
                print("El dato se ha eliminado")
            else:
                print("El dato no se ha eliminado")
        else:
            print("El nombre buscado no se encuentra en la lista")

def modificar(nombres, edades, estado):
    if lista_vacia(estado, "LIBRE"):
        print("No hay datos para modificar")
    else:
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        indice = buscar(nombres, nombre_buscar)
        if indice >= 0:
            print("Dato encontrado")
            mostrar(nombres, edades, indice)
            confirmar = input("Desea modificar [S | N]? ")
            while not validar_respuesta(confirmar):
                confirmar = input("Desea modificar [S | N]? ")
            if confirmar.upper() == "S":
                nombres[indice] = input("Ingrese un nuevo nombre: ")
                edades[indice] = int(input('Ingrese nueva edad: '))
                print("El dato se ha modificado")
            else:
                print("El dato no se ha modificado")
        else:
            print("El nombre buscado no se encuentra en la lista")

def buscar_libre(estado, valor):
    for i, item in enumerate(estado):
        if item == valor:
            return i
    return -1

def lista_vacia(estado, valor):
    return valor not in estado

def buscar(nombres, nombre):
    for i, item in enumerate(nombres):
        if item == nombre:
            return i
    return -1

def mostrar(nombres, edades, indice):
    print(f"Nombre: {nombres[indice]}, Edad: {edades[indice]}")

def validar_respuesta(respuesta):
    return respuesta.upper() in ["S", "N"]

def main():
    nombres = [""] * 10
    edades = [0] * 10
    estado = ["LIBRE"] * 10
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            alta(nombres, edades, estado)
        elif opcion == 2:
            listar(nombres, edades, estado)
        elif opcion == 3:
            baja(nombres, edades, estado)
        elif opcion == 4:
            modificar(nombres, edades, estado)
        elif opcion == 5:
            continuar = False
        else:
            print("La opción ingresada no es correcta")

if __name__ == "__main__":
    main()