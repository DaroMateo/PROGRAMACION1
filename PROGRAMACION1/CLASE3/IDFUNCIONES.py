variablea= "HOLA"
idvariablea= id(variablea)

variableb= "chau"
idvariableb = id(variableb)

print(f"Id variable a= {idvariablea}")
print(f"Id variable b= {idvariableb}")


def funcion(variable):
    """procesa"""
    variable = variable + 1
    print(f"Id variable= {id(variable)} y el valor es {variable}")
    return variable
"""retorna a la variable(funcion)"""
funcion(variablea)
funcion(variableb)

print(f"Id variable a despues = {idvariablea} y el valor es {variablea}")
print(f"Id variable b despues = {idvariableb} y el valor es {variableb}")    

listaordenada= (1,2,3,4,5)
idvariablea= id(listaordenada)

print(f"Id variable a= {idvariablea}")

def funcion(lista:list):
    lista.append(6)
    print(f"ID lista= {id(lista)} y el valor es {lista}")
    