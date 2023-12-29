from enum import Enum
import pygame


class MapObject(Enum):
    NOTHING = ' '
    SNAKE = '@'
    FOOD = '*'
    WALL = '#'
    TRAP = '$'
    DANGER = 'D'


class Map:
    def __init__(self):
        self.max_rows = 20
        self.max_columns = 20
        self.snake_row = 0
        self.snake_col = 0

        self.obj_map = {
                   MapObject.NOTHING: "black",
                   MapObject.SNAKE: "white",
                   MapObject.FOOD: "pink",
                   MapObject.WALL: "brown",
                   MapObject.TRAP: "black",
                   MapObject.DANGER: "black"
                  }

        self.objects = []
        for i in range(self.max_rows * self.max_columns):
            self.objects.append(MapObject.NOTHING)

        self.set(5, 5, MapObject.WALL)
        self.set(14, 10, MapObject.FOOD)

    def set(self, row: int, col: int, obj: MapObject):
        self.objects[row * self.max_columns + col] = obj

    def get(self, row: int, col: int):
        return self.objects[row * self.max_columns + col]

    def draw(self, display: pygame.Surface):
        cell_dimension = 32
        pos_x = (display.get_width() - self.max_columns * cell_dimension) / 2
        pos_y = (display.get_height() - self.max_rows * cell_dimension) / 2

        for i in range(self.max_rows):
            for j in range(self.max_columns):
                rect = pygame.Rect(pos_x, pos_y, cell_dimension, cell_dimension)
                pygame.draw.rect(display, self.obj_map[self.get(i, j)], rect)
                pos_x += cell_dimension

            pos_x = (display.get_width() - self.max_columns * cell_dimension) / 2
            pos_y += cell_dimension


