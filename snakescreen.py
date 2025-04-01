import pygame
import random

from pygame import Surface

from gamescreen import gamescreen, GameState
from map import Map, MapCell, MapObject
from snake import Snake


class snakescreen(gamescreen):

    def init(self, display: Surface):
        pass

    def __init__(self, display):
        self.display = display
        self.levelMap = Map()
        self.gameOver = False
        self.levelMap.load_level("assets\\level1.json")
        self.player = Snake(self.levelMap.snake, 3)

        self.generate_new_food()

    def update(self) -> GameState:
        if self.gameOver:
            return GameState.GAME_OVER

        if self.player.ate_food:
            self.generate_new_food()
            self.player.ate_food = False

        self.handle_input()
        return self.player.update(self.levelMap)

    def draw(self):
        self.levelMap.draw(self.display)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.gameOver = True

    def reset(self):
        self.player = Snake(MapCell(7, 7), 3)
        self.gameOver = False

    def generate_new_food(self):
        while True:
            new_row = random.randint(0, self.levelMap.max_rows - 1)
            new_col = random.randint(0, self.levelMap.max_columns - 1)

            if self.valid_food_position(new_row, new_col):
                break

        self.levelMap.set(new_row, new_col, MapObject.FOOD)

    def valid_food_position(self, row: int, col: int) -> bool:
        obj = self.levelMap.get(row, col)

        return obj == MapObject.NOTHING or obj == MapObject.DANGER
