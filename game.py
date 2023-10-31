import pygame


class Game:
    def run(self):
        pygame.init()

        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("palegreen2")
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
