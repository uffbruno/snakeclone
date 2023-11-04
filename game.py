import pygame


class Game:
    def run(self):
        pygame.init()

        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("palegreen2")

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                running = False
            if keys[pygame.K_w]:
                player_pos.y -= 100 * dt
            if keys[pygame.K_a]:
                player_pos.x -= 100 * dt
            if keys[pygame.K_s]:
                player_pos.y += 100 * dt
            if keys[pygame.K_d]:
                player_pos.x += 100 * dt

            pygame.draw.rect(screen, "white", (player_pos.x, player_pos.y, 40, 40))

            pygame.display.flip()
            dt = clock.tick(60) / 1000

        pygame.quit()
