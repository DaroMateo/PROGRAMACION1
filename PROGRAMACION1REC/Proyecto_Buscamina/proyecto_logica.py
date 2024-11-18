import pygame
import random
import sys
import json

# Constantes
ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NOMBRE_FUENTE = pygame.font.match_font("Arial Narrow")
ARCHIVO_PUNTAJES = "puntajesbuscamina.json"
# SONIDO_PALABRA_DESCUBIERTA = pygame.mixer.Sound("coin_mario.mp3")
# SONIDO_FIN_JUEGO = pygame.mixer.Sound("game_over.mp3")
# Colores
COLOR_BOTON = (0, 200, 0)
COLOR_TEXTO = (255, 255, 255)
COLOR_CASILLA = (200, 200, 200)
COLOR_CASILLA_DESCUBIERTA = (150, 150, 150)
COLOR_BANDERA = (255, 0, 0)


pygame.init()
pygame.mixer.init()


# Variables del juego
puntos = 0
fin_juego = False
apodo = ""
entrada_activa = False
silencio = False  # Bandera de silencio para sonidos

# Cargar y configurar sonidos
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("ringtones-got-theme.mp3")
sonido_fondo.set_volume(0.2) # Configurar volumen set_volume es la cantidad de sonido que se reproduce, 0.2 es el porcentaje de volumen que se reproduce

# Cargar iconos
icono_sonido_encendido = pygame.image.load('unmute.png')
icono_sonido_apagado = pygame.image.load('mute.png')
tamano_icono = 50
posicion_icono = (ANCHO - tamano_icono - 10, 10)  # Esquina superior derecha

# Cargar imagen de fondo
imagen_fondo = pygame.image.load('fondo1.jpg')
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))

# Fuentes
fuente = pygame.font.Font(NOMBRE_FUENTE, 36)  # Tamaño de la fuente de texto (36 pixeles) 
fuente_pequena = pygame.font.SysFont(None, 36)

# Configurar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('BUSCAMINAS')

# Constantes de posición
POSICION_TITULO = (ANCHO / 2, 50) # Centrar el texto en la pantalla, 2 ,50 son las coordenadas
POSICION_PUNTOS = (ANCHO / 2, 250) # Centrar el texto en la pantalla, 2, 250 son las coordenadas
ANCHO_BOTON, ALTO_BOTON = 200, 50 # Tamaño de los botones
INICIO_BOTON_Y = ALTO / 2 - 100 # Posición inicial de los botones
ESPACIADO_BOTON = 70 # Espaciado entre botones

#Configuracion de matriz 

def crear_matriz_buscamina(filas, columnas, num_minas):
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    minas_colocadas = 0
    while minas_colocadas < num_minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if matriz[fila][columna] != -1:
            matriz[fila][columna] = -1
            minas_colocadas += 1
    for fila in range(filas):
        for columna in range(columnas):
            if matriz[fila][columna] == -1:
                continue
            for i in range(max(0, fila - 1), min(filas, fila + 2)):
                for j in range(max(0, columna - 1), min(columnas, columna + 2)):
                    if matriz[i][j] == -1:
                        matriz[fila][columna] += 1
    return matriz

