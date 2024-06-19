flag = True
contador = 0
clave = int(input("Ingrese clave"))
while clave != 9999 and contador < 2:
    clave = int(input("Error reingrese clave"))
    contador += 1
    if contador == 2 and clave != 9999:
        flag = False

if flag == True:
    print("Bievenido al cajero automatico, elija la operacion a realizar")
else:
    print("Bloqueado")