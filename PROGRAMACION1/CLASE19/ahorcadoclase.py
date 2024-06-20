import pygame
import pygame_textinput
import json
import random

pygame.init()

running = True

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

textinput = pygame_textinput.TextInputVisualizer()

tick_1s = pygame.USEREVENT + 0
tick_2s = pygame.USEREVENT + 1
pygame.time.set_timer(tick_1s,1000)
pygame.time.set_timer(tick_2s,2000)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Ahorcado")

puntaje = 0
nombre= ""
font = pygame.font.SysFont("Arial Narrow", 40)
font1 = pygame.font.SysFont("Arial Narrow", 110)
text = font.render("Puntaje: ", True, (0, 0, 0))


with open("datos.json", "r") as archivo:
    ahorcado = json.load(archivo)["ahorcado"]

lista_palabras_usadas = []

def obtener_palabra_random(lista, idioma):
    palabra = random.choice(lista)

    if len(lista_palabras_usadas) == len(lista):
        print("Ya no quedan palabras, pesado.")
        palabra = False

    else:
        while palabra["id"] in lista_palabras_usadas:
            palabra = random.choice(lista)

        lista_palabras_usadas.append(palabra["id"])
        palabra = palabra[idioma]
    
    return palabra

def slot_palabra(palabra:str):
    retorno = ""

    if palabra == False:
        retorno = "Juego Terminado"
    else:
        for letra in palabra:
            retorno += "-"

    return retorno

def verificar_letra_en_palabra(palabra, ingreso ,palabra_secreta):
    bandera_cambio = False

    lista_palabra_secreta = []

    for letra in palabra_secreta:
        lista_palabra_secreta.append(letra)

    if len(ingreso) == 1:
        for i in range(len(palabra)):
            if palabra[i] == ingreso:
                lista_palabra_secreta[i] = ingreso
                bandera_cambio = True

    palabra_final = ""
    for letra in lista_palabra_secreta:
        palabra_final += letra

    print(palabra_final)

    return palabra_final if bandera_cambio == True else False


linea = pygame.draw.line(window, (0,0,0), (300,100), (300, 200), 10)
#window.blit(linea)


#numero = obtener_palabra_random(ahorcado)
"""for i in range(11):
    numero = obtener_palabra_random(ahorcado,"ES")
    print(numero)


print(lista_palabras_usadas)"""

palabra_secreta = ""
bandera_nombre = True

posicion = (130, 12)
contador_errores = 0

while running:
    window.fill((255,255,255))
    
    events = pygame.event.get()

    textinput.update(events)

    window.blit(textinput.surface, posicion)


    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Hiciste click")
            print(event.pos)
            if event.pos[0] >= (250) and event.pos[0] <= 309 and event.pos[1] >= (250) and event.pos[1] <= 309:
                palabra = obtener_palabra_random(ahorcado, "ES")
                palabra_secreta = slot_palabra(palabra)
                

        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.KSCAN_RETURN):
            if bandera_nombre == True:
                nombre = textinput.value
                posicion = (130,200)
                bandera_nombre = False
            else:
                validacion = verificar_letra_en_palabra(palabra, textinput.value,palabra_secreta)
                if validacion != False:
                    palabra_secreta = validacion
                else:
                    contador_errores += 1
                if validacion == palabra:
                    puntaje += len(palabra)
                    palabra = obtener_palabra_random(ahorcado, "ES")
                    palabra_secreta = slot_palabra(palabra)
                    contador_errores = 0
                if contador_errores == 6:
                    palabra = obtener_palabra_random(ahorcado, "ES")
                    palabra_secreta = slot_palabra(palabra)
                    contador_errores = 0
            textinput.value = ""

        if event.type == pygame.QUIT:
            running = False


    pygame.draw.line(window, ("brown"), (400,0), (400, 100), 10)
    
    pygame.draw.ellipse(window, ("brown"), (350, 100, 100, 50), 5)

    pygame.draw.rect(window, (238, 130, 238), (250, 250, 60, 60))
    text = font.render(f"Puntaje: {puntaje}", True, (0, 0, 0))
    text3 = font.render(f"Errores: {contador_errores}", True, (0, 0, 0))
    text1 = font1.render(f"{palabra_secreta}", True, (0, 0, 0))
    text2 = font.render(f"Nombre: {nombre}", True, (0, 0, 0))
    window.blit(text,(600,10))
    window.blit(text3,(600,500))
    window.blit(text1,(100,400))
    window.blit(text2,(10,10))

    pygame.display.update()

    pygame.display.flip()


                      