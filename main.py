import pygame
from game.game_engine import GameEngine

WIDTH, HEIGHT = 700, 500
FPS = 60
MAX_DT = 0.05  # cap frame time so a stalled window doesn't teleport objects


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Anvil Dodge - Pygame Edition")
    clock = pygame.time.Clock()

    engine = GameEngine(WIDTH, HEIGHT)

    running = True
    while running:
        dt = min(clock.tick(FPS) / 1000, MAX_DT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            engine.handle_event(event)

        engine.update(dt)
        engine.render(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()