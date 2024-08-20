import pygame

def load_images():
    images = []
    for i in range(7):
        image = pygame.image.load(f"assets/hangman{i}.png")
        images.append(image)
    return images

def draw_hangman(WIN, hangman_status, images):
    WIN.blit(images[hangman_status], (10, 10))
    pygame.display.update()