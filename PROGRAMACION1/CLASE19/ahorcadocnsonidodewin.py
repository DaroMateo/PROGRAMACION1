import random
import sys
import json
import pygame

# Inicializar Pygame
pygame.init()

# Constantes
ANCHO, ALTO = 800, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NOMBRE_FUENTE = pygame.font.match_font('arial')
ARCHIVO_PUNTAJES = "puntajes.json"
ARCHIVO_PALABRAS = "palabras.json"
SONIDO_PALABRA_DESCUBIERTA = pygame.mixer.Sound("coin_mario.mp3")
SONIDO_FIN_JUEGO = pygame.mixer.Sound("game_over.mp3")

# Configuración de pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Ahorcado')

# Cargar palabras
def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        contenido = json.load(file)["ahorcado"]
    return contenido

PALABRAS = leer_archivo('ahorcado.json')

# Variables del juego
palabra_seleccionada = None
adivinadas = []
intentos = 6
puntos = 0
juego_terminado = False
idioma = None
apodo = ""
entrada_activa = False
copia_palabras = PALABRAS.copy()
silenciar = False  # Bandera de silencio de sonido

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
POS_TITULO = (ANCHO / 2, 50)
POS_PALABRA = (ANCHO / 2, 150)
POS_INTENTOS = (ANCHO / 2, 200)
POS_PUNTOS = (ANCHO / 2, 250)
POS_AHORCADO = (400, 400)
ANCHO_BOTON, ALTO_BOTON = 200, 50
INICIO_Y_BOTON = ALTO / 2 - 100
ESPACIADO_BOTON = 70

# Funciones de dibujo
def dibujar_texto(superficie, texto, tamano, x, y, alinear="centro"):
    fuente = pygame.font.Font(NOMBRE_FUENTE, tamano)
    superficie_texto = fuente.render(texto, True, BLANCO)
    rect_texto = superficie_texto.get_rect()
    if alinear == "centro":
        rect_texto.midtop = (x, y)
    elif alinear == "izquierda":
        rect_texto.topleft = (x, y)
    elif alinear == "derecha":
        rect_texto.topright = (x, y)
    superficie.blit(superficie_texto, rect_texto)

def dibujar_ahorcado(intentos):
    if intentos <= 5:
        pygame.draw.circle(pantalla, BLANCO, POS_AHORCADO, 30, 3)  # Cabeza
    if intentos <= 4:
        pygame.draw.rect(pantalla, BLANCO, (POS_AHORCADO[0] - 15, POS_AHORCADO[1] + 30, 30, 60), 3)  # Torso
    if intentos <= 3:
        pygame.draw.line(pantalla, BLANCO, (POS_AHORCADO[0], POS_AHORCADO[1] + 30), (POS_AHORCADO[0] - 50, POS_AHORCADO[1] + 80), 3)  # Brazo izquierdo
    if intentos <= 2:
        pygame.draw.line(pantalla, BLANCO, (POS_AHORCADO[0], POS_AHORCADO[1] + 30), (POS_AHORCADO[0] + 50, POS_AHORCADO[1] + 80), 3)  # Brazo derecho
    if intentos <= 1:
        pygame.draw.line(pantalla, BLANCO, (POS_AHORCADO[0], POS_AHORCADO[1] + 90), (POS_AHORCADO[0] - 50, POS_AHORCADO[1] + 150), 3)  # Pierna izquierda
    if intentos <= 0:
        pygame.draw.line(pantalla, BLANCO, (POS_AHORCADO[0], POS_AHORCADO[1] + 90), (POS_AHORCADO[0] + 50, POS_AHORCADO[1] + 150), 3)  # Pierna derecha

# Función de selección de idioma
def seleccionar_idioma():
    global idioma
    seleccionando = True
    while seleccionando:
        pantalla.blit(imagen_fondo, (0, 0))  # Dibujar imagen de fondo
        dibujar_texto(pantalla, "Seleccione Idioma / Select Language", 48, ANCHO / 2, 100)
        dibujar_texto(pantalla, "Presione 'E' para inglés o 'S' para español", 36, ANCHO / 2, 200)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando el usuario cierra la ventana
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_e:
                    idioma = 'EN'
                    seleccionando = False
                elif evento.key == pygame.K_s:
                    idioma = 'ES'
                    seleccionando = False

# Función para traducir texto según el idioma seleccionado
def traducir(clave):
    if idioma == 'EN':
        traducciones = {
            "Seleccione Idioma / Select Language": "Select Language / Seleccione Idioma",
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
            "Seleccione Idioma / Select Language": "Seleccione Idioma / Select Language",
            "Presione 'E' para inglés o 'S' para español": "Presione 'E' para inglés o 'S' para español",
            "Ingrese Apodo:": "Ingrese Apodo:",
            "Palabra:": "Palabra:",
            "Intentos Restantes:": "Intentos Restantes:",
            "Puntos:": "Puntos:",
            "Juego del Ahorcado": "Juego del Ahorcado",
            "Play": "Jugar",
            "Salir": "Salir",
            "Scores": "Puntaje"
        }
    else:
        return clave  # Por defecto, devolver la clave si el idioma no es soportado

    return traducciones.get(clave, clave)  # Devolver texto traducido o la clave en sí si no se encuentra

