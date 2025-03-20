import pygame
from pygame import Surface

from gamescreen import gamescreen, GameState
from map import Map, MapCell
from snake import Snake


class snakescreen(gamescreen):

    def __init__(self, display):
        self.player = Snake(MapCell(7, 7), 3)
        self.display = display
        self.levelMap = Map()
        self.gameOver = False

    def init(self, display: Surface):
        player = Snake(MapCell(7, 7), 3)
        display = display
        levelMap = Map()
        gameOver = False

    def update(self) -> GameState:
        if self.gameOver:
            return GameState.GAME_OVER

        self.handle_input()
        self.player.update(self.levelMap)
        return GameState.NO_CHANGE

    def draw(self):
        self.levelMap.draw(self.display)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            gameOver = True

    def reset(self):
        pass
