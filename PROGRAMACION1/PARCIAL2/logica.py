import pygame
import random
import sys
import json

# Inicializar Pygame
pygame.init()

# Constantes
ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NOMBRE_FUENTE = pygame.font.match_font('arial')
ARCHIVO_PUNTAJES = "puntajes.json"
ARCHIVO_PALABRAS = "palabras.json"
SONIDO_PALABRA_DESCUBIERTA = pygame.mixer.Sound("coin_mario.mp3")
SONIDO_FIN_JUEGO = pygame.mixer.Sound("game_over.mp3")

# Configurar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Ahorcado')

# Cargar palabras
def leer_archivo(archivo):
    with open(archivo, 'r') as archivo:
        ahorcado = json.load(archivo)["ahorcado"]
    return ahorcado

PALABRAS = leer_archivo('ahorcado.json')

# Variables del juego
palabra_seleccionada = None
adivinadas = []
intentos = 6
puntos = 0
fin_juego = False
idioma = None
apodo = ""
entrada_activa = False
copiar_palabras = PALABRAS.copy()
silencio = False  # Bandera de silencio para sonidos

# Cargar y configurar sonidos
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("ringtones-got-theme.mp3")
sonido_fondo.set_volume(0.2)

# Cargar iconos
icono_sonido_encendido = pygame.image.load('unmute.png')
icono_sonido_apagado = pygame.image.load('mute.png')
tamano_icono = 50
posicion_icono = (ANCHO - tamano_icono - 10, 10)  # Esquina superior derecha

# Cargar imagen de fondo
imagen_fondo = pygame.image.load('fondo1.jpg').convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))

# Fuentes
fuente = pygame.font.Font(NOMBRE_FUENTE, 36)

# Constantes de posición
POSICION_TITULO = (ANCHO / 2, 50)
POSICION_PALABRA = (ANCHO / 2, 150)
POSICION_INTENTOS = (ANCHO / 2, 200)
POSICION_PUNTOS = (ANCHO / 2, 250)
POSICION_AHORCADO = (400, 400)
ANCHO_BOTON, ALTO_BOTON = 200, 50
INICIO_BOTON_Y = ALTO / 2 - 100
ESPACIADO_BOTON = 70

# Funciones de dibujo
def dibujar_texto(surf, texto, tamano, x, y, alineacion="center"):
    """
        Una función que representa texto en una superficie en una posición y alineación específicas.

        Args:
        surf: La superficie sobre la que representar el texto.
        texto: El texto en el ultimo proceso.
        tamano: El tamaño de fuente del texto..
        x: La posición de la coordenada x.
        y: la posición de la coordenada y.
        alineacion: La alineación del texto, por defecto es "centro".

        Returns:
            None
    """
    fuente = pygame.font.Font(NOMBRE_FUENTE, tamano)
    superficie_texto = fuente.render(texto, True, BLANCO)
    rectangulo_texto = superficie_texto.get_rect()
    if alineacion == "center":
        rectangulo_texto.midtop = (x, y)
    elif alineacion == "left":
        rectangulo_texto.topleft = (x, y)
    elif alineacion == "right":
        rectangulo_texto.topright = (x, y)
    surf.blit(superficie_texto, rectangulo_texto)

def dibujar_ahorcado(intentos):
    """
    Dibuja al ahorcado según el número de errores restantes.

    Args:
        intentos (int): El número de errores restantes..

    Returns:
        None
    """
    if intentos <= 5:
        pygame.draw.circle(pantalla, BLANCO, POSICION_AHORCADO, 30, 3)  # Cabeza
    if intentos <= 4:
        pygame.draw.rect(pantalla, BLANCO, (POSICION_AHORCADO[0] - 15, POSICION_AHORCADO[1] + 30, 30, 60), 3)  # Torso
    if intentos <= 3:
        pygame.draw.line(pantalla, BLANCO, (POSICION_AHORCADO[0], POSICION_AHORCADO[1] + 30), (POSICION_AHORCADO[0] - 50, POSICION_AHORCADO[1] + 80), 3)  # Brazo Izquierdo
    if intentos <= 2:
        pygame.draw.line(pantalla, BLANCO, (POSICION_AHORCADO[0], POSICION_AHORCADO[1] + 30), (POSICION_AHORCADO[0] + 50, POSICION_AHORCADO[1] + 80), 3)  # Brazo Derecho
    if intentos <= 1:
        pygame.draw.line(pantalla, BLANCO, (POSICION_AHORCADO[0], POSICION_AHORCADO[1] + 90), (POSICION_AHORCADO[0] - 50, POSICION_AHORCADO[1] + 150), 3)  # Pierna Izquierda
    if intentos <= 0:
        pygame.draw.line(pantalla, BLANCO, (POSICION_AHORCADO[0], POSICION_AHORCADO[1] + 90), (POSICION_AHORCADO[0] + 50, POSICION_AHORCADO[1] + 150), 3)  # Pierna Derecha

