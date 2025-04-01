import pygame
import random

from gamescreen import GameState
from snakescreen import snakescreen
from gameoverscreen import gameoverscreen


class Game:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        random.seed()

        self.screen = pygame.display.set_mode((640, 640))

        self.screens = {
            GameState.INITIAL_SCREEN: None,
            GameState.OPTIONS_SCREEN: None,
            GameState.PLAYING: snakescreen(self.screen),
            GameState.PLAYER_LOST: None,
            GameState.LEVEL_CLEAR: None,
            GameState.GAME_OVER: gameoverscreen(self.screen),
            GameState.CONGRATS: None,
            GameState.ENDING_SCREEN: None,
            GameState.CREDITS: None,
            GameState.EXIT: None,
        }

        self.currentState = GameState.PLAYING

    def run(self):
        clock = pygame.time.Clock()
        running = True
        currentScreen = None
        dt = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill("palegreen2")

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                running = False

            if self.currentState != GameState.NO_CHANGE:
                currentScreen = self.screens[self.currentState]

                if currentScreen is None:
                    running = False
                    continue

            self.currentState = currentScreen.update()
            currentScreen.draw()

            pygame.display.flip()
            dt = clock.tick(60) / 1000
            print(dt)

        pygame.quit()

