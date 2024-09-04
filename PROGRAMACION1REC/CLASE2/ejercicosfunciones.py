'''Desarrollar una función que reciba una patente que tendrá tres letras y tres números o tres números y tres
letras. Deberá retornar auto o moto, si la patente es tres letras y tres números o tres números y tres letras
respectivamente.'''
'''
def tipo_de_vehiculo(patente) -> str:

    
    #Recibe una patente y devuelve "Auto" si la patente tiene letras y numeros, o "Moto" si tiene solo numeros y letras.
    
    for i in patente:
        #if  i>= 'a' and i <= 'z' or i>= 'A' and i <= 'Z':
        if ord(i) >= 65 and ord(i) <= 90:
            resultado = "Auto"
        else:
            resultado = "Moto"
        break
    return resultado
'''

'''resultado = tipo_de_vehiculo("ABC123")
print(resultado)'''

'''Desarrollar una función que reciba como parámetros fecha actual y fecha de nacimiento; y retorne la edad.'''

'''def calcular_edad(fecha_actual, fecha_nacimiento):
    """
    Calcula la edad basándose en la fecha actual y la fecha de nacimiento.
    
    :param fecha_actual: Tupla (año_actual, mes_actual, dia_actual)
    :param fecha_nacimiento: Tupla (año_nacimiento, mes_nacimiento, dia_nacimiento)
    :return: Edad en años
    """
    año_actual, mes_actual, dia_actual = fecha_actual
    año_nacimiento, mes_nacimiento, dia_nacimiento = fecha_nacimiento
    
    # Calcular edad básica
    edad = año_actual - año_nacimiento
    
    # Ajustar edad si el cumpleaños aún no ha ocurrido este año
    if (mes_actual < mes_nacimiento) or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
        edad -= 1

    return edad'''

# Ejemplos de uso
#print(calcular_edad((2024, 8, 28), (2000, 8, 27)))

'''Desarrollar una función que reciba como parametros numero de DNI y
[MASCULINO|FEMENINO|EMPRESA]. Deberá retornar el CUIL/CUIT formado por:
CUIL/T: Son 11 números en total:
XY – 12345678 – Z
XY: Indican el tipo (Masculino, Femenino o una empresa)
12345678: Número de DNI
Z: Código Verificador'''

def convertir_dni_a_8_digitos(dni):
    dni_str = str(dni)
    longitud_dni = len(dni_str)

    # Si el DNI tiene menos de 8 dígitos, agregar ceros al inicio
    if longitud_dni < 8:
        ceros_a_agregar = 8 - longitud_dni
        dni_str_completo = ""
        for _ in range(ceros_a_agregar):
            dni_str_completo += "0"  # Agregar ceros al principio
        dni_str_completo += dni_str  # Añadir el DNI original
    else:
        dni_str_completo = dni_str

    return dni_str_completo

def calcular_suma_xy(xy, dni_str):
    # Definir los multiplicadores para cada dígito
    multiplicadores = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    
    # Convertir XY a una cadena para tratar los dígitos por separado
    xy_str = str(xy)
    
    # Iniciar la suma xy
    suma = 0
    
    # Usar un for para multiplicar cada dígito correspondiente por su multiplicador
    for i in range(len(multiplicadores)):
        if i < 2:
            # Para los primeros dos dígitos, usamos los dígitos de XY
            suma += int(xy_str[i]) * multiplicadores[i]
        else:
            # Para los siguientes, usamos los dígitos del DNI
            suma += int(dni_str[i - 2]) * multiplicadores[i]
    
    return suma

def calcular_cuil_cuit(dni, tipo):
    # Paso 1: Determinar XY según el tipo
    if tipo == 'MASCULINO':
        xy = 20
    elif tipo == 'FEMENINO':
        xy = 27
    elif tipo == 'EMPRESA':
        xy = 30
    else:
        print("Tipo no válido. Debe ser 'MASCULINO' o 'FEMENINO' o 'EMPRESA'.")
    
    # Convertir el DNI a una cadena para asegurarnos de que tiene 8 dígitos
    dni_str = convertir_dni_a_8_digitos(dni)

    # Paso 2: Multiplicar XY y cada dígito del DNI por los valores especificados
    suma = calcular_suma_xy(xy, dni_str)

    # Paso 3: Obtener el resto de la división entre la suma y 11
    resto = suma % 11

    # Paso 4: Determinar el código verificador Z
    if resto == 0:
        z = 0
    elif resto == 1:
        if tipo == 'MASCULINO':
            z = 9
            xy = 23
        elif tipo == 'FEMENINO':
            z = 4
            xy = 23
        elif tipo == 'EMPRESA':
            z = 6
            xy = 30
    else:
        z = 11 - resto

    # Paso 5: Formar el CUIL/CUIT
    cuil_cuit = f"{xy}-{dni_str}-{z}"

    return cuil_cuit

# Solicitar el DNI y el sexo del usuario
dni = input("Ingresa tu DNI (sin puntos): ")
sexo = input("Ingresa tu sexo (MASCULINO / FEMENINO/ EMPRESA): ").upper()

# Validar que el DNI es un número y el sexo es correcto
if not dni.isdigit():
    print("El DNI debe ser un número.")
elif sexo not in ['MASCULINO', 'FEMENINO' , 'EMPRESA']:
    print("El sexo ingresado no es válido.")
else:
    # Calcular y mostrar el CUIL/CUIT
    cuil_cuit = calcular_cuil_cuit(int(dni), sexo)
    print(f"Tu CUIL/CUIT es: {cuil_cuit}")