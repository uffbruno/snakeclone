import pygame
from enum import Enum, auto
from collections import deque
from map import Map, MapObject, MapCell


class SnakeDirection(Enum):
    SD_LEFT = auto()
    SD_UP = auto()
    SD_RIGHT = auto()
    SD_DOWN = auto()


class Snake:

    def __init__(self, position: MapCell, initial_size: int):
        self.old_tail = position
        self.size = initial_size
        self.movement_delay = 20
        self.delay_left = self.movement_delay
        self.direction = SnakeDirection.SD_RIGHT

        self.head = position
        self.tail = position
        self.body = deque()
        if initial_size > 2:
            for i in range(initial_size - 2):
                self.body.append(position)

    def update(self, levelMap: Map):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction = SnakeDirection.SD_UP
        if keys[pygame.K_a]:
            self.direction = SnakeDirection.SD_LEFT
        if keys[pygame.K_s]:
            self.direction = SnakeDirection.SD_DOWN
        if keys[pygame.K_d]:
            self.direction = SnakeDirection.SD_RIGHT

        self.move(levelMap)

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
        new_row = self.head.row + row_offset
        new_col = self.head.col + col_offset

        # print(new_row, new_col)

        self.old_tail = MapCell(self.tail.row, self.tail.col)

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

        print(self.tail.row, self.tail.col, self.old_tail.row, self.old_tail.col)
