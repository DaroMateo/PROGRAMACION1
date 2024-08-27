import pygame
import sys
import pygame_textinput
import json
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


with open("PROGRAMACION1\PLUS\\ahorcado_juanma\datos.json", "r") as archivo:
    ahorcado = json.load(archivo)["ahorcado"]


with open("PROGRAMACION1\PLUS\\ahorcado_juanma\jranking.json", "r") as archivo:
    top = json.load(archivo)["ranking"]



window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Ahorcado")


pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
sonido_fondo = pygame.mixer.Sound("PROGRAMACION1\PLUS\\ahorcado_juanma\Saint Seiya 8 BITS.mp3")
sonido_fondo.set_volume(0.1)
sonido_fondo.stop()


font = pygame.font.SysFont("Arial Narrow", 40)
font_descripcion = pygame.font.SysFont("Arial Narrow", 32)
font2 = pygame.font.SysFont("Twitchy.TV", 40)
font_palabra_secreta = pygame.font.SysFont("Arial Narrow", 110)


def swap(lista:list, indice_uno:int, indice_dos:int) -> list:
    """
    Swapea los valores de dos indices de una lista.

    Args:
        lista (list): Lista que contiene los valores a intercambiar.
        indice_uno (int): Indice del valor a intercambiar.
        indice_dos (int): Indice del segundo valor a intercambiar.

    Returns:
        list: Retorna la lista con los valores intercambiados.
    """
    auxiliar = lista[indice_uno]
    lista[indice_uno] = lista[indice_dos]
    lista[indice_dos] = auxiliar
    
    return lista  


