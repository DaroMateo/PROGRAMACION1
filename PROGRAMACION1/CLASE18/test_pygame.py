import pygame

pygame.init()

running = True

window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("vamos a hacer un juego!")
while(running):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	window.fill((255, 255, 255)) # Se pinta el fondo de la ventana

	pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
	pygame.display.flip()# Muestra los cambios en la pantalla