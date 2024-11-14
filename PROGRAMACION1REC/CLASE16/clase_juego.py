import pygame
# import pygame as pg
import random

# Inicializaciones
pygame.init()
pygame.mixer.init()

# CONSTS
PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600
RESOLUCION_PANTALLA = (PANTALLA_ANCHO, PANTALLA_ALTO)

color_fondo = [127, 157, 235]
posicion_personaje = [400, 300]

# COLORES: RGB[A] (Red, Green, Blue) [Alpha] -> 0 - 255
COLOR_ROJO = (255, 0, 0)
COLOR_NARANJA = (245, 79, 7)
COLOR_AZUL_CLARO = (127, 157, 235)
COLOR_FUCSIA = (204, 6, 161)

# Pantalla Principal
# pantalla = pygame.display.set_mode((800, 600))
# pantalla = pygame.display.set_mode(RESOLUCION_PANTALLA)
pantalla = pygame.display.set_mode(RESOLUCION_PANTALLA, pygame.RESIZABLE) # Ventana maximizable
# pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption("Mi super Juego xd")

# Imagenes:
imagen_roca = pygame.image.load("Programacion_I_2C/Clase_17/roca.jpg") # Cargando una imagen de roca
pygame.display.set_icon(imagen_roca) # Creo el icono de la ventana principal
imagen_personaje = pygame.image.load("Programacion_I_2C/Clase_17/personaje.jpg")
imagen_joystick = pygame.image.load("Programacion_I_2C/Clase_17/joystick.png")
# Modificamos el tamaño de la imagen del joystick
imagen_joystick = pygame.transform.scale(imagen_joystick, (PANTALLA_ANCHO, PANTALLA_ALTO))
ancho_personaje = imagen_personaje.get_width()

# Sonidos:
# Fondo (largos, ininterrupidos)
pygame.mixer.music.load("Programacion_I_2C/Clase_17/test_sound.mp3")
pygame.mixer.music.set_volume(0.3) # 0 - 1 | 0.3 == 30%
# Efectos (mas cortos)
mi_sonido = pygame.mixer.Sound("Programacion_I_2C/Clase_17/test_sound.mp3")
mi_sonido.set_volume(0.25)

# Reloj
clock = pygame.time.Clock()


def generar_color_aleatorio()->list:
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
# contador = 0
# while True:
#     # Recorremos los eventos:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     # Dibujar en la pantalla
#     pantalla.fill(COLOR_AZUL_CLARO)

#     # contador += 1
#     # print(contador)
#     # Actualizan los cambios que le hicieron en esa iteracion.
#     pygame.display.update()

contador = 0
corriendo = True

#pygame.mixer.music.play(-1)
while corriendo == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.set_pos(400, 300))
            #mi_sonido.play()
            #pygame.mixer.music.play(-1)
            # print(evento)
            # color_fondo = generar_color_aleatorio()
            # if posicion_personaje[0] + ancho_personaje < PANTALLA_ANCHO:
            #     posicion_personaje[0] += 10
            # if posicion_personaje[0] > PANTALLA_ANCHO:
            #     posicion_personaje[0] = 0 - ancho_personaje
            # else:
            #     posicion_personaje[0] += 10
            #     posicion_personaje[1] += 10
            imagen_personaje.set_alpha(random.randint(0, 255)) # Cambiamos la transparencia del personaje

    pantalla.fill(color_fondo)
    pantalla.blit(imagen_joystick, (0, 0))
    pantalla.blit(imagen_personaje, posicion_personaje)

    # Rect (clase) -> Ubicacion y Tamaño (X, Y, Ancho, Alto) 
    pygame.draw.rect(pantalla, COLOR_NARANJA, (50, 50, 100, 75), width=10)
    pygame.draw.rect(pantalla, COLOR_NARANJA, (50, 150, 100, 75), width=10, border_radius=15)
    pygame.draw.circle(pantalla, COLOR_FUCSIA, (700, 100), 75, width=20)
    # print(contador)
    # contador += 1
    # if contador > 3:
    #     contador = 0
    #     posicion_personaje[0] += 1

    clock.tick(60)
    print(clock.get_fps())
    pygame.display.flip()

pygame.quit()