def ordenar(lista:list, clave:str, ascendente:bool=True)-> list: 
    """
    Ordena una lista de diccionarios en base a una clave de forma ascendente o descendente.

    Args:
        lista (list): Lista de diccionarios a ordenar.
        clave (str): Clave a usar para ordenar la lista
        ascendente (bool, opcional): Declara si la lista se ordena de forma ascendente o descendente. Se le asigna False para ordenar de forma descendente. (Si no se pasa ningun valor booleano ordena de forma ascendente por defecto.)

    Returns:
        list: Retorna la lista de diccionarios ordenada.
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if ascendente and int(lista[i][clave] )> int(lista[j][clave]) or not ascendente and int(lista[i][clave]) < int(lista[j][clave]):
                swap(lista, i, j)
    return lista


def modificar_datos_json(nombre:str, clave:str, lista:list, dato_jugador:dict) -> None:
    """
    Modifica un archivo JSON sobreescribiendo su contenido con una nueva lista de diccionarios, la cual contiene un diccionario pasado por parametro, que aloja el nick y el score del usuario. Luego se le agrega la lista de diccionarios existente y se la ordena segun el valor del score de forma descendente. Como instancia final elimina el último elemento del diccionario.

    Args:
        nombre (str): Nombre y ruta del archivo JSON a modificar.
        clave (str): La clave de la lista de diccionarios.
        lista (list): La lista de diccionarios a sobreescribir en el JSON.
        dato (dict): Valor en formato diccionario que desea agregar a la lista del mismo. 

    Returns:
        None
    """
    data = dato_jugador
    data.append(lista)
    data = ordenar(data, "score", False)
    data.pop()
    data = {clave:data}
    
    with open(nombre, 'w+') as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False )


def generar_json(nombre:str, lista:list, clave:str) -> None:
    """
    Genera un archivo JSON con el nombre y la ruta deseada y se le da como valor la lista proporcionada bajo la clave ingresada.

    Args:
        nombre (str): El nombre y la ruta del archivo JSON a generar.
        lista (list): La lista de datos a escribir en el archivo JSON.
        clave (str): La clave bajo la cual se almacenara la lista en el archivo JSON.

    Returns:
        None
    """
    data = {clave: lista}

    with open(nombre, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False )


lista_palabras_usadas = []

def obtener_palabra(lista:list, idioma:str) -> str:
    """
    Genera una palabra aleatoria de una lista ingresada con el idioma seleccionado como criterio.
    
    Args:
        lista (list): Lista de palabras.
        idioma (str): El idioma en el que se desea devolver la palabra.
    
    Returns:
        str: La palabra seleccionada aleatoriamente en el idioma especificado.
    """
    
    palabra = random.choice(lista)
    bandera = False
    if len(lista_palabras_usadas) == len(lista):
        print("Ya no quedan palabras, pesado.")
        palabra = False
        bandera = True
        
    else:
        while palabra ["id"] in lista_palabras_usadas:
            palabra = random.choice(lista)
    if bandera == False:
        lista_palabras_usadas.append(palabra["id"])
        palabra = palabra[idioma]

    return palabra


def slot_palabra(palabra):
    """
    Genera un string de guiones basado en el largo de la palabra de ingresada.
    
    Args:
        palabra (str): Palabra con la cual la cual se generará el string.
    
    Returns:
        str: String de guiones que representa la palabra ingresada.
    """
        
    retorno = ""

    if palabra == False:
        retorno = True

    else:
        for letra in palabra:  
            retorno += "-"

    return retorno


def verificar_letra(palabra:str, ingreso:str, palabra_secreta:str) -> str:
    """
    Esta función verifica si una letra está en la palabra secreta ingresada, actualiza la misma si la letra corresponde y devuelve la palabra actualizada. Si la letra no corresponde, devuelve False.

    Args:
        palabra: Una cadena que representa la palabra original
        ingreso: La letra a verificar
        palabra_secreta: Cadena formada por guiones a actualizar.

    Returns:
        str: Si la letra está en la palabra secreta, retorna la palabra actualizada con la letra visible tantas veces como la contenga. Si la letra no corresponde, retorna False.
    """
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

    return palabra_final if bandera_cambio == True else False


def ranking():
    """
    Muestra el ranking de los mejores jugadores en el juego. Contiene la interfaz y la informacion del ranking.

    Returns:
        bool: Al clickear en el boton para volver al menu principal retorna True.
    """    
    imagen_fondo = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\el_bosque.jpg")
    window.blit(imagen_fondo,(0,0))
    exit = pygame.draw.rect(window, (255, 0, 0), (750, 0, 100, 40))
    text_exit = font2.render("X", True, (255,255,255))
    window.blit(text_exit, (765, 10))
    recuadro()

    primer_puesto = pygame.draw.rect(window, (238, 130, 238), (50, 100, 700, 60))
    segundo_puesto = pygame.draw.rect(window, (238, 130, 238), (50, 200, 700, 60))
    tercero_puesto = pygame.draw.rect(window, (238, 130, 238), (50, 300, 700, 60))
    cuarto_puesto = pygame.draw.rect(window, (238, 130, 238), (50, 400, 700, 60))
    quinto_puesto = pygame.draw.rect(window, (238, 130, 238), (50, 500, 700, 60))
    
    text_puesto = font2.render("PUESTO", True, (0,0,0))
    text_place = font2.render("PLACE", True, (0,0,0))
    text_nombre = font2.render("NOMBRE", True, (0,0,0))
    text_name = font2.render("NAME", True, (0,0,0))
    text_puntos = font2.render("PUNTOS", True, (0,0,0))
    text_score = font2.render("SCORE", True, (0,0,0))

    window.blit(text_puesto, (32, 50))
    window.blit(text_nombre, (340, 50))
    window.blit(text_puntos, (654, 50))

    text_primero = font2.render("1°", True, (0,0,0))
    text_segundo = font2.render("2°", True, (0,0,0))
    text_tercero = font2.render("3°", True, (0,0,0))
    text_cuarto = font2.render("4°", True, (0,0,0))
    text_quinto = font2.render("5°", True, (0,0,0))

    window.blit(text_primero, (80, 116))
    window.blit(text_segundo, (80, 216))
    window.blit(text_tercero, (80, 316))
    window.blit(text_cuarto, (80, 416))
    window.blit(text_quinto, (80, 516))

    nombre_uno = font2.render(f"{top[0]["nick"]}", True, (0,0,0))
    nombre_dos = font2.render(f"{top[1]["nick"]}", True, (0,0,0))
    nombre_tres = font2.render(f"{top[2]["nick"]}", True, (0,0,0))
    nombre_cuatro = font2.render(f"{top[3]["nick"]}", True, (0,0,0))
    nombre_cinco = font2.render(f"{top[4]["nick"]}", True, (0,0,0))

    window.blit(nombre_uno, (316,116))
    window.blit(nombre_dos, (316,216))
    window.blit(nombre_tres, (316,316))
    window.blit(nombre_cuatro, (316,416))
    window.blit(nombre_cinco, (316,516))

    puntos_uno = font2.render(f"{top[0]["score"]}", True, (0,0,0))
    puntos_dos = font2.render(f"{top[1]["score"]}", True, (0,0,0))
    puntos_tres = font2.render(f"{top[2]["score"]}", True, (0,0,0))
    puntos_cuatro = font2.render(f"{top[3]["score"]}", True, (0,0,0))
    puntos_cinco = font2.render(f"{top[4]["score"]}", True, (0,0,0))

    window.blit(puntos_uno,(700,116))
    window.blit(puntos_dos,(700,216))
    window.blit(puntos_tres,(700,316))
    window.blit(puntos_cuatro,(700,416))
    window.blit(puntos_cinco,(700,516))

    run = True

    while run:
        events = pygame.event.get()
                
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 750 and event.pos[0] <= 795 and event.pos[1] >= 5 and event.pos[1] <= 38:
                    run = False
                    retorno = True
            
            pygame.display.flip()
    
    return retorno
         
    
def recuadro():
    """
    Renderiza un cortorno en la ventana utilizando líneas de color negro con coordenadas.
    """
    pygame.draw.line(window, (0,0,0), (0,0), (0, 600), 10)
    pygame.draw.line(window, (0,0,0), (0,600), (800, 600), 10)
    pygame.draw.line(window, (0,0,0), (0,0), (800, 0), 11)
    pygame.draw.line(window, (0,0,0), (800,0), (800, 600), 11)
     


def nombre_puntos(puntos, idioma, lista, sonido_fondo):
    """
    Renderiza una ventana donde se le solicita al usuario que ingrese su nombre, al cual se le adjunta su puntaje y se lo agrega al JSON con el ranking en caso de que el mismo supere alguna puntuacion de dicho top 5. (El idioma ingresado modifica los textos en pantalla. Debe ser "ES" o "EN").

    Args:
        puntos (int): Contador de puntos del jugador.
        idioma (str): Cadena de caracteres que define el idioma de los textos. Debe ser "ES" o "EN".
        lista (list): Lista que contiene el diccionario con la informacion del top 5 (Ranking).
        sonido_fondo (pygame.mixer.Sound): Objeto de sonido que contiene la musica de fondo.

    Returns:
        bool: Devuelve True cuando el usuario ingresa el nombre al terminar la partida.
    """

    retorno = None
    puntaje = puntos
    continuar = True

    window.fill((255,255,255))
    imagen_fondo = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\el_fondo.png")
    imagen_titulo = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\stitulo_juego.png")
    imagen_final = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\game_over.png")
    window.blit(imagen_fondo,(0,100))
    window.blit(imagen_titulo,(125,40))
    window.blit(imagen_final,(242,180))
    recuadro()
    rectangulo_puntaje = pygame.draw.rect(window, (238, 130, 238), (240, 384, 300, 60))
    rectangulo_nombre = pygame.draw.rect(window, (238, 130, 238), (240, 500, 300, 60))
    
    sonido_mute = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\sonido_mute.png")
    sonido = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\sonido.png")
    window.blit(sonido,(690,10))
    window.blit(sonido_mute,(740,10))

    input_nombre = pygame_textinput.TextInputVisualizer()

    if idioma == "ES":
        text_puntos = font2.render(f"Tu Puntaje: {puntaje}", True, (0,0,0))
        text_nombre = font2.render(f"INGRESE SU NOMBRE", True, "White")
        window.blit(text_nombre,(241,472))
        window.blit(text_puntos,(296, 400))

    if idioma == "EN":
        text_score = font2.render(f"Your Score: {puntaje}", True, (0,0,0))
        text_name = font2.render(f"ENTER YOUR NAME", True, "White")
        window.blit(text_score,(296, 400))
        window.blit(text_name,(252,472))


    while continuar:
        events = pygame.event.get()
        rectangulo_nombre = pygame.draw.rect(window, (238, 130, 238), (240, 500, 300, 60))
        input_nombre.update(events)
        window.blit(input_nombre.surface, (340, 518))
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 740 and event.pos[0] <= 780 and event.pos[1] >= 10 and event.pos[1] <= 50:
                    sonido_fondo.set_volume(0)

                if event.pos[0] >= 692 and event.pos[0] <= 727 and event.pos[1] >= 10 and event.pos[1] <= 50:
                    sonido_fondo.set_volume(0.1)

            if event.type == pygame.QUIT:
                continuar = False
                sys.exit()

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.KSCAN_RETURN):
                nombre = input_nombre.value
                if nombre != "":
                    id_juego = {"score": puntaje, "nick": nombre}
                    modificar_datos_json("ahorcado\jranking.json", "ranking", id_juego, lista)
                    generar_json("ahorcado\jranking.json", lista, "ranking")
                    retorno = True
                    continuar = False
        
        pygame.display.flip()
    
    return retorno
             

def español():
    """
    Renderiza la versión en español de la interdaz de la pantalla del juego.

    Returns:
        None
    """
    imagen_juego = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\el_bosque.jpg")
    imagen_soga = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\soga.png")
    window.blit(imagen_juego, (0,0))
    window.blit(imagen_soga, (250,0))

    recuadro_letra = pygame.draw.rect(window, (238, 130, 238), (50, 180, 160, 60))
    boton_obtener_palabra = pygame.draw.rect(window, (238, 130, 238), (50, 500, 260, 60))
    recuadro()

    text_obtener_palabra = font2.render("Obtener Palabra", True, (0,0,0))
    text_letra = font2.render("Letra:", True, (0,0,0))
    window.blit(text_obtener_palabra,(64, 516))
    window.blit(text_letra, (70,198))



def ingles():
    """
    Renderiza la versión en ingles de la interdaz de la pantalla del juego.

    Returns:
        None
    """
    imagen_juego = pygame.image.load("ahorcado\el_bosque.jpg")
    imagen_soga = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\soga.png")
    window.blit(imagen_juego, (0,0))
    window.blit(imagen_soga, (250,0))

    recuadro_letra = pygame.draw.rect(window, (238, 130, 238), (50, 180, 160, 60))
    boton_obtener_palabra = pygame.draw.rect(window, (238, 130, 238), (50, 500, 260, 60))
    recuadro()

    text_obtener_palabra = font2.render("Get Word", True, (0,0,0))
    window.blit(text_obtener_palabra,(120, 516))
    text_letra = font2.render("Letter:", True, (0,0,0))
    window.blit(text_letra, (60,198))


def juego(idioma, lista, sonido_fondo):
    """
    Renderiza la pantalla principal de juego en base al idioma ingresado, se configura en base a la ventana del juego y maneja el input de texto del usuario.
    Cuando el usuario ingresa las letras, se verifican en la palabra, y tambien si la misma se ha adivinado correctamente. De ser así, actualiza la puntuación y se selecciona una nueva palabra.
    Si el usuario comete un error, la función actualiza el contador de errores. En caso de que el usuario alcance el número máximo de errores (6) o adivine la palabra correctamente, el juego termina y se devuelve la puntuación final.

    Args:
        idioma (str): Cadena de caracteres con el idioma del juego deseado.
        lista (list): Lista de diccionarios con las palabras del juego.
        sonido_fondo (pygame.mixer.Sound): Objeto de sonido que contiene la musica de fondo.

    Returns:
        int: Retorna la puntuación del usuario.
    """
    retorno = None
    running = True
    bandera_palabra = False
    bandera_interfaz = False
    bandera_derrota = False
    palabra_secreta = ""
    puntaje = 0
    contador_errores = 0

    pygame.mixer.init()

    sonido_palabra = pygame.mixer.Sound("PROGRAMACION1\PLUS\\ahorcado_juanma\palabra_descubierta.mp3")
    sonido_palabra.set_volume(0.2)

    sonido_derrota = pygame.mixer.Sound("PROGRAMACION1\PLUS\\ahorcado_juanma\Derrota.mp3")
    sonido_derrota.set_volume(0.2)

    

    textinput = pygame_textinput.TextInputVisualizer()

    while running:
        if bandera_interfaz == False:
            events = pygame.event.get()

            imagen_juego = pygame.image.load("ahorcado\el_bosque.jpg")
            window.blit(imagen_juego, (0,0))
            imagen_soga = pygame.image.load("PROGRAMACION1\PLUS\ahorcado_juanma\soga.png")
            window.blit(imagen_soga, (300,0))
            recuadro()           

            if idioma == "ES":
                español()
                puntos = font2.render(f"Puntaje: {puntaje}", True, (0,0,0))
                errores = font2.render(f"Errores: {contador_errores}", True, "White")
                window.blit(errores, (630, 530))
                window.blit(puntos, (630, 70))

            if idioma == "EN":
                ingles()
                score = font2.render(f"Score: {puntaje}", True, (0,0,0))
                faults = font2.render(f"Faults: {contador_errores}", True, "White")
                window.blit(faults, (630, 530))
                window.blit(score, (630, 70))

            textinput.update(events)
            window.blit(textinput.surface, (152,200))

        sonido_mute = pygame.image.load("ahorcado\sonido_mute.png")
        sonido = pygame.image.load("ahorcado\sonido.png")
        window.blit(sonido,(690,10))
        window.blit(sonido_mute,(740,10))
    

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 740 and event.pos[0] <= 780 and event.pos[1] >= 10 and event.pos[1] <= 50:
                    sonido_fondo.set_volume(0)

                if event.pos[0] >= 692 and event.pos[0] <= 727 and event.pos[1] >= 10 and event.pos[1] <= 50:
                    sonido_fondo.set_volume(0.1)

            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            if bandera_palabra == True:
                text_palabra_secreta = font_palabra_secreta.render(f"{palabra_secreta}", True, "white")
                window.blit(text_palabra_secreta,(100,400))
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= (50) and event.pos[0] <= 310 and event.pos[1] >= 500 and event.pos[1] <= 560:
                    palabra = obtener_palabra(lista, idioma)
                    palabra_secreta = slot_palabra(palabra)
                    bandera_palabra = True



            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.KSCAN_RETURN):
                validacion = verificar_letra(palabra, textinput.value, palabra_secreta)
                textinput.value = ""

                if validacion != False:
                    palabra_secreta = validacion

                else:
                    contador_errores += 1

                if validacion == palabra:
                    sonido_palabra.play()
                    puntaje += len(palabra)
                    palabra = obtener_palabra(lista, idioma)
                    palabra_secreta = slot_palabra(palabra)
                    contador_errores = 0
                    
            if contador_errores == 1:
                pygame.draw.circle(window, (0, 0, 0), (410, 180), 30)

            if contador_errores == 2:
                pygame.draw.circle(window, (0, 0, 0), (410, 180), 30)
                pygame.draw.line(window, (0,0,0), (410,214), (410, 350), 60)

            if contador_errores == 3:
                pygame.draw.circle(window, (0, 0, 0), (410, 180), 30)
                pygame.draw.line(window, (0,0,0), (410,214), (410, 350), 60)
                pygame.draw.line(window, (0,0,0), (443,224), (500, 270), 20)

            if contador_errores == 4:
                pygame.draw.circle(window, (0, 0, 0), (410, 180), 30)
                pygame.draw.line(window, (0,0,0), (410,214), (410, 350), 60)
                pygame.draw.line(window, (0,0,0), (443,224), (500, 270), 20)
                pygame.draw.line(window, (0,0,0), (377,224), (320, 270), 20)

            if contador_errores == 5:
                pygame.draw.circle(window, (0, 0, 0), (410, 180), 30)
                pygame.draw.line(window, (0,0,0), (410,214), (410, 350), 60)
                pygame.draw.line(window, (0,0,0), (443,224), (500, 270), 20)
                pygame.draw.line(window, (0,0,0), (377,224), (320, 270), 20)
                pygame.draw.line(window, (0,0,0), (420,340), (480, 440), 20)

            if contador_errores == 6:
                window.blit(imagen_juego, (0,0))
                window.blit(imagen_soga, (250,0))
                text_continuar = font2.render("CONTINUAR", True, (0,0,0))
                text_continue = font2.render("CONTINUE", True, (0,0,0))
                sonido_mute = pygame.image.load("ahorcado\sonido_mute.png")
                sonido = pygame.image.load("ahorcado\sonido.png")
                window.blit(sonido,(690,10))
                window.blit(sonido_mute,(740,10))
                rectangulo_continuar = pygame.draw.rect(window, (238, 130, 238), (250, 480, 300, 60))

                if idioma == "EN":
                    window.blit(text_continue,(324,498))

                if idioma == "ES":
                    window.blit(text_continuar,(318,498))
                
                recuadro()
                pygame.draw.circle(window, (0, 0, 0), (410, 180), 30)
                pygame.draw.line(window, (0,0,0), (410,214), (410, 350), 60)
                pygame.draw.line(window, (0,0,0), (443,224), (500, 270), 20)
                pygame.draw.line(window, (0,0,0), (377,224), (320, 270), 20)
                pygame.draw.line(window, (0,0,0), (420,340), (480, 440), 20)
                pygame.draw.line(window, (0,0,0), (400,340), (340, 440), 20)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] >= 250 and event.pos[0] <= 549 and event.pos[1] >= 479 and event.pos[1] <= 540:
                        bandera_derrota = True
                        sonido_derrota.play()

                        if bandera_derrota == True:
                            bandera_interfaz = True
                            retorno = puntaje
                            running = False

            if puntaje == 91 or palabra_secreta == True:
                bandera_interfaz = True
                retorno = puntaje
                running = False
                
            pygame.display.flip()

    return retorno



def elegir_idioma(sonido_fondo):
    """
    Renderiza la pantalla para elegir el idioma al inicio del juego.
    
    Args:
        sonido_fondo (pygame.mixer.Sound): Objeto de sonido que contiene la musica de fondo.
    
    Returns:
        str: Retorna el idioma elegido en formato de clave ("ES" = español, "EN" = inglés).
    """    
    retorno = False
    continuar = True


    imagen_fondo = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\el_fondo.png")


    window.fill((255,255,255))
    window.blit(imagen_fondo,(0,100))


    recuadro()
    pygame.draw.line(window, (0,0,0), (0,0), (0, 600), 10)
    pygame.draw.line(window, (0,0,0), (0,600), (800, 600), 10)
    pygame.draw.line(window, (0,0,0), (0,0), (800, 0), 11)
    pygame.draw.line(window, (0,0,0), (800,0), (800, 600), 11)


    sonido_mute = pygame.image.load("ahorcado\sonido_mute.png")
    sonido = pygame.image.load("ahorcado\sonido.png")
    window.blit(sonido,(690,10))
    window.blit(sonido_mute,(740,10))


    text_elegir_idioma = font2.render("ELIGE UN IDIOMA PARA COMENZAR!", True, (0,0,0))
    recuadro_idioma = pygame.draw.rect(window, (238, 130, 238), (130, 84, 540, 60))
	

    boton_español = pygame.draw.rect(window, (142, 68, 173), (60, 200, 300, 60))
    boton_ingles = pygame.draw.rect(window, (142, 68, 173), (440, 200, 300, 60))
    text_español = font2.render("ESPAÑOL", True, (0,0,0))
    text_ingles = font2.render("ENGLISH", True, (0,0,0))
	

    window.blit(text_elegir_idioma,(146,100))
    window.blit(text_español, (140,214))
    window.blit(text_ingles,(530,215))


    while continuar:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 740 and event.pos[0] <= 780 and event.pos[1] >= 10 and event.pos[1] <= 50:
                    sonido_fondo.set_volume(0)

                if event.pos[0] >= 692 and event.pos[0] <= 727 and event.pos[1] >= 10 and event.pos[1] <= 50:
                    sonido_fondo.set_volume(0.1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 60 and event.pos[0] <= 360 and event.pos[1] >= 200 and event.pos[1] <= 259:
                    retorno = "ES"
                    continuar = False
                    
                if event.pos[0] >= 440 and event.pos[0] <= 740 and event.pos[1] >= 200 and event.pos[1] <= 259:
                    retorno = "EN"
                    continuar = False                    

            if event.type == pygame.QUIT:
                continuar = False
                sys.exit()

            pygame.display.flip()
            
    return retorno




def menu_principal(sonido_fondo):
    """
    Renderiza la pantalla que contiene el menú principal del juego, que esta dividida en tres botones: "JUGAR", "RANKING" y "SALIR".

    Args:
        sonido_fondo (pygame.mixer.Sound): Objeto de sonido que contiene la musica de fondo.

    Returns:
        bool: Retorna True si el usuario seleccionó la opción "JUGAR". En caso de que el usuario seleccione la opcion "RANKING" retornara False.
    """
    retorno = False
    menu = True
    imagen_fondo = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\el_fondo.png")
    imagen_segundotitulo = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\stitulo_utn.png")
    imagen_titulo = pygame.image.load("PROGRAMACION1\PLUS\\ahorcado_juanma\stitulo_juego.png")
    

    window.fill((255,255,255))

    window.blit(imagen_fondo,(0,100))
    window.blit(imagen_titulo,(125,150))
    window.blit(imagen_segundotitulo,(309,72))
    

    boton_start = pygame.draw.rect(window, (238, 130, 238), (250, 300, 300, 60))
    text_start = font2.render("JUGAR", True, (0, 0, 0))


    boton_ranking = pygame.draw.rect(window, (238, 130, 238), (250, 370, 300, 60))
    text_ranking = font2.render("RANKING", True, (0, 0, 0))


    boton_salir = pygame.draw.rect(window, (238, 130, 238), (250, 440, 300, 60))
    text_salir = font2.render("SALIR", True, (0,0,0))


    text_descripcion = font_descripcion.render("Developed by Juan Manuel Magas.", True, "Grey")

    recuadro()

    bandera_textos = True
    bandera_musica = True

    while menu:
        events = pygame.event.get()

        sonido_mute = pygame.image.load("ahorcado\sonido_mute.png")
        sonido = pygame.image.load("ahorcado\sonido.png")
        window.blit(sonido,(690,10))
        window.blit(sonido_mute,(740,10))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 740 and event.pos[0] <= 780 and event.pos[1] >= 10 and event.pos[1] <= 50:
                    sonido_fondo.set_volume(0)

                if event.pos[0] >= 692 and event.pos[0] <= 727 and event.pos[1] >= 10 and event.pos[1] <= 50:
                    sonido_fondo.set_volume(0.1)
                    

            if event.type == pygame.QUIT:
                menu = False
                sys.exit()

            if bandera_textos == True:
                window.blit(text_start,(350,318))
                window.blit(text_ranking,(334,388))
                window.blit(text_salir, (356,456))
                window.blit(text_descripcion,(216,570))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] > 250 and event.pos[0] <= 550 and event.pos[1] >= 350 and event.pos[1] <= 409:
                    retorno = False
                    menu = False

                if event.pos[0] >= 250 and event.pos[0] <= 550 and event.pos[1] >= 440 and event.pos[1] <= 499:
                    menu = False

                    sys.exit()
                if event.pos[0] >= 250 and event.pos[0] <= 550 and event.pos[1] >= 300 and event.pos[1] <= 359:
                    bandera_textos = False
                    retorno = True
                    menu = False

        pygame.display.flip()

    return retorno


def ahorcado():
    """
    Función principal donde se aloja el bucle que controla el funcionamiento del juego en su totalidad. Carga las palabras y el top 5 del juego desde sus respectivos archivos JSON e inicializa las fuentes y la musica de fondo del juego.
    """
     
    pygame.init()
     
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600


    with open("ahorcado\datos.json", "r") as archivo:
        ahorcado = json.load(archivo)["ahorcado"]


    with open("ahorcado\jranking.json", "r") as archivo:
        top = json.load(archivo)["ranking"]


    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("Ahorcado")


    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.1)
    sonido_fondo = pygame.mixer.Sound("ahorcado\Saint Seiya 8 BITS.mp3")
    sonido_fondo.set_volume(0.1)


    font = pygame.font.SysFont("Arial Narrow", 40)
    font_descripcion = pygame.font.SysFont("Arial Narrow", 32)
    font2 = pygame.font.SysFont("Twitchy.TV", 40)
    font_palabra_secreta = pygame.font.SysFont("Arial Narrow", 110)

    run = True
    opciones_menu = True
    bandera_juego = False
    resultado = -1


    while run:
        events = pygame.event.get()
        sonido_fondo.play(-1)

        for event in events:    
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if opciones_menu == True:
                opcion = menu_principal(sonido_fondo)

            if opcion == True:
                opciones_menu = False
                idioma = elegir_idioma(sonido_fondo)
                print(idioma)
                bandera_juego = True
            
            if bandera_juego == True:
                opcion = False
                if idioma != False:
                    resultado = juego(idioma, ahorcado, sonido_fondo)

            if resultado >= 0:
                bandera_juego = False
                player = nombre_puntos(resultado, idioma, top, sonido_fondo)

            if opcion == False or player == True:
                bucle = ranking()

            if bucle == True:
                opciones_menu = True
                bandera_juego = False
                
        pygame.display.flip()



