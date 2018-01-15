import pygame
from Tank import Tank

class Player(Tank):
    INIT_X = 15
    INIT_Y = 38

    def __init__(self):
        self.reset()

    def reset(self):
        x = self.INIT_X
        y = self.INIT_Y
        Tank.__init__(self, x, y)

    def display(self, G):
        pygame.draw.rect(G.screen, G.COLOR_PLAYER,
                         [(G.MARGIN + G.SIZE_POS) * self.x + G.MARGIN, (G.MARGIN + G.SIZE_POS) * self.y + G.MARGIN, G.SIZE_POS,
                          G.SIZE_POS])

    def move(self, map):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            Tank.moveLeft(self, map)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            Tank.moveRight(self, map)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            Tank.moveUp(self, map)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            Tank.moveDown(self, map)