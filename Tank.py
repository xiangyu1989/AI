class Tank():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def checkWall(self, x, y, walls):
        if [x, y] in walls:
            return True
        else:
            return False

    def collectFuel(self, map):
        if map.grid[self.y][self.x] == map.POS_FUEL:
            map.grid[self.y][self.x] = map.POS_EMPTY
            map.score += 1
            return True
        else:
            return False

    def moveLeft(self, map):
        if self.x > 0:
            if self.checkWall(self.x - 1, self.y, map.walls):
                self.x = self.x
            else:
                self.x = (self.x) - 1

        self.collectFuel(map)
        return self

    def moveRight(self, map):
        if self.x < map.COLS - 1:
            if self.checkWall(self.x + 1, self.y, map.walls):
                self.x = self.x
            else:
                self.x = (self.x) + 1

        self.collectFuel(map)
        return self

    def moveUp(self, map):
        if self.y > 0:
            if self.checkWall(self.x, self.y - 1, map.walls):
                self.y = self.y
            else:
                self.y = (self.y) - 1

        self.collectFuel(map)
        return self

    def moveDown(self, map):
        if self.y < map.ROWS - 1:
            if self.checkWall(self.x, self.y + 1, map.walls):
                self.y = self.y
            else:
                self.y = (self.y) + 1

        self.collectFuel(map)
        return self