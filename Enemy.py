import pygame
from Tank import Tank
from random import randint

class Enemy(Tank):
    INIT_X = 15
    INIT_Y = 1

    def __init__(self):
        self.reset()

    def reset(self):
        x = self.INIT_X
        y = self.INIT_Y
        Tank.__init__(self, x, y)
        return self


    def display(self, G):
        pygame.draw.rect(G.screen, G.COLOR_ENEMY,
                         [(G.MARGIN + G.SIZE_POS) * self.x + G.MARGIN, (G.MARGIN + G.SIZE_POS) * self.y + G.MARGIN, G.SIZE_POS,
                          G.SIZE_POS])

    def move(self, map):
        move = randint(0, 3)
        if move == 0:
            Tank.moveLeft(self, map)
        elif move == 1:
            Tank.moveRight(self, map)
        elif move == 2:
            Tank.moveUp(self, map)
        elif move == 3:
            Tank.moveDown(self, map)