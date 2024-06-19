"""Enunciado:
De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos
Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso ( entre 100 y 800)
Tipo de material ( aluminio, hierro , madera)
Costo en $ (mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue tipo de material más usado ( aluminio, hierro , madera)
Informe B- El porcentaje de contenedores de Categoría peligroso
Informe C- La marca y tipo del contenedor más pesado
Informe D- La marca del contenedor de comestible con menor costo
Informe E- El promedio de costo de todos los contenedores de HIerro"""

contenedores = 1
contador_aluminio = 0
contador_hierro = 0
contador_madera = 0
contador_peligroso = 0
flag = True
contenedor_mas_pesado = None
marca_mas_pesada = None
tipo_mas_pesado = None
flag_menor_costo = True
marca_menor_costo = None
contenedor_menor_costo = None
acumulador_costo_hierro = 0





for i in range (contenedores):
    
    marca_contenedor = input("Ingrese la marca: ")

    categoria = input("Ingrese una categoría: ")

    while categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria":
        categoria = input("Error- Reingrese una categoría: ")

    peso = input("Ingrese un peso en kg: ")
    peso = int(peso)
    
    while peso == None or peso == "" or (peso < 100 or peso > 800):
        peso = input("Reingrese un peso en kg: ")
        peso = int(peso)

    tipo_material = input("Ingrese un material: ")

    while tipo_material != "aluminio" and tipo_material != "hierro" and tipo_material != "madera":
        tipo_material = input("Error- Reingrese un material: ")

    costo = input("Ingrese el costo: ")
    costo = int(costo)

    while costo < 1:
        costo = input("Error-Reingrese el costo: ")
        costo = int(costo)

#informe A tipo de material más usado
    match(tipo_material):
        case("aluminio"):
            contador_aluminio += 1

        case("hierro"):
            contador_hierro += 1
            acumulador_costo_hierro += costo
        case _:
            contador_madera += 1
    
    if(categoria == "peligroso"):
        contador_peligroso += 1

    if flag == True:
        contenedor_mas_pesado = peso
        marca_mas_pesada = marca_contenedor
        tipo_mas_pesado = tipo_material
        flag = False
    else:
        if(peso > contenedor_mas_pesado):
            marca_mas_pesada = marca_contenedor
            tipo_mas_pesado = tipo_material
            contenedor_mas_pesado = peso

    if categoria == "comestible":
        if flag_menor_costo == True:
            flag_menor_costo = False
            marca_menor_costo = marca_contenedor
            contenedor_menor_costo = costo
        else:
            if(costo < contenedor_menor_costo):
                marca_menor_costo = marca_contenedor
                contenedor_menor_costo = costo




if(contador_aluminio > contador_hierro and contador_aluminio > contador_madera):
    material_mas_usado = "aluminio"
elif(contador_hierro > contador_madera):
    material_mas_usado = "hierro"
else:
    material_mas_usado = "madera"

porcentaje_peligroso = (contador_peligroso * 100)  / contenedores

if contador_hierro > 0:
    promedio_costo_hierro = (acumulador_costo_hierro / contador_hierro)
else:
    promedio_costo_hierro = 0

mensaje = f"tipo de material más usado: {material_mas_usado}\nporcentaje contenedor peligroso: {porcentaje_peligroso} %\nmarca y tipo contenedor más pesado:{marca_mas_pesada} // {contenedor_mas_pesado}\nmarca contenedor comestible con menor costo:{marca_menor_costo}\npromedio costo contenedores de hierro:{promedio_costo_hierro:.2f}"

print(mensaje)



    
