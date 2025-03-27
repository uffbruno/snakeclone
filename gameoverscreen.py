import pygame
from gamescreen import gamescreen, GameState


class gameoverscreen(gamescreen):
    def __init__(self, display):
        self.screen = display
        self.font = pygame.font.SysFont("Comic Sans MS", 30)

    def update(self) -> GameState:
        keys = pygame.key.get_pressed()
        return GameState.NO_CHANGE

    def draw(self):
        text_display = self.font.render("GAME OVER", False, (0, 0, 0))
        self.screen.blit(text_display, (320, 320))
