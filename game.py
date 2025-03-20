import pygame

from gamescreen import GameState
from snake import Snake
from snakescreen import snakescreen
from map import Map, MapCell


class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 640))

        self.screens = {
            GameState.PLAYING: snakescreen(self.screen),
        }

        self.currentState = GameState.PLAYING

    def run(self):

        clock = pygame.time.Clock()
        running = True
        dt = 0

        player = Snake(MapCell(7, 7), 3)
        levelMap = Map()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill("palegreen2")

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                running = False

            currentScreen = self.screens[self.currentState]
            currentScreen.update()
            currentScreen.draw()

            pygame.display.flip()
            dt = clock.tick(60) / 1000

        pygame.quit()
