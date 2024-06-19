"""carga mixta"""
from os import system 
from PROGRAMACION1.funcioneslista import funcionespablo

nombres = ["A","A","A","A","A"]
estado = ["LIBRE","LIBRE","LIBRE","LIBRE","LIBRE"]
edad = ["A","A","A","A","A"]
continuar = True


while continuar == True:
    
    print ("Menu")
    print ("1- alta")
    print ("2- listar")
    print ("3- baja")
    print ("4- modificar")
    print ("5- salir")

    opcion = ingresar_opcion(1,5)
    system("cls")

    match opcion:
        case 1:
            indice = buscar_libre(estado,"LIBRE")
            if indice >= 0:
                nombres[indice] = alta('Ingrese nombre: ')
                edad[indice] = alta('Ingrese edad: ')
                estado[indice] = "OCUPADO"                
        case 2:
            if lista_vacia(estado,"LIBRE","listar") == False:
                listar(estado, nombres, edad)
        case 3:
            if lista_vacia(estado, "LIBRE","eliminar") == False:
                indice = ingresar_dato_buscar(nombres,"nombre")
                if indice >= 0:
                    mostrar(nombres, edad, indice)
                    confirmar = confirmar_si_o_no("borrar")
                    if confirmar:    
                        estado[indice] = "LIBRE"
                    imprimir_estado_dato("eliminado", confirmar)
        case 4:
            if not lista_vacia(estado, "LIBRE","modificar"):
                indice = ingresar_dato_buscar(nombres,"perro")
                if indice >= 0:
                    mostrar(nombres, edad, indice)
                    confirmar = confirmar_si_o_no("modificar")
                    if confirmar:    
                        nombres[indice] = input("ingrese un nuevo nombre: ") 
                    imprimir_estado_dato("modificado", confirmar)
        case 5:
            continuar = False