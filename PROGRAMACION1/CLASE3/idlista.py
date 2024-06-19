lista_ordena = [1, 2, 3, 4, 5]
id_variable_a = id(lista_ordena)

print(f"Id lista_ordena a = {id_variable_a}")

def funcion(lista:list):
    lista.append(6)
    print(f"Id lista= {id(lista)} y el valor es {lista}")

funcion(lista_ordena)

print(f"Id lista_ordena a despues = {id_variable_a} y el valor es {lista_ordena}")