def modificar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                contiguas = 0
                for k in range(max(0, i - 1), min(len(matriz), i + 2)):
                    for l in range(max(0, j - 1), min(len(matriz[0]), j + 2)):
                        if matriz[k][l] == -1:
                            contiguas += 1
                if contiguas > 0:
                    matriz[i][j] = contiguas
    return matriz

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
    fuente = pygame.font.Font(NOMBRE_FUENTE, tamano) # Cargar fuente de texto en la superficie en el tamanio indicado 
    superficie_texto = fuente.render(texto, True, BLANCO) # Rerpesenta el texto en la superficie
    rectangulo_texto = superficie_texto.get_rect() # Crea un rectángulo que cubre el texto
    if alineacion == "center": # Si la alineación es "centro" 
        rectangulo_texto.midtop = (x, y) # El rectángulo se centra en la superficie, .midtop representa el punto medio superior del rectángulo 
    elif alineacion == "left": # Si la alineación es "izquierda"
        rectangulo_texto.topleft = (x, y) 
    elif alineacion == "right": # Si la alineación es "derecha"
        rectangulo_texto.topright = (x, y)
    surf.blit(superficie_texto, rectangulo_texto) # Rellena el rectángulo con el texto

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
    - pygame.Rect: El rectángulo que define el área del botón.
    """
    raton = pygame.mouse.get_pos()  # Obtener la posición del ratón
    clic = pygame.mouse.get_pressed()  # Obtener el estado del clic

    rect_boton = pygame.Rect(x, y, ancho, alto)  # Crear un rectángulo para el botón

    if rect_boton.collidepoint(raton):  # Determinar si el ratón está sobre el botón
        pygame.draw.rect(pantalla, color_activo, rect_boton)  # Botón activo
        if clic[0] == 1 and accion is not None:  # Si se hace clic y hay acción
            accion()
    else:
        pygame.draw.rect(pantalla, color_inactivo, rect_boton)  # Botón inactivo

    dibujar_texto(pantalla, texto, 36, rect_boton.centerx, rect_boton.centery - 18)

    return rect_boton  # Retornar el rectángulo del botón

#Configuracion de niveles

def seleccionar_nivel():
    while True: 
        pantalla.blit(imagen_fondo, (0, 0))
        boton_facil = dibujar_boton("Facil", ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y - ESPACIADO_BOTON, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200))
        boton_medio = dibujar_boton("Medio", ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200))
        boton_dificil = dibujar_boton("Difícil", ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y + ESPACIADO_BOTON, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200))

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if boton_facil.collidepoint(event.pos): 
                    return (8, 8, 10) # Facil: 8x8 con 10 minas 
                elif boton_medio.collidepoint(event.pos): 
                    return (16, 16, 40) # Medio: 16x16 con 40 minas 
                elif boton_dificil.collidepoint(event.pos): 
                    return (30, 30, 100) # Difícil: 24x24 con 99 minas 
        pygame.display.flip()
  
#configuracion de sonido

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
    global silencio #que use la variable que está fuera de la función en lugar de crear una nueva dentro de la función.
    silencio = not silencio
    if silencio:
        sonido_fondo.stop()
    else:
        sonido_fondo.play(-1)  # Reproducir el sonido indefinidamente


#Puntaje

def swap(lista: list, indice_uno: int, indice_dos: int) -> list:
    """
    Swapea los valores de dos índices de una lista.

    Args:
        lista (list): Lista que contiene los valores a intercambiar.
        indice_uno (int): Índice del valor a intercambiar.
        indice_dos (int): Índice del segundo valor a intercambiar.

    Returns:
        list: Retorna la lista con los valores intercambiados.
    """
    auxiliar = lista[indice_uno]
    lista[indice_uno] = lista[indice_dos]
    lista[indice_dos] = auxiliar

    return lista  


def ordenar(lista: list, clave: str, ascendente: bool = True) -> list: 
    """
    Ordena una lista de diccionarios en base a una clave de forma ascendente o descendente.

    Args:
        lista (list): Lista de diccionarios a ordenar.
        clave (str): Clave a usar para ordenar la lista.
        ascendente (bool, opcional): Declara si la lista se ordena de forma ascendente o descendente. 
                                     Se le asigna False para ordenar de forma descendente. 
                                     (Si no se pasa ningún valor booleano, ordena de forma ascendente por defecto.)

    Returns:
        list: Retorna la lista de diccionarios ordenada.
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if ascendente and int(lista[i][clave]) > int(lista[j][clave]) or not ascendente and int(lista[i][clave]) < int(lista[j][clave]):
                swap(lista, i, j)
    return lista

