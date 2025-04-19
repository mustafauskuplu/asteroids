import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE

def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)

    Player.containers = (updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        dt = clock.tick(60) / 1000

        updatable.update(dt)
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()