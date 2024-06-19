import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Círculo controlado con flechas del teclado y contador de tiempo")

MIDNIGHTBLUE = (25, 25, 112)
OLIVE = (128, 128, 0)

clock = pygame.time.Clock()

circle_radius = 25
circle_x = screen_width // 2
circle_y = screen_height // 2
circle_speed = 5

font = pygame.font.Font(None, 36)

start_ticks = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed
    if circle_x - circle_radius < 0:
        circle_x = circle_radius
    if circle_x + circle_radius > screen_width:
        circle_x = screen_width - circle_radius
    if circle_y - circle_radius < 0:
        circle_y = circle_radius
    if circle_y + circle_radius > screen_height:
        circle_y = screen_height - circle_radius

    seconds = (pygame.time.get_ticks() - start_ticks) // 1000

    screen.fill(MIDNIGHTBLUE)

    pygame.draw.circle(screen, OLIVE, (circle_x, circle_y), circle_radius)

    timer_text = font.render(f"Tiempo: {seconds} s", True, OLIVE)
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()