def generar_json(nombre: str, lista: list, clave: str):
    """
    Genera un archivo JSON con la lista proporcionada bajo la clave dada.

    Args:
        nombre (str): El nombre del archivo JSON a generar.
        lista (list): La lista de datos a guardar en el archivo JSON.
        clave (str): La clave bajo la cual se guardará la lista en el archivo JSON.
    """
    data = {clave: lista}
    with open(nombre, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def leer_archivo (archivo_nombre:str):
    if len(archivo_nombre) == 0:
        contenido = False  
    else:          
        with open(archivo_nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido
   
def guardar_puntajes(nuevo_puntaje):
    """
    Función para guardar una nueva partitura en un archivo. Si el archivo existe, carga los datos,
    agrega la nueva puntuación y la guarda. Si el archivo no existe, se inicializa
    los datos con una lista vacía de puntuaciones y guarda la nueva puntuación.
    
    Parameters:
        nuevo_puntaje: La nueva puntuación que se guardará.
        
    Returns:
        Esta función no devuelve ningún valor.
    """
    contenido = leer_archivo(ARCHIVO_PUNTAJES)
    if contenido:
        data = json.loads(contenido)
    else:
        data = {"puntajes": []}

    data["puntajes"].append(nuevo_puntaje)
    data["puntajes"] = ordenar(data["puntajes"], clave='puntos', ascendente=False)

    generar_json(ARCHIVO_PUNTAJES, data["puntajes"], "puntajes")

def cargar_puntajes():
    """
    Cargue las puntuaciones más altas desde el archivo JSON especificado por ARCHIVO_PUNTAJES.

    Returns:
        Una lista de diccionarios que representan las puntuaciones más altas, donde cada diccionario contiene las claves "apodo" y "puntos".
        Si el archivo no existe o está vacío, se devuelve una lista vacía.
    """
    with open(ARCHIVO_PUNTAJES, 'r') as file:
        contenido = file.read() # Lee el contenido del archivo JSON y lo almacena en la variable 'contenido'
        if contenido:
            data = json.loads(contenido)
            return data.get("puntajes", [])
    return []

# Función para mostrar ranking
def mostrar_ranking(): 
    """
    Una función para mostrar la clasificación de los 5 mejores puntajes, incluida la visualización de apodos y puntos de los jugadores.
    """

    puntajes = cargar_puntajes()  # Cargar puntajes en orden descendente por puntos 
    puntajes = ordenar(puntajes, clave='puntos', ascendente=False)[:5]  # Top 5 puntajes en orden ascendente

    pantalla.blit(imagen_fondo, (0, 0))

    dibujar_texto(pantalla, ("Puntajes Más Altos"), 48, ANCHO / 2, 20)
    desplazamiento_y = 150
    for puntaje in puntajes:   # Mostrar puntajes en orden descendente por puntos y apodos 
        dibujar_texto(pantalla, f"{puntaje['apodo']}: {puntaje['puntos']}", 36, ANCHO / 2, desplazamiento_y) # Mostrar puntajes en orden descendente por puntos y apodos 
        desplazamiento_y += 50 # +=50 para separar los apodos con los puntajes y mostrarlos en orden descendente por puntos y apodos

    dibujar_boton(("Atras"), 50, 50, 120, 50, (50, 50, 255), (100, 100, 255), menu_principal)

    pygame.display.flip() #.flip actualiza la pantalla

    while True:  # Mostrar puntajes en orden descendente por puntos y apodos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando se cierra la ventana
            elif event.type == pygame.MOUSEBUTTONDOWN: # Mostrar puntajes en orden descendente por puntos y apodos
                pos_raton = pygame.mouse.get_pos() # Mostrar puntajes en orden descendente por puntos y apodos, .get_pos devuelve una tupla (x, y) de la posición del ratón
                if 50 < pos_raton[0] < 170 and 50 < pos_raton[1] < 100:
                    menu_principal()  # Volver al menú principal si se hace clic en "Salir"


#Dibujar tablero

def dibujar_tablero(matriz, descubiertas, banderas, pantalla, fuente_pequena):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Validar dimensiones de matrices auxiliares
    if len(descubiertas) != filas or any(len(descubiertas[fila]) != columnas for fila in range(filas)):
        print("Error: Las dimensiones de 'descubiertas' no coinciden con las de 'matriz'.")
        return

    if len(banderas) != filas or any(len(banderas[fila]) != columnas for fila in range(filas)):
        print("Error: Las dimensiones de 'banderas' no coinciden con las de 'matriz'.")
        return

    tam_casilla = 50
    margen = 10

    for fila in range(filas):
        for columna in range(columnas):
            try:
                # Coordenadas de la celda
                x = columna * (tam_casilla + margen)
                y = fila * (tam_casilla + margen) + 100
                rect = pygame.Rect(x, y, tam_casilla, tam_casilla)

                # Dibujar celda descubierta o cubierta
                if descubiertas[fila][columna]:
                    pygame.draw.rect(pantalla, COLOR_CASILLA_DESCUBIERTA, rect)
                    if matriz[fila][columna] != 0:
                        texto = fuente_pequena.render(str(matriz[fila][columna]), True, COLOR_TEXTO)
                        pantalla.blit(texto, (x + (tam_casilla - texto.get_width()) // 2, y + (tam_casilla - texto.get_height()) // 2))
                else:
                    pygame.draw.rect(pantalla, COLOR_CASILLA, rect)
                    if banderas[fila][columna]:
                        pygame.draw.rect(pantalla, COLOR_BANDERA, rect)

            except IndexError:
                print(f"Error al acceder a fila {fila}, columna {columna}. Revise las dimensiones.")
                return


#Menu y Bucle principal

def iniciar_juego():
    """
    Inicia un nuevo juego de Buscaminas.

    Esta función reinicia las variables del juego y llama a la función `juego_principal()`.
    """
    global matriz, descubiertas, banderas, puntaje  # Que use las variables que están fuera de la función en lugar de crear nuevas dentro de la función.

    # Reiniciar variables del juego
    filas, columnas, num_minas = seleccionar_nivel() 
    matriz = crear_matriz_buscamina(filas, columnas, num_minas)  # Generar una nueva matriz con minas distribuidas aleatoriamente
    descubiertas = [[False for _ in range(8)] for _ in range(8)]  # Reiniciar el estado de las casillas descubiertas
    banderas = [[False for _ in range(8)] for _ in range(8)]  # Reiniciar el estado de las banderas
    puntaje = 0  # Reiniciar el puntaje a 0000

    juego_principal()  # Llamar a la función que maneja el bucle principal del juego


def menu_principal():
    """
    Muestra el menú principal del juego y permite al jugador seleccionar opciones como iniciar un nuevo juego, ver el marcador o salir del juego.

    Esta función inicializa las variables globales del juego e inicia el bucle del juego. Actualiza continuamente la pantalla con la imagen de fondo del juego y muestra el título del juego. También dibuja botones para iniciar un nuevo juego, ver el marcador y salir del juego. Además, dibuja un ícono para activar o desactivar el sonido del juego.

    Parameters:
    None

    Returns:
    None
    """
    global idioma #que use la variable que está fuera de la función en lugar de crear una nueva dentro de la función.

    # Reproducir música de fondo
    sonido_fondo.play(loops=-1)

    ejecutando = True
    while ejecutando:  # Bucle principal del juego 
        pantalla.blit(imagen_fondo, (0, 0))  # Dibujar imagen de fondo
        dibujar_texto(pantalla, "BUSCAMINAS", 48, POSICION_TITULO[0], POSICION_TITULO[1])

        # Dibujar botones
        dibujar_boton("Nivel", ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y - ESPACIADO_BOTON, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200), seleccionar_nivel)
        dibujar_boton("Jugar", ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200), iniciar_juego)
        dibujar_boton("Ver Puntajes", ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y + ESPACIADO_BOTON, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200), mostrar_ranking)
        dibujar_boton("Salir", ANCHO / 2 - ANCHO_BOTON / 2, INICIO_BOTON_Y + 2 * ESPACIADO_BOTON, ANCHO_BOTON, ALTO_BOTON, NEGRO, (200, 200, 200), pygame.quit)

        # Dibujar ícono de sonido
        if silencio:  # Si el sonido esta silenciado, mostrar el ícono de sonido apagado
            pantalla.blit(pygame.transform.scale(icono_sonido_apagado, (tamano_icono, tamano_icono)), posicion_icono)
        else:  # Si el sonido no esta silenciado, mostrar el ícono de sonido encendido
            pantalla.blit(pygame.transform.scale(icono_sonido_encendido, (tamano_icono, tamano_icono)), posicion_icono)

        pygame.display.flip()

        for event in pygame.event.get(): # Manejo de eventos del juego (Click, teclado, etc.)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando se cierra la ventana
            elif event.type == pygame.MOUSEBUTTONDOWN: # Manejo de eventos de click del ratón (Click, teclado, etc.)
                if posicion_icono[0] < event.pos[0] < posicion_icono[0] + tamano_icono and posicion_icono[1] < event.pos[1] < posicion_icono[1] + tamano_icono: # Verificar si el click se encuentra dentro del ícono de sonido (activado o desactivado) y cambiar el estado del silencio a su opuesto 
                    alternar_sonido()  # Alternar sonido cuando se hace clic en el ícono de sonido
                    
def juego_principal():
    global matriz, descubiertas, banderas, puntaje  #que use la variable que está fuera de la función en lugar de crear una nueva dentro de la función.

    filas, columnas, num_minas = seleccionar_nivel() 
    matriz = crear_matriz_buscamina(filas, columnas, num_minas)
    descubiertas = [[False for _ in range(8)] for _ in range(8)]
    banderas = [[False for _ in range(8)] for _ in range(8)]
    puntaje = 0
    fin_juego = False

    while True:
        pantalla.blit(imagen_fondo, (0, 0))

        for event in pygame.event.get():  # Manejar eventos del juego (entradas del usuario, pulsaciones de botones, teclado, etc.)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando se cierra la ventana

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                columna = x // 60
                fila = (y - 100) // 60
                if 0 <= fila < 8 and 0 <= columna < 8:
                    if event.button == 1:  # Clic izquierdo
                        if not banderas[fila][columna]:  # No se puede descubrir si hay una bandera
                            descubiertas[fila][columna] = True
                            if matriz[fila][columna] == -1:
                                print("¡Boom! Has encontrado una mina. Has perdido la partida.")
                                fin_juego = True
                            else:
                                puntaje += 1
                    elif event.button == 3:  # Clic derecho
                        banderas[fila][columna] = not banderas[fila][columna]

                if boton_reiniciar.collidepoint(event.pos):
                    matriz = crear_matriz_buscamina(filas, columnas, num_minas)
                    descubiertas = [[False for _ in range(8)] for _ in range(8)]
                    banderas = [[False for _ in range(8)] for _ in range(8)]
                    puntaje = 0

        pantalla.blit(imagen_fondo, (0, 0))
        dibujar_tablero(matriz, descubiertas, banderas, pantalla, fuente_pequena)
        boton_reiniciar = dibujar_boton("Reiniciar", 300, 50, 200, 50, (100, 100, 100), (150, 150, 150))

        # Mostrar puntaje
        texto_puntaje = fuente.render(f"Puntaje: {puntaje:04d}", True, COLOR_TEXTO)
        pantalla.blit(texto_puntaje, (20, 20))

        if fin_juego:
            pygame.time.wait(1000)
            juego_principal()

        pygame.display.flip()

# Iniciar el juego
menu_principal()