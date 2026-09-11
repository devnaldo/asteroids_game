import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()   
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dlt = 0.0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True: 
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dlt = clock.tick(60) / 1000 # limit the framerate to 60 FPS

        screen.fill("black") 
        player.draw(screen)
        pygame.display.flip()
        

   

if __name__ == "__main__":
    main()
