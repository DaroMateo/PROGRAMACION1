def tipo_de_vehiculo(patente) -> str:
    
    """
    Recibe una patente que tendra tres letras y tres numeros o tres numeros y tres letras.
    Debera retornar "Auto" si la patente tiene letras y numeros, o "Moto" si tiene solo numeros y letras.
    """
    
    for i in patente:
        #if  i>= 'a' and i <= 'z' or i>= 'A' and i <= 'Z':
        if ord(i) >= 65 and ord(i) <= 90:
            resultado = "Auto"
        else:
            resultado = "Moto"
        break
    return resultado

def calcular_edad(fecha_actual, fecha_nacimiento):
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

    return edad

def convertir_dni_a_8_digitos(dni):
    
    """
    Convierte un DNI a una cadena de 8 caracteres, rellenando con ceros a la izquierda si es necesario.

    :param dni: Número de DNI
    :return: Cadena de 8 caracteres con el DNI
    """
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
    
    """
    Calcula la suma XY de un CUIL/CUIT.
    
    Parameters
    ----------
    xy : int
        Número de 2 dígitos que indica el tipo de CUIL/CUIT.
    dni_str : str
        Número de DNI como cadena.
    
    Returns
    -------
    int
        Suma de los productos de cada dígito de XY con cada dígito del DNI.
    """
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

def calcular_cuil_cuit(dni: str, tipo: str)-> str:
    
    # Paso 1: Determinar XY según el tipo
    """
    Calcula el CUIL/CUIT de una persona.

    Parameters
    ----------
    dni : int
        Número de DNI.
    tipo : str
        Tipo de CUIL/CUIT. Puede ser 'MASCULINO', 'FEMENINO' o 'EMPRESA'.

    Returns
    -------
    str
        CUIL/CUIT formado por XY-DNI-Z, donde XY indica el tipo, DNI es el número de DNI y Z es el código verificador.
    """

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

def medir_cadena(cadena:str)->int:
    """
    Calcula el largo de una cadena de caracteres

    Parameters
    ----------
    cadena : str
        La cadena de caracteres a evaluar

    Returns
    -------
    int
        El largo de la cadena
    """
    contador = 0
    for _ in cadena: # el _ es un placeholder, no se usa en este caso
        contador += 1
    return contador

def completar_dni(cadena:str)->str:
    """
    Completa el dni de una persona

    Parameters
    ----------
    cadena : str
        La cadena de caracteres a evaluar

    Returns
    -------
    str
        La cadena con el dni completado
    """
    if  medir_cadena(cadena)<=8:
        for _ in range(medir_cadena(cadena),8):
            cadena = '0' + cadena
    return cadena

def verificar_dni(cadena:str)->bool:
    """
    Determina si una cadena de caracteres es un dni

    Parameters
    ----------
    cadena : str
        La cadena de caracteres a evaluar

    Returns
    -------
    bool
        True si la cadena es un dni, False de lo contrario
    """
    retorno = True
    if medir_cadena(cadena) <= 6 and medir_cadena(cadena) >= 8:
        retorno = False
    return retorno