# Función de entrada de apodo
def entrada_apodo():
    global apodo, entrada_activa
    if apodo:
        return  # Si el apodo ya está establecido, omitir entrada
    entrada_activa = True
    caja_entrada = pygame.Rect(ANCHO / 2 - 100, ALTO / 2 - 25, 200, 50)
    color_inactivo = pygame.Color('lightskyblue3')
    color_activo = pygame.Color('dodgerblue2')
    color = color_inactivo
    activo = False
    texto = ''
    terminado = False

    while not terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando el usuario cierra la ventana
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if caja_entrada.collidepoint(evento.pos):
                    activo = not activo
                else:
                    activo = False
                color = color_activo if activo else color_inactivo
            if evento.type == pygame.KEYDOWN:
                if activo:
                    if evento.key == pygame.K_RETURN:
                        terminado = True
                    elif evento.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                    else:
                        texto += evento.unicode
            pantalla.fill(NEGRO)
            dibujar_texto(pantalla, traducir("Ingrese Apodo:"), 36, ANCHO / 2, ALTO / 2 - 100)
            texto_superficie = fuente.render(texto, True, color)
            pantalla.blit(texto_superficie, (caja_entrada.x + 5, caja_entrada.y + 5))
            pygame.draw.rect(pantalla, color, caja_entrada, 2)
            pygame.display.flip()

# Función de actualización de puntaje
def actualizar_puntaje(nuevos_puntos):
    global puntos
    puntos += nuevos_puntos

# Función de selección de palabra
def seleccionar_palabra():
    global palabra_seleccionada, adivinadas
    palabra_seleccionada = random.choice(PALABRAS)
    adivinadas = []

# Función de fin de juego
def fin_juego(ganado):
    global juego_terminado, intentos, puntos, copia_palabras, PALABRAS

    juego_terminado = True
    pantalla.blit(imagen_fondo, (0, 0))  # Dibujar imagen de fondo
    if ganado:
        actualizar_puntaje(10)
        SONIDO_PALABRA_DESCUBIERTA.play()
        dibujar_texto(pantalla, "¡Felicidades! ¡Ganaste!", 48, ANCHO / 2, ALTO / 2 - 50)
    else:
        SONIDO_FIN_JUEGO.play()
        dibujar_texto(pantalla, "Fin del Juego", 48, ANCHO / 2, ALTO / 2 - 50)
        dibujar_texto(pantalla, f"La palabra era: {palabra_seleccionada}", 36, ANCHO / 2, ALTO / 2 + 50)

    pygame.display.flip()
    pygame.time.wait(3000)

    if not copia_palabras:  # Si copia_palabras está vacía, restaurar el original
        PALABRAS = leer_archivo('ahorcado.json')
        copia_palabras = PALABRAS.copy()

    intentos = 6
    seleccionar_palabra()
    juego_terminado = False

# Bucle del juego principal
def bucle_principal():
    global juego_terminado, silenciar, intentos
    seleccionar_palabra()
    sonido_fondo.play(-1)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Salir del programa cuando el usuario cierra la ventana
            elif evento.type == pygame.KEYDOWN:
                if not juego_terminado:
                    letra = evento.unicode.upper()
                    if letra.isalpha() and len(letra) == 1:
                        if letra not in adivinadas:
                            adivinadas.append(letra)
                            if letra not in palabra_seleccionada.upper():
                                intentos -= 1
                                if intentos == 0:
                                    fin_juego(False)
                            else:
                                if all(letra.upper() in adivinadas for letra in palabra_seleccionada):
                                    fin_juego(True)
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Click izquierdo
                    if posicion_icono[0] <= evento.pos[0] <= posicion_icono[0] + tamano_icono and posicion_icono[1] <= evento.pos[1] <= posicion_icono[1] + tamano_icono:
                        silenciar = not silenciar
                        if silenciar:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

        pantalla.blit(imagen_fondo, (0, 0))  # Dibujar imagen de fondo

        # Mostrar palabra con letras adivinadas
        palabra_mostrada = ""
        for letra in palabra_seleccionada:
            if letra.upper() in adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "

        dibujar_texto(pantalla, traducir("Palabra:") + " " + palabra_mostrada, 36, POS_PALABRA[0], POS_PALABRA[1])
        dibujar_texto(pantalla, traducir("Intentos Restantes:") + f" {intentos}", 36, POS_INTENTOS[0], POS_INTENTOS[1])
        dibujar_texto(pantalla, traducir("Puntos:") + f" {puntos}", 36, POS_PUNTOS[0], POS_PUNTOS[1])

        dibujar_ahorcado(intentos)

        # Dibujar icono de sonido
        if silenciar:
            pantalla.blit(icono_sonido_apagado, posicion_icono)
        else:
            pantalla.blit(icono_sonido_encendido, posicion_icono)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

# Ejecutar juego
seleccionar_idioma()
entrada_apodo()
bucle_principal()