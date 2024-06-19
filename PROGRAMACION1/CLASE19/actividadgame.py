'''ahorcado =
{
    [
        {"id":1, "ES": "elefante", "EN": "elephant"},
        {"id":2, "ES": "departamento", "EN": "department"},
        {"id":3, "ES": "medicina", "EN": "medicine"},
        {"id":4, "ES": "ingenieria", "EN": "engineering"},
        {"id":5,"ES":"computadora","EN":"computer"},
        {"id":6,"ES":"dispositivo","EN":"device"},
        {"id":7,"ES":"software","EN":"software"},
        {"id":8,"ES":"hardware","EN":"hardware"},
        {"id":9,"ES":"idioma","EN":"language"},
        {"id":10,"ES":"ciudadano","EN":"citizen"}
    ]
}
Ahorcado:
A. Lista de diccionarios
B. Se elegirá el idioma a jugar, palabras en español o en inglés.
C. Se tendrán 6 intentos.
D. Cada palabra adivinada suma un punto por letra de la misma. Ejemplo: “elefante” tiene
8 puntos.
E. La figura del ahorcado será:
➢ Círculo para la cabeza.
➢ Rectángulo para el tórax.
➢ Líneas para brazos y piernas.
F. La app debe tener un botón de inicio de juego.
G. Una vez iniciado el mismo se debe colocar el nick del jugador en una caja de texto.
H. Debe tener también otro botón para cerrar el juego (No hacerlo desde la X)❌
I. Debe tener un botón para mutear / desmutear el audio. ��/��
J. Debe tener a la vista los puntos acumulados.
K. Luego de cada partida, debe guardar en un archivo los siguientes datos:
➢ Nick.
➢ Puntaje.
Debe mostrarse el top 3 de los mejores puntajes en la pantalla inicial.'''

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_NAME = pygame.font.match_font('arial')

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game')

# Load words
WORDS = [
    {"id":1, "ES": "elefante", "EN": "elephant"},
    {"id":2, "ES": "departamento", "EN": "department"},
    {"id":3, "ES": "medicina", "EN": "medicine"},
    {"id":4, "ES": "ingenieria", "EN": "engineering"},
    {"id":5, "ES": "computadora", "EN": "computer"},
    {"id":6, "ES": "dispositivo", "EN": "device"},
    {"id":7, "ES": "software", "EN": "software"},
    {"id":8, "ES": "hardware", "EN": "hardware"},
    {"id":9, "ES": "idioma", "EN": "language"},
    {"id":10, "ES": "ciudadano", "EN": "citizen"}
]

# Game variables
selected_word = random.choice(WORDS)['ES']  # Change 'ES' to 'EN' for English
guessed = ['_' for _ in selected_word]
attempts = 6
points = 0
game_over = False
font = pygame.font.Font(FONT_NAME, 36)

# Drawing functions
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_hangman(attempts):
    if attempts <= 5:
        pygame.draw.circle(screen, BLACK, (400, 200), 30, 3)  # Head
    if attempts <= 4:
        pygame.draw.rect(screen, BLACK, (385, 230, 30, 60), 3)  # Torso
    if attempts <= 3:
        pygame.draw.line(screen, BLACK, (400, 230), (350, 280), 3)  # Left Arm
    if attempts <= 2:
        pygame.draw.line(screen, BLACK, (400, 230), (450, 280), 3)  # Right Arm
    if attempts <= 1:
        pygame.draw.line(screen, BLACK, (400, 290), (350, 350), 3)  # Left Leg
    if attempts <= 0:
        pygame.draw.line(screen, BLACK, (400, 290), (450, 350), 3)  # Right Leg

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.unicode.isalpha():
                char = event.unicode.lower()
                if char in selected_word:
                    for i in range(len(selected_word)):
                        if selected_word[i] == char:
                            guessed[i] = char
                            points += 1
                else:
                    attempts -= 1

    if attempts == 0 or '_' not in guessed:
        game_over = True
    
    # Draw elements
    draw_text(screen, "Hangman Game", 48, WIDTH / 2, 20)
    draw_text(screen, f"Word: {' '.join(guessed)}", 36, WIDTH / 2, 100)
    draw_text(screen, f"Attempts Left: {attempts}", 36, WIDTH / 2, 150)
    draw_text(screen, f"Points: {points}", 36, WIDTH / 2, 200)
    draw_hangman(attempts)
    
    pygame.display.flip()

pygame.quit()