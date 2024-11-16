import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Buscaminas")

# Colores
COLOR_BOTON = (0, 200, 0)
COLOR_TEXTO = (255, 255, 255)
COLOR_CASILLA = (200, 200, 200)
COLOR_CASILLA_DESCUBIERTA = (150, 150, 150)
COLOR_BANDERA = (255, 0, 0)

# Fuentes
fuente = pygame.font.SysFont(None, 48)
fuente_pequena = pygame.font.SysFont(None, 36)

# Cargar la imagen de fondo
fondo = pygame.image.load("fondo1.jpg")
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Cargar el sonido de fondo
pygame.mixer.music.load("ringtones-got-theme.mp3")
pygame.mixer.music.play(-1)  # Reproducir en bucle

def crear_matriz_buscamina(filas=8, columnas=8, num_minas=10):
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

def dibujar_tablero(matriz, descubiertas, banderas):
    filas = len(matriz)
    columnas = len(matriz[0])
    tam_casilla = 50
    margen = 10
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * (tam_casilla + margen)
            y = fila * (tam_casilla + margen) + 100
            rect = pygame.Rect(x, y, tam_casilla, tam_casilla)
            if descubiertas[fila][columna]:
                pygame.draw.rect(pantalla, COLOR_CASILLA_DESCUBIERTA, rect)
                if matriz[fila][columna] != 0:
                    texto = fuente_pequena.render(str(matriz[fila][columna]), True, COLOR_TEXTO)
                    pantalla.blit(texto, (x + (tam_casilla - texto.get_width()) // 2, y + (tam_casilla - texto.get_height()) // 2))
            else:
                pygame.draw.rect(pantalla, COLOR_CASILLA, rect)
                if banderas[fila][columna]:
                    pygame.draw.rect(pantalla, COLOR_BANDERA, rect)

def crear_boton(texto, x, y, ancho, alto):
    rect = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(pantalla, COLOR_BOTON, rect)
    texto_superficie = fuente.render(texto, True, COLOR_TEXTO)
    pantalla.blit(texto_superficie, (x + (ancho - texto_superficie.get_width()) // 2, y + (alto - texto_superficie.get_height()) // 2))
    return rect


def juego_principal():
    global matriz, descubiertas, banderas, puntaje  #que use la variable que está fuera de la función en lugar de crear una nueva dentro de la función.

    matriz = crear_matriz_buscamina()
    descubiertas = [[False for _ in range(8)] for _ in range(8)]
    banderas = [[False for _ in range(8)] for _ in range(8)]
    puntaje = 0
    fin_juego = False

    while True:
        pantalla.blit(fondo, (0, 0))

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
                    matriz = crear_matriz_buscamina()
                    descubiertas = [[False for _ in range(8)] for _ in range(8)]
                    banderas = [[False for _ in range(8)] for _ in range(8)]
                    puntaje = 0

        pantalla.blit(fondo, (0, 0))
        dibujar_tablero(matriz, descubiertas, banderas)
        boton_reiniciar = crear_boton("Reiniciar", 300, 50, 200, 50)

        # Mostrar puntaje
        texto_puntaje = fuente.render(f"Puntaje: {puntaje:04d}", True, COLOR_TEXTO)
        pantalla.blit(texto_puntaje, (20, 20))

        if fin_juego:
            pygame.time.wait(1000)
            juego_principal()

        pygame.display.flip()

# Iniciar el juego
juego_principal()