# Función de selección de idioma
def seleccionar_idioma():
    """
    Selecciona el idioma del juego mostrando un mensaje en la pantalla. El usuario puede seleccionar inglés ('E') o español ('S').

    Esta función utiliza una variable global 'idioma' para almacenar el idioma seleccionado. El idioma está configurado en 'EN' para inglés y 'ES' para español.
    Parameters:
        None
    
    Returns:
        None
    """
    global idioma #se usa dentro de una función para referirse a una variable que está definida fuera de la función, es decir, en el ámbito global del módulo. Esto permite modificar la variable global desde dentro de la función.
    seleccionando = True
    while seleccionando:
        pantalla.blit(imagen_fondo, (0, 0))  # Dibujar imagen de fondo
        dibujar_texto(pantalla, "Seleccione Idioma", 48, ANCHO / 2, 100)
        dibujar_texto(pantalla, "Presione 'E' para inglés o 'S' para español", 36, ANCHO / 2, 200)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando se cierra la ventana
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    idioma = 'EN'
                    seleccionando = False
                elif event.key == pygame.K_s:
                    idioma = 'ES'
                    seleccionando = False

# Función para traducir texto según el idioma seleccionado
def traducir(clave):
    """
    Traduce una clave determinada a su valor correspondiente en un diccionario según el idioma seleccionado.

    Args:
        clave (str): La clave a traducir.

    Returns:
        str: El valor traducido correspondiente a la clave dada. Si el idioma no es compatible, la clave se devuelve tal cual.
    """
    if idioma == 'EN':
        traducciones = {
            "Seleccione Idioma": "Select Language",
            "Presione 'E' para inglés o 'S' para español": "Press 'E' for English or 'S' for Spanish",
            "Ingrese Apodo:": "Enter Nickname:",
            "Palabra:": "Word:",
            "Intentos Restantes:": "Attempts Left:",
            "Puntos:": "Points:",
            "Juego del Ahorcado": "Hangman Game",
            "Jugar": "Play",
            "Salir": "Quit",
            "Puntaje": "Scores"
        }
    elif idioma == 'ES':
        traducciones = {
            "Seleccione Idioma": "Seleccione Idioma",
            "Presione 'E' para inglés o 'S' para español": "Presione 'E' para inglés o 'S' para español",
            "Ingrese Apodo:": "Ingrese Apodo:",
            "Palabra:": "Palabra:",
            "Attempts Left:": "Intentos Restantes:",
            "Points:": "Puntos:",
            "Hangman Game": "Juego del Ahorcado",
            "Play": "Jugar",
            "Quit": "Salir",
            "Scores": "Puntaje"
        }
    else:
        return clave  # Devolver la clave si el idioma no está soportado

    return traducciones.get(clave, clave)  # Devolver texto traducido o la clave misma si no se encuentra

