def identificar_par(num)->str:
    result = "es par" if num %2 == 0 else "NO es par"
    return result
respuesta = identificar_par(3)
print(respuesta)

print((lambda num: "es par" if num %2 == 0 else "NO es par")(3))