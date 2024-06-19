import pygame

pygame.init()

running = True
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

tick_1s = pygame.USEREVENT + 0
tick_2s = pygame.USEREVENT + 1
pygame.time.set_timer(tick_1s,1000)
pygame.time.set_timer(tick_2s,2000)

font = pygame.font.SysFont("Arial Narrow", 50)
text = font.render("Puntaje", True, (255, 0, 0))

'''imagen_original = pygame.image.load("test_pygame/pac_man_escenario_vacio.jpg")
fondo = pygame.transform.scale(imagen_original, (SCREEN_WIDTH, SCREEN_HEIGHT))'''

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Hola Mundo")

#window.blit(fondo, (0, 0))
window.blit(text,(50,50))

while running:
	for event in pygame.event.get():
		if event.type == tick_1s:
			print("Ya paso un segundo")
		if event.type == pygame.QUIT:
			running = False
  
		#window.fill((255, 0, 0)) # Se pinta el fondo de la ventana
		#pygame.draw.rect(window, (255, 255, 0), (30, 30, 60, 60))
		#pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
	
		pygame.display.flip()# Muestra los cambios en la pantalla

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