# Función de entrada de apodo
def entrada_apodo():
    """
    Entrada de apodo interactiva utilizando pygame.

    Esta función muestra una caja de entrada de texto en la pantalla para que el usuario ingrese un apodo.
    Si el apodo ya está configurado, la función se salta.

    La función utiliza pygame para manejar los eventos de entrada del usuario. Si el usuario cierra la ventana,
    se sale del programa. Si el usuario hace clic dentro de la caja de entrada, se activa o desactiva el estado
    de entrada. Si el usuario presiona la tecla Enter, se guarda el texto ingresado como apodo y se sale de la
    función. Si el usuario presiona la tecla Backspace, se elimina el último carácter del texto ingresado.
    Si el usuario presiona cualquier otra tecla, se agrega el carácter correspondiente al texto ingresado.

    La función dibuja la imagen de fondo, muestra el texto "Ingrese Apodo:" en la pantalla y muestra el texto ingresado
    en la caja de entrada. La caja de entrada se ajusta automáticamente al ancho del texto ingresado.

    No hay parámetros de entrada.

    No hay valor de retorno.
    """
    global apodo, entrada_activa #se usa dentro de una función para referirse a una variable que está definida fuera de la función, es decir, en el ámbito global del módulo. Esto permite modificar la variable global desde dentro de la función.
    if apodo:
        return  # Si el apodo ya está configurado, saltar la entrada

    entrada_activa = True
    caja_entrada = pygame.Rect(ANCHO / 2 - 100, ALTO / 2 - 25, 200, 50)
    color_inactivo = pygame.Color('lightskyblue3')
    color_activo = pygame.Color('dodgerblue2')
    color = color_inactivo
    activo = False
    texto = ''
    hecho = False

    while not hecho:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando se cierra la ventana
            if event.type == pygame.MOUSEBUTTONDOWN:
                if caja_entrada.collidepoint(event.pos):
                    activo = not activo
                else:
                    activo = False
                color = color_activo if activo else color_inactivo
            if event.type == pygame.KEYDOWN:
                if activo:
                    if event.key == pygame.K_RETURN:
                        apodo = texto
                        hecho = True
                        entrada_activa = False
                    elif event.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                    else:
                        texto += event.unicode

        pantalla.blit(imagen_fondo, (0, 0))  # Dibujar imagen de fondo
        dibujar_texto(pantalla, traducir("Ingrese Apodo:"), 48, ANCHO / 2, ALTO / 2 - 100)
        superficie_txt = fuente.render(texto, True, color)
        ancho = max(200, superficie_txt.get_width() + 10)
        caja_entrada.w = ancho
        pantalla.blit(superficie_txt, (caja_entrada.x + 5, caja_entrada.y + 5))
        pygame.draw.rect(pantalla, color, caja_entrada, 2)
        pygame.display.flip()

# Función para crear botones
def dibujar_boton(texto, x, y, ancho, alto, color_inactivo, color_activo, accion=None):
    """
    Dibuja un botón en la pantalla con el texto y las dimensiones especificadas.

    Parameters:
    - texto: El texto que se mostrará en el botón.
    - x: La coordenada x de la esquina superior izquierda del botón.
    - y: La coordenada y de la esquina superior izquierda del botón.
    - ancho: El ancho del botón.
    - alto: La altura del botón.
    - color_inactivo: El color del botón cuando está inactivo.
    - color_activo: El color del botón cuando está activo.
    - accion: La función que se ejecutará cuando se haga clic en el botón (el valor predeterminado es None).

    Returns:
    Esta función no devuelve ningún valor.
    """
    raton = pygame.mouse.get_pos()
    clic = pygame.mouse.get_pressed()

    if x < raton[0] < x + ancho and y < raton[1] < y + alto:
        pygame.draw.rect(pantalla, color_activo, (x, y, ancho, alto))
        if clic[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color_inactivo, (x, y, ancho, alto))

    dibujar_texto(pantalla, texto, 36, x + (ancho / 2), y + (alto / 2) - 18)

# Función para guardar puntajes
def guardar_puntajes(nuevo_puntaje):
    """
    función para guardar una nueva partitura en un archivo. Si el archivo existe, carga los datos,
    agrega la nueva puntuación y la guarda. Si el archivo no existe, se inicializa
    los datos con una lista vacía de puntuaciones y guarda la nueva puntuación.
    Parameters:
        nuevo_puntaje: La nueva puntuación que se guardará.
    Returns:
        Esta función no devuelve ningún valor.
    """
    existe_archivo = True
    carpeta = "PARCIAL2"
    ruta_completa = carpeta + "/" + ARCHIVO_PUNTAJES
    if existe_archivo(ruta_completa):
        with open(ruta_completa, 'r') as archivo:
            datos = json.lARCHIVO_PUNTAJESoad(archivo)
    else:
        datos = {"puntajes": []}  # Si el archivo no existe, inicializar con una lista vacía de puntajes

    datos["puntajes"].append(nuevo_puntaje)  # Agregar el nuevo puntaje a la lista de puntajes

    with open(ARCHIVO_PUNTAJES, 'w') as archivo:
        json.dump(datos, archivo, indent=4)  # Guardar los datos actualizados en el archivo JSON

