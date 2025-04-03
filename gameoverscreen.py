import os
import pygame
from gamescreen import gamescreen, GameState

class gameoverscreen(gamescreen):
    def __init__(self, display):
        self.screen = display
        self.bg_image = pygame.image.load(os.path.join('assets', 'images', 'game-over.png'))
        self.font = pygame.font.SysFont("Comic Sans MS", 30)

    def update(self) -> GameState:
        keys = pygame.key.get_pressed()
        return GameState.NO_CHANGE

    def draw(self):
        self.screen.blit(self.bg_image, (0, 0))
