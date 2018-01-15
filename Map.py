import pygame
from random import randint

class Map():
    (POS_EMPTY, POS_WALL, POS_FUEL) = range(3)

    COLOR_RED = (255, 0, 0)
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)
    COLOR_GROUND = (50, 255, 100)
    COLOR_PLAYER = (50, 50, 50)
    COLOR_FUEL = (20, 27, 229)
    COLOR_WALLS = (220, 50, 200)
    COLOR_ENEMY = COLOR_RED

    ROWS = 40
    COLS = 30
    MARGIN = 0
    SIZE_POS = 20

    RESOLUTION = [1100, 800]

    def __init__(self):
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        self.reset()

    def reset(self):
        self.grid = []
        self.walls = []
        self.fuels = []
        self.score = 0

        self.buildMap()

        return self

    def buildMap(self):
        # Define Walls - For map variation this has to be done by algorithm
        for i in range(2, 16):
            for j in range(4, 6):
                self.walls.append([i, j])

        # Distribute fuel
        self.fuels.append([12, 8])
        self.fuels.append([26, 14])
        self.fuels.append([4, 29])
        self.fuels.append([15, 15])

        # Draw empty map
        for row in range(self.ROWS):
            self.grid.append([])
            for column in range(self.COLS):
                self.grid[row].append(self.POS_EMPTY)

        # Add walls
        for wall in self.walls:
            self.grid[wall[1]][wall[0]] = self.POS_WALL

        # Add fuel
        for fuel in self.fuels:
            self.grid[fuel[1]][fuel[0]] = self.POS_FUEL

        return self


    def displayScore(self):
        scoretext = self.scorefont.render("Score: " + (str)(self.score), 1, self.COLOR_RED)
        self.screen.blit(scoretext, (610, 675))


    def displayMap(self):
        for row in range(self.ROWS):
            for column in range(self.COLS):
                color = self.COLOR_GROUND
                pygame.draw.rect(self.screen, color, [(self.MARGIN + self.SIZE_POS) * column + self.MARGIN,
                                                      (self.MARGIN + self.SIZE_POS) * row + self.MARGIN, self.SIZE_POS,
                                                      self.SIZE_POS])

                if self.grid[row][column] == 2:
                    pygame.draw.rect(self.screen, self.COLOR_FUEL, [(self.MARGIN + self.SIZE_POS) * column + self.MARGIN + 7,
                                                          (self.MARGIN + self.SIZE_POS) * row + self.MARGIN + 7,
                                                          self.SIZE_POS - 14, self.SIZE_POS - 14])

    def drawWalls(self):
        for wall in self.walls:
            pygame.draw.rect(self.screen, self.COLOR_WALLS, [(self.MARGIN + self.SIZE_POS) * wall[0] + self.MARGIN,
                                                      (self.MARGIN + self.SIZE_POS) * wall[1] + self.MARGIN, self.SIZE_POS,
                                                      self.SIZE_POS])
