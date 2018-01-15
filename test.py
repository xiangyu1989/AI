import pygame
from random import randint
from Map import Map
from Player import Player
from Enemy import Enemy

if __name__ == "__main__":
    GAME = Map()
    HERO = Player()
    VILLIAN = Enemy()
    pygame.init()
    GAME.scorefont = pygame.font.Font(None,30)
    done = False
    clock = pygame.time.Clock()

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                        done = True

        GAME.screen.fill(GAME.COLOR_BLACK)

        HERO.move(GAME)
        VILLIAN.move(GAME)

        GAME.displayMap()
        GAME.drawWalls()
        HERO.display(GAME)
        VILLIAN.display(GAME)
        if GAME.score == 4:
            GAME.reset()
            HERO.reset()
            VILLIAN.reset()
        GAME.displayScore()
        clock.tick(10)
        pygame.display.flip()
    pygame.quit()