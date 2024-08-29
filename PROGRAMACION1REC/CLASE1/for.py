# 1 solo parametro -> fin | inicio = 0, paso = +1
mi_rango = range(5) # 0, 1, 2, 3, 4
print(mi_rango)
mi_lista = list(mi_rango) # [0, 1, 2, 3, 4]
print(mi_lista)

#2 parametros -> fin | inicio, fin
mi_rango_b = range(2, 7) # 2, 3, 4, 5, 6
mi_lista_b = list(mi_rango_b) # [2, 3, 4, 5, 6]
print(mi_lista_b)

# 3 parametros -> fin | inicio, fin, paso
mi_rango_c = range(15, 5, -1) # 15, 14, 13, 12, 11, 10, 9, 8, 7
mi_lista_c = list(mi_rango_c) # [15, 14, 13, 12, 11, 10, 9, 8, 7]
print(mi_lista_c)

for numero in mi_rango:
    print(numero)

for numero in mi_lista:
    print(numero)