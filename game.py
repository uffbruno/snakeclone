import pygame

from snake import Snake
from map import Map


class Game:

    def __init__(self):
        pass

    @staticmethod
    def run():
        pygame.init()

        screen = pygame.display.set_mode((640, 640))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        player = Snake(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2))
        map = Map()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("palegreen2")

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                running = False

            map.draw(screen)

            player.update()
            player.draw(screen)


            pygame.display.flip()
            dt = clock.tick(60) / 1000

        pygame.quit()
