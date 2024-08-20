import pygame
from surfaces.window import draw_word, update_window, WIN
from surfaces.images import load_images
from hangman import Hangman
from word import Word
from time import sleep

win_sound = pygame.mixer.Sound('assets/win-sound.mp3')
lose_sound = pygame.mixer.Sound('assets/burning-memories.mp3')

clock = pygame.time.Clock()

images = load_images()
hangman = Hangman()
word = Word()

run = True
FPS = 60

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            letter = chr(event.key).lower()
            guess_correct = word.guess(letter)
            hangman.update(guess_correct)
    draw_word(word.word, word.guessed)
    hangman.draw(WIN, images)
    update_window()

    if word.is_guessed():
        print("You won!")
        win_sound.play()
        sleep(2)
        run = False
    
    elif hangman.is_lost():
        print("You lost!")
        lose_sound.play()
        sleep(5)
        run = False

pygame.quit()