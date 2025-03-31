import pygame
from enum import Enum, auto
from collections import deque
from map import Map, MapObject, MapCell
from utilities import Utilities
from gamescreen import GameState


class SnakeDirection(Enum):
    SD_LEFT = auto()
    SD_UP = auto()
    SD_RIGHT = auto()
    SD_DOWN = auto()


class Snake:

    def __init__(self, position: MapCell, initial_size: int) -> object:
        self.old_tail = position
        self.size = initial_size
        self.movement_delay = 20
        self.delay_left = self.movement_delay
        self.direction = SnakeDirection.SD_RIGHT
        self.is_dead = False
        self.ate_food = False

        self.head = MapCell(position.row, position.col)
        self.tail = MapCell(position.row, position.col)
        self.body = deque()
        if initial_size > 2:
            for i in range(initial_size - 2):
                self.body.append(MapCell(position.row, position.col))

    def update(self, levelMap: Map):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.direction != SnakeDirection.SD_DOWN \
                and self.direction != SnakeDirection.SD_UP:
            self.direction = SnakeDirection.SD_UP
            self.delay_left = 2

        if keys[pygame.K_a] and self.direction != SnakeDirection.SD_RIGHT \
                and self.direction != SnakeDirection.SD_LEFT:
            self.direction = SnakeDirection.SD_LEFT
            self.delay_left = 2

        if keys[pygame.K_s] and self.direction != SnakeDirection.SD_DOWN \
                and self.direction != SnakeDirection.SD_UP:
            self.direction = SnakeDirection.SD_DOWN
            self.delay_left = 2

        if keys[pygame.K_d] and self.direction != SnakeDirection.SD_RIGHT \
                and self.direction != SnakeDirection.SD_LEFT:
            self.direction = SnakeDirection.SD_RIGHT
            self.delay_left = 2

        self.move(levelMap)

        if self.is_dead:
            return GameState.GAME_OVER

        return GameState.NO_CHANGE

    def move(self, levelmap: Map):

        row_offset = 0
        col_offset = 0

        if self.direction == SnakeDirection.SD_LEFT:
            col_offset = -1
        elif self.direction == SnakeDirection.SD_RIGHT:
            col_offset = 1
        elif self.direction == SnakeDirection.SD_UP:
            row_offset = -1
        elif self.direction == SnakeDirection.SD_DOWN:
            row_offset = 1

        self.delay_left -= 1
        if self.delay_left > 0:
            return

        self.body.append(MapCell(self.head.row, self.head.col))
        new_row = Utilities.correct_pos(self.head.row + row_offset, levelmap.max_rows)
        new_col = Utilities.correct_pos(self.head.col + col_offset, levelmap.max_columns)

        obj = levelmap.get(new_row, new_col)

        self.is_dead = (obj == MapObject.WALL or obj == MapObject.SNAKE)
        self.ate_food = obj == MapObject.FOOD

        self.old_tail = MapCell(self.tail.row, self.tail.col)

        if not self.ate_food:
            tail = self.body.popleft()
            self.tail = MapCell(tail.row, tail.col)

        self.head.row = new_row
        self.head.col = new_col

        self.delay_left = self.movement_delay

        self.update_map_position(levelmap)

    def update_map_position(self, levelMap: Map):
        levelMap.set(self.head.row, self.head.col, MapObject.SNAKE)

        for body in self.body:
            levelMap.set(body.row, body.col, MapObject.SNAKE)

        levelMap.set(self.tail.row, self.tail.col, MapObject.SNAKE)

        levelMap.set(self.old_tail.row, self.old_tail.col, MapObject.NOTHING)
