# lista = [7, 3, 5, 2, 1]

def ordenar_lista(lista:list, criterio:str = "asc") -> bool: # Parametros Formales: variables vacias |  Parametros Opcional
    flag = False
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (criterio == "asc" and lista[i] > lista[j]) or (criterio == "dsc" and lista[i] < lista[j]):
                #SwaP
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                flag = True
    return flag

# ordenar_lista(lista) # Parametros actuales
# print(lista)
# ordenar_lista(lista, "dsc") # Parametros actuales
# print(lista)

def ordenar_doble_criterio (lista_principal:list, lista_a:list, criterio:str = "asc")-> bool:
    flag = False 
    for i in range (len(lista_principal)-1):
        for j in range (i + 1, len (lista_principal)):
            if (criterio == "asc" and lista_principal [i] > lista_principal [j]) or (criterio == "dsc" and lista_principal [i] < lista_principal [j]):
                
                aux = lista_principal [i]
                lista_principal [i] = lista_principal [j]
                lista_principal [j] = aux

                aux = lista_a [i]
                lista_a [i] = lista_a [j]
                lista_a [j] = aux
                flag = True

            elif lista_principal [i] == lista_principal [j] :
                if (criterio == "asc" and lista_a [i] > lista_a [j]) or (criterio == "dsc" and lista_a [i] < lista_a [j]):
                
                    aux = lista_a [i]
                    lista_a [i] = lista_a [j]
                    lista_a [j] = aux
                    flag = True
    return flag

# ordenar_doble_criterio (calificaciones_alumnos, nombre_alumnos, "dsc")
# print (calificaciones_alumnos)
# print (nombre_alumnos)

# apellidos =           ["Perez", "Fernandez", "Gomez"] # 3
# antiguedades =        [15,           5,        20   ] # 3
# legajos =             [435,         250,       673  ] # 3
# codigo_sector_emp =   [1,            2,         1   ] # 3
# codigo_sucursal_emp = [2,            3,         1   ] # 3

# id_sucursal = [   1,     2,        3    ] # 3
# sucursales =  ["CABA", "PBA", "Interior"] # 3

# id_sectores =   [    1,        2   ] # 2
# sectores =      ["Sistemas", "RRHH"] # 2


# print(f'{"Apellido":12} {"Antiguedad":4} {"Legajo":5} {"Sector":10} {"Sucursal":10}')
# print("----------------------------------------------------")
# for i in range(len(apellidos)):
#     for j in range(len(id_sectores)):
#         for k in range(len(sucursales)):
#             if codigo_sucursal_emp[i] == id_sucursal[k]:
#                 if codigo_sector_emp[i] == id_sectores[j]:
#                     print(f'{apellidos[i]:12} {antiguedades[i]:8} {legajos[i]:8} {sectores[j]:10} {sucursales[k]:10}')


