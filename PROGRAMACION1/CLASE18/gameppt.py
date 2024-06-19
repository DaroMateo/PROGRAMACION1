import pygame

pygame.init() #Se inicializa pygame
screen = pygame.display.set_mode([500, 500]) #Se crea una ventana
running = True
while running:
   # Se verifica si el usuario cerro la ventana
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   screen.fill((255, 255, 255))# Se pinta el fondo de la ventana
   # Se dibuja un círculo azul en el centro
   pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
   pygame.display.flip()# Muestra los cambios en  la pantalla
pygame.quit() # Fin

'''Se dibuja un círculo azul'''
#pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

'''Se dibuja un cuadrado amarillo'''
#pygame.draw.rect(screen, (255, 255, 0), (30, 30, 60, 60))

'''Pygame maneja todos sus mensajes de eventos a través de una cola de eventos. '''
#pygame.event.get()

'''Se crea una ventana'''
#screen = pygame.display.set_mode([500, 500]) 

'''Título de la ventana'''
#pygame.display.set_caption(“Hola Mundo”) 

'''Se verifica si el usuario cerro la ventana'''
#for event in pygame.event.get():
#    print(type(event)) # <class 'Event'>

'''Se verifica si el usuario cerro la ventana'''
#for event in pygame.event.get():
#    if event.type == pygame.QUIT:
#        running = False

"""Se verifica si el evento es el del mouse presionado y luego se verifica cual es la posición:"""
#for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#           running = False
#       if event.type == pygame.MOUSEBUTTONDOWN :
#           print(event.pos) # (322, 153)

'''Para poder fijar un evento que ocurran por tiempo.'''
#tick = pygame.USEREVENT + 0
#pygame.time.set_timer(tick,1000)
#while running:
#   for event in pygame.event.get():
#       if event.type == tick:
#       	print("Ya paso un segundo")

'''Se verifica si el evento es el de una tecla presionada y luego se verifica cual es la tecla: Eventos(Teclado)'''
#for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#           running = False
#       if event.type == pygame.KEYDOWN:
#           if event.key == pygame.K_x:
#               print("Se presiono la tecla X")

'''Teclado(s/eventos)'''
#from pygame.locals import K_x
#pressed_keys = pygame.key.get_pressed()
#if True in pressed_keys:
#    if pressed_keys[K_x]:
#            print("Se presiono la tecla X")

'''Con el método load de la clase image se puede generar una superficie desde una imagen: (IMAGEN)'''
#imagen = pygame.image.load("00.png")
#print(type(imagen)) # <class 'pygame.Surface'>

'''Para copiar la superficie de la imagen en la superficie de la pantalla o en otra superficie se debe utilizar blit() indicando la ubicación. IMGAEN '''
#imagen = pygame.image.load("00.png")
#print(type(imagen)) # <class 'pygame.Surface'>
#screen.blit(imagen,(50,50))

'''El método render me permite obtener una superficie a partir de un texto. TEXTO'''
#font = pygame.font.SysFont("Arial Narrow", 50)
#text = font.render("HOLA MUNDO", True, (255, 0, 0))
#print(type(text)) # <class 'pygame.Surface'>

'''Para copiar la superficie del texto en la superficie de la pantalla o en otra superficie se debe utilizar blit() indicando la ubicación. TEXTO'''
#font = pygame.font.SysFont("Arial Narrow", 50)
#text = font.render("HOLA MUNDO", True, (255, 0, 0))
#screen.blit(text,(50,50))

'''La forma más básica de crear un objeto Rect en Pygame es simplemente pasar dos tuplas. 
La primera tupla (izquierda, arriba) representa la posición del Rect en la ventana, mientras que la segunda tupla (ancho, alto) representa las dimensiones del Rect. RECTANGULOS'''
# Se dibuja un cuadrado amarillo
#rectangulo = pygame.Rect((30, 30), (60,60))
#pygame.draw.rect(screen, (255, 255, 0), rectangulo)

'''También es posible obtener un objeto Rect de una superficie y manipularlo.  RECTANGULOS'''
#imagen_dona = pygame.image.load("00.png")
#rect_dona = imagen_dona.get_rect()
#rect_dona.centerx = 200
#rect_dona.centery = 100
#print(rect_dona.width,rect_dona.height) # 200 200
#screen.blit(imagen_dona,rect_dona)

'''Para cada rectángulo, es posible comprobar si colisiona con otro. COLISIONES'''
#if rect_player.colliderect(rect_piedra):
#   print("El jugador colisiona con la piedra")
#if rect_player.colliderect(rect_fuego):
#    print("El jugador colisiona con el fuego")

'''Es posible comprobar si un rectángulo colisiona con algún otro rectángulo de una lista de Rect. COLISIONES'''
#if rect_player.collidelist(lista_rect) >= 0:
#    print("El jugador colisionó con la piedra")

'''También es posible comprobar si colisiona una superficie con una coordenada. COLISIONES'''
#if event.type == pygame.MOUSEBUTTONDOWN :
#    if rect_player.collidepoint(event.pos):
#   		print("CLICK sobre el jugador")

'''Los formatos de archivos de sonido que Pygame soporta son MID, WAV y MP3. Si al play se le pasa -1 como argumento, se va a reproducir el sonido de manera indefinida. SONIDO'''
#pygame.mixer.init()
#pygame.mixer.music.set_volume(0.7)
#sonido_fondo = pygame.mixer.Sound("fondo.wav")
#sonido_fondo.set_volume(0.2)
#sonido_fondo.play()
#sonido_fondo.stop()



