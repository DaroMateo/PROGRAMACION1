import pygame

pygame.init()

# Asegúrate de que el archivo "Pixeled.ttf" esté en la carpeta de tu proyecto
NOMBRE_FUENTE = "Pixeled.ttf"  
fuente = pygame.font.Font(NOMBRE_FUENTE, 36)  # Tamaño de la fuente de texto (36 pixeles)

# Ejemplo de uso
pantalla = pygame.display.set_mode((800, 600))
texto = fuente.render("¡Hola, Pygame!", True, (255, 255, 255))  # Texto blanco
pantalla.blit(texto, (100, 100))
pygame.display.flip()