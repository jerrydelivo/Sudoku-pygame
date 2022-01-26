from Shared import GameObject
from Shared import GameConstants


class Board(GameObject):

    def __init__(self):
        self.run = 0
        self.last_move = []
        self.board = [[0 for _ in range(9)] for _ in range(9)]


    def tiles(self):
        if self.run == 0:
            self.board = [[0 for _ in range(9)] for _ in range(9)]

        return self.board

    def checkboard(self, puzzle):
        n = len(puzzle)
        for row in puzzle:
            i = 1
            while i <= n:
                if i not in row:
                    return False
                i += 1
        j = 0
        transpose = []
        temp_row = []
        while j < n:
            for row in puzzle:
                temp_row.append(row[j])
            transpose.append(temp_row)
            temp_row = []
            j += 1
        for row in transpose:
            i = 1
            while i <= n:
                if i not in row:
                    return False
                i += 1
        return True

    def update_board(self, mouse, key):
        x = mouse[0]
        y = mouse[1]
        self.last_move = [x,y]
        return self.unsolve

    def newboard(self):
        self.run = 0
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def getGame(self):
        return self.__game

    def isReplaceable(self):
        return self.__tag <= 0

    