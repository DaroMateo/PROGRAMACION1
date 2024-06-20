'''
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
    {"id": 1, "ES": "elefante", "EN": "elephant"},
    {"id": 2, "ES": "departamento", "EN": "department"},
    {"id": 3, "ES": "medicina", "EN": "medicine"},
    {"id": 4, "ES": "ingenieria", "EN": "engineering"},
    {"id": 5, "ES": "computadora", "EN": "computer"},
    {"id": 6, "ES": "dispositivo", "EN": "device"},
    {"id": 7, "ES": "software", "EN": "software"},
    {"id": 8, "ES": "hardware", "EN": "hardware"},
    {"id": 9, "ES": "idioma", "EN": "language"},
    {"id": 10, "ES": "ciudadano", "EN": "citizen"}
]

# Game variables
selected_word = None
guessed = []
attempts = 6
points = 0
game_over = False
language = None
nickname = ""
input_active = False
words_copy = WORDS.copy()

# Fonts
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

# Language selection function
def select_language():
    global language
    selecting = True
    while selecting:
        screen.fill(WHITE)
        draw_text(screen, "Select Language / Seleccione Idioma", 48, WIDTH / 2, 100)
        draw_text(screen, "Press 'E' for English or 'S' for Spanish", 36, WIDTH / 2, 200)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    language = 'EN'
                    selecting = False
                elif event.key == pygame.K_s:
                    language = 'ES'
                    selecting = False

# Nickname input function
def input_nickname():
    global nickname, input_active
    input_active = True
    input_box = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 - 25, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        nickname = text
                        done = True
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(WHITE)
        draw_text(screen, "Enter Nickname:", 48, WIDTH / 2, HEIGHT / 2 - 100)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

# Main game loop
def main_game():
    global selected_word, guessed, attempts, points, game_over, words_copy

    if not words_copy:
        draw_text(screen, f"Final Score for {nickname}: {points}", 48, WIDTH / 2, HEIGHT / 2)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        exit()

    selected_word = random.choice([word[language] for word in words_copy])
    words_copy = [word for word in words_copy if word[language] != selected_word]
    guessed = ['_' for _ in selected_word]
    attempts = 6
    game_over = False

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over and not input_active:
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

        if game_over:
            pygame.time.wait(1000)
            main_game()

        pygame.display.flip()

    pygame.quit()

# Start the game
select_language()
input_nickname()
main_game()