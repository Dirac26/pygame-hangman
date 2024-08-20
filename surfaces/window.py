import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)

def draw_word(word, guesses):
    WIN.fill(WHITE)
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, True, BLACK)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2 + 100, HEIGHT/2 - text.get_height()/2 + 100))

def update_window():
    pygame.display.update()