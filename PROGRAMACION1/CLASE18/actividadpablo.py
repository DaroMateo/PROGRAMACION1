import pygame

pygame.init()

running = True
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

tick_1s = pygame.USEREVENT + 0
pygame.time.set_timer(tick_1s,1000)

font = pygame.font.SysFont("Arial Narrow", 25)

#imagen_original = pygame.image.load("fondo_negro.gif")
#fondo = pygame.transform.scale(imagen_original, (SCREEN_WIDTH, SCREEN_HEIGHT))

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Hola Mundo")
posicion_y = 0
posicion_x = 0
ancho = 50
alto = 50
paso = 30

contador = 0
while running:
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		if event.type == tick_1s:
			contador += 1
		if keys[pygame.K_UP]:
			if posicion_y - paso > 0:
				posicion_y -= paso
			else:
				posicion_y = 0
		if keys[pygame.K_DOWN]:
			if posicion_y+paso < SCREEN_HEIGHT - alto:
				posicion_y += paso
			else:
				posicion_y = SCREEN_HEIGHT-alto
		if keys[pygame.K_LEFT]:
			if posicion_x > 0:
				posicion_x -= paso
			else:
				posicion_x = 0
		if keys[pygame.K_RIGHT]:
			if posicion_x+paso < SCREEN_WIDTH - ancho:
				posicion_x += paso
			else:
				posicion_x = SCREEN_WIDTH-ancho
		if event.type == pygame.QUIT:
			running = False
  
		#window.fill((255, 0, 0)) # Se pinta el fondo de la ventana
		#pygame.draw.rect(window, (255, 255, 0), (30, 30, 60, 60))
		#pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
	
		pygame.display.flip()# Muestra los cambios en la pantalla
	texto = font.render(f"Tiempo: {contador}", True, (255, 0, 0))
	#window.blit(fondo, (0, 0)) 
	cuadrado = pygame.draw.rect(window, (255, 255, 0), (posicion_x, posicion_y, ancho, alto))    
	window.blit(texto,(10,10))

'''
import pygame

pygame.init()

running = True

window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hola Mundo")
while(running):
	for event in pygame.event.get():
		#print(event)
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(event.pos)
				
	window.fill((255, 0, 0)) # Se pinta el fondo de la ventana
	pygame.draw.rect(window, (255, 255, 0), (30, 30, 60, 60))
	pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
	
	pygame.display.flip()# Muestra los cambios en la pantalla
'''