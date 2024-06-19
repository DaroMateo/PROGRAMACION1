variable_a = 5
id_variable_a = id(variable_a)

variable_b = 10
id_variable_b = id(variable_b)

print(f"Id variable a = {id_variable_a}")
print(f"Id variable b = {id_variable_b}")


def funcion(variable):
    variable = variable + 1
    print(f"Id variable= {id(variable)} y el valor es {variable}")
    return variable

variable_a_2 = funcion(variable_a)
variable_b_2 = funcion(variable_b)

print(f"Id variable a despues = {id_variable_a} y el valor es {variable_a_2}")
print(f"Id variable b despues = {id_variable_b} y el valor es {variable_b_2}")
