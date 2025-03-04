import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    pygame.init()

    # Setup screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # Welcome messages
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Clock
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)


if __name__ == "__main__":
    main()
