import json
from enum import Enum
import pygame


class MapObject(Enum):
    NOTHING = ' '
    SNAKE = '@'
    FOOD = '*'
    WALL = '#'
    TRAP = '$'
    DANGER = 'D'


class MapCell:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


class Map:
    def __init__(self):
        self.max_rows = 20
        self.max_columns = 20
        self.snake = MapCell(0, 0)

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

    def set(self, row: int, col: int, obj: MapObject):
        self.objects[row * self.max_columns + col] = obj

    def get(self, row: int, col: int) -> MapObject:
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

    def load_level(self, filename: str):
        with open(filename) as f:
            json_obj = json.load(f)

        layout = json_obj.get('level').get('layout')

        self.objects.clear()

        row_index = 0
        col_index = 0

        for row in layout:
            col_index = 0
            for obj in row:
                self.objects.append(MapObject(obj))
                if MapObject(obj) == MapObject.SNAKE:
                    self.snake = MapCell(row_index, col_index)

                col_index += 1

            row_index += 1