def cargar_puntajes():
    """
    Cargue las puntuaciones más altas desde el archivo JSON especificado por ARCHIVO_PUNTAJES.

    Returns:
        Una lista de diccionarios que representan las puntuaciones más altas, donde cada diccionario contiene las claves "apodo" y "puntos".
        Si el archivo no existe o está vacío, se devuelve una lista vacía.
    """
    with open(ARCHIVO_PUNTAJES, 'r') as archivo:
        contenido = archivo.read()
        if contenido:
            datos = json.loads(contenido)
            return datos.get("puntajes", [])
    return []

# Función para mostrar ranking
def mostrar_ranking():
    """
    Una función para mostrar la clasificación de los 5 mejores puntajes, incluida la visualización de apodos y puntos de los jugadores.
    """

    puntajes = cargar_puntajes()
    puntajes = sorted(puntajes, key=lambda x: x['puntos'], reverse=True)[:5]  # Top 5 puntajes

    pantalla.blit(imagen_fondo, (0, 0))

    dibujar_texto(pantalla, traducir("Puntajes Más Altos"), 48, ANCHO / 2, 20)
    desplazamiento_y = 150
    for puntaje in puntajes:
        dibujar_texto(pantalla, f"{puntaje['apodo']}: {puntaje['puntos']}", 36, ANCHO / 2, desplazamiento_y)
        desplazamiento_y += 50

    dibujar_boton(traducir("Salir"), 50, 50, 120, 50, (50, 50, 255), (100, 100, 255), menu_principal)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando se cierra la ventana
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_raton = pygame.mouse.get_pos()
                if 50 < pos_raton[0] < 170 and 50 < pos_raton[1] < 100:
                    menu_principal()  # Volver al menú principal si se hace clic en "Salir"

# Función para iniciar el juego
def iniciar_juego():
    """
    Inicia un nuevo juego.

    Esta función reinicia las variables del juego y llama a la función `juego_principal()`.
    """
    global idioma, copiar_palabras, puntos #se usa dentro de una función para referirse a una variable que está definida fuera de la función, es decir, en el ámbito global del módulo. Esto permite modificar la variable global desde dentro de la función.

    seleccionar_idioma()

    # Reiniciar variables del juego
    copiar_palabras = PALABRAS.copy()
    puntos = 0  # Reiniciar puntos para un nuevo juego
    juego_principal()

# Función del menú principal
def menu_principal():
    """
    Muestra el menú principal del juego y permite al jugador seleccionar opciones como iniciar un nuevo juego, ver el marcador o salir del juego.

    Esta función inicializa las variables globales del juego e inicia el bucle del juego. Actualiza continuamente la pantalla con la imagen de fondo del juego y muestra el título del juego. También dibuja botones para iniciar un nuevo juego, ver el marcador y salir del juego. Además, dibuja un ícono para activar o desactivar el sonido del juego.

    Parameters:
    None

    Returns:
    None
    """
    global idioma #se usa dentro de una función para referirse a una variable que está definida fuera de la función, es decir, en el ámbito global del módulo. Esto permite modificar la variable global desde dentro de la función.

    # Reproducir música de fondo
    sonido_fondo.play(loops=-1)

    ejecutando = True
    while ejecutando:
        pantalla.blit(imagen_fondo, (0, 0))  # Dibujar imagen de fondo
        dibujar_texto(pantalla, traducir("Juego del Ahorcado"), 48, POSICION_TITULO[0], POSICION_TITULO[1])

        # Dibujar botones
        dibujar_boton(traducir("Jugar"), ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200), iniciar_juego)
        dibujar_boton(traducir("Puntaje"), ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y + ESPACIADO_BOTON, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200), mostrar_ranking)
        dibujar_boton(traducir("Salir"), ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y + 2 * ESPACIADO_BOTON, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200), pygame.quit)

        # Dibujar ícono de sonido
        if silencio:
            pantalla.blit(pygame.transform.scale(icono_sonido_apagado, (tamano_icono, tamano_icono)), posicion_icono)
        else:
            pantalla.blit(pygame.transform.scale(icono_sonido_encendido, (tamano_icono, tamano_icono)), posicion_icono)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando se cierra la ventana
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if posicion_icono[0] < event.pos[0] < posicion_icono[0] + tamano_icono and posicion_icono[1] < event.pos[1] < posicion_icono[1] + tamano_icono:
                    alternar_sonido()  # Alternar sonido cuando se hace clic en el ícono

