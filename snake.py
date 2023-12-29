import pygame
from enum import Enum, auto


class SnakeDirection(Enum):
    SD_LEFT = auto()
    SD_UP = auto()
    SD_RIGHT = auto()
    SD_DOWN = auto()


class Snake:

    def __init__(self, position: pygame.Vector2):
        self.pos = position
        self.size = pygame.Vector2(32, 32)
        self.head = pygame.Rect(self.pos, self.size)
        self.movement_delay = 30
        self.delay_left = self.movement_delay
        self.direction = SnakeDirection.SD_LEFT

    def draw(self, display: pygame.Surface):
        pygame.draw.rect(display, "white", self.head)

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction = SnakeDirection.SD_UP
        if keys[pygame.K_a]:
            self.direction = SnakeDirection.SD_LEFT
        if keys[pygame.K_s]:
            self.direction = SnakeDirection.SD_DOWN
        if keys[pygame.K_d]:
            self.direction = SnakeDirection.SD_RIGHT

        self.move()

    def move(self):

        row_offset = 0
        col_offset = 0

        if self.direction == SnakeDirection.SD_LEFT:
            row_offset = -1
        elif self.direction == SnakeDirection.SD_RIGHT:
            row_offset = 1
        elif self.direction == SnakeDirection.SD_UP:
            col_offset = -1
        elif self.direction == SnakeDirection.SD_DOWN:
            col_offset = 1

        self.delay_left -= 1
        if self.delay_left > 0:
            return

        self.head.x += self.head.width * row_offset
        self.head.y += self.head.height * col_offset

        self.delay_left = self.movement_delay
