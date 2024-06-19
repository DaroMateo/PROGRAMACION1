import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Objeto en movimiento con contador de tiempo")

# Colores
MISTYROSE1 = (255, 228, 225)
ORANGE = (255, 128, 0)

# Configuración del reloj
clock = pygame.time.Clock()

# Configuración del objeto
obj_size = 50
obj_x = screen_width // 2
obj_y = screen_height // 2
obj_speed_x = 5
obj_speed_y = 5

# Fuente para el contador de tiempo
font = pygame.font.Font(None, 36)

# Tiempo inicial
start_ticks = pygame.time.get_ticks()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del objeto
    obj_x += obj_speed_x
    obj_y += obj_speed_y

    # Evitar que el objeto se salga de la pantalla
    if obj_x < 0 or obj_x + obj_size > screen_width:
        obj_speed_x = -obj_speed_x
    if obj_y < 0 or obj_y + obj_size > screen_height:
        obj_speed_y = -obj_speed_y

    # Calcular el tiempo transcurrido
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000

    # Limpiar la pantalla
    screen.fill(MISTYROSE1)

    # Dibujar el objeto
    pygame.draw.rect(screen, ORANGE, (obj_x, obj_y, obj_size, obj_size))

    # Renderizar el tiempo en pantalla
    timer_text = font.render(f"Tiempo: {seconds} s", True, ORANGE)
    screen.blit(timer_text, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()