# Función principal del bucle de juego
def juego_principal():
    """
    Bucle de juego principal para el juego Hangman. Gestiona la lógica del juego, la entrada del usuario y el estado del juego para jugar.
    Maneja la selección de una palabra aleatoria de una lista, la entrada del usuario para adivinar letras, actualiza el estado del juego en función de las conjeturas,
    y dibujar los elementos del juego en la pantalla.
    Gestiona la puntuación final, guarda la puntuación y sale del juego cuando es necesario.
    """
    global palabra_seleccionada, adivinadas, intentos, puntos, fin_juego, copiar_palabras  #se usa dentro de una función para referirse a una variable que está definida fuera de la función, es decir, en el ámbito global del módulo. Esto permite modificar la variable global desde dentro de la función.

    if not copiar_palabras:
        dibujar_texto(pantalla, f"Puntaje Final para {apodo}: {puntos}", 48, ANCHO / 2, ALTO / 2)
        pygame.display.flip()
        pygame.time.wait(3000)
        guardar_puntajes({"apodo": apodo, "puntos": puntos})  # Guardar el puntaje final
        pygame.quit()
        sys.exit()  # Salir del programa después de mostrar el puntaje final

    palabra_seleccionada = random.choice([palabra[idioma] for palabra in copiar_palabras])
    copiar_palabras = [palabra for palabra in copiar_palabras if palabra[idioma] != palabra_seleccionada]
    adivinadas = ['_' for _ in palabra_seleccionada]
    intentos = 6
    fin_juego = False

    while True:
        pantalla.blit(imagen_fondo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando se cierra la ventana
            elif event.type == pygame.KEYDOWN and not fin_juego and not entrada_activa:
                if event.unicode.isalpha():
                    caracter = event.unicode.lower()
                    if caracter in palabra_seleccionada:
                        for i in range(len(palabra_seleccionada)):
                            if palabra_seleccionada[i] == caracter:
                                adivinadas[i] = caracter
                                puntos += 1
                    else:
                        intentos -= 1

        if intentos == 0 or '_' not in adivinadas:
            fin_juego = True
            if "_" not in adivinadas:
                SONIDO_PALABRA_DESCUBIERTA.play()  # Reproducir sonido al descubrir una letra
            else:
                SONIDO_FIN_JUEGO.play()  

        # Dibujar elementos
        dibujar_texto(pantalla, "Juego del Ahorcado", 48, *POSICION_TITULO)
        dibujar_texto(pantalla, f"Palabra: {' '.join(adivinadas)}", 36, *POSICION_PALABRA)
        dibujar_texto(pantalla, f"Intentos Restantes: {intentos}", 36, *POSICION_INTENTOS)
        dibujar_texto(pantalla, f"Puntos: {puntos}", 36, *POSICION_PUNTOS)
        dibujar_ahorcado(intentos)

        if fin_juego:
            pygame.time.wait(1000)
            juego_principal()

        if silencio:
            pantalla.blit(pygame.transform.scale(icono_sonido_apagado, (tamano_icono, tamano_icono)), posicion_icono)
        else:
            pantalla.blit(pygame.transform.scale(icono_sonido_encendido, (tamano_icono, tamano_icono)), posicion_icono)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando se cierra la ventana
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if posicion_icono[0] < event.pos[0] < posicion_icono[0] + tamano_icono and posicion_icono[1] < event.pos[1] < posicion_icono[1] + tamano_icono:
                    alternar_sonido()  # Alternar sonido cuando se hace clic en el ícono
        pygame.display.flip()

    pygame.quit()

# Función para alternar el sonido
def alternar_sonido():
    """
    Activa o desactiva el sonido.

    Esta función alterna la variable global `silencio` entre `Verdadero` y `Falso`.
    Si `silencio` es `True`, el sonido `sonido_fondo` se detiene.
    Si `silencio` es `False`, el sonido `sonido_fondo` se reproduce indefinidamente.

    Parameters:
        None

    Returns:
        None
    """
    global silencio #se usa dentro de una función para referirse a una variable que está definida fuera de la función, es decir, en el ámbito global del módulo. Esto permite modificar la variable global desde dentro de la función.
    silencio = not silencio
    if silencio:
        sonido_fondo.stop()
    else:
        sonido_fondo.play(-1)  # Reproducir el sonido indefinidamente

'''# Iniciar el juego
seleccionar_idioma()
entrada_apodo()
menu_principal()'''