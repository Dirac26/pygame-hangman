from surfaces.images import draw_hangman

class Hangman:
    def __init__(self):
        self.status = 0
    
    def update(self, guess_correct):
        if not guess_correct:
            self.status += 1

    def draw(self, WIN, images):
        draw_hangman(WIN, self.status, images)

    def is_lost(self):
        return self.status >= 6