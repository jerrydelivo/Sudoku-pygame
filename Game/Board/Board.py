from Shared import GameObject
from Shared import GameConstants
import random
import copy
import itertools

class Board(GameObject):

    def __init__(self):
        self.run = 0
        self.board = [[0 for _ in range(9)] for _ in range(9)]


    def tiles(self):
        if self.run == 0:
            self.board = [[0 for _ in range(9)] for _ in range(9)]

        return self.board

    def findNextCellToFill(self, grid, i, j):
        for x in range(i,9):
            for y in range(j,9):
                if grid[x][y] == 0:
                    return x,y
        for x in range(0,9):
            for y in range(0,9):
                if grid[x][y] == 0:
                    return x,y
        return -1,-1

    def isValid(self, grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
            columnOk = all([e != grid[x][j] for x in range(9)])
            if columnOk:
                # finding the top left x,y co-ordinates of the section containing the i,j cell
                secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                for x in range(secTopX, secTopX+3):
                    for y in range(secTopY, secTopY+3):
                        if grid[x][y] == e:
                            return False
                return True
        return False

    def sudoku_ok(self, line):
        return (sum(line) == sum(set(line)))

    def check_sudoku(self, grid):
        bad_rows = [row for row in grid if not self.sudoku_ok(row)]
        grid = list(zip(*grid))
        bad_cols = [col for col in grid if not self.sudoku_ok(col)]
        squares = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = list(sum(itertools.chain(row[j:j+3] for row in grid[i:i+3]),()))
                squares.append(square)
        bad_squares = [square for square in squares if not self.sudoku_ok(square)]
        return not (bad_rows or bad_cols or bad_squares)

    def solveSudoku(self, grid, i=0, j=0):
        i,j = self.findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
            if self.isValid(grid,i,j,e):
                grid[i][j] = e
                if self.solveSudoku(grid, i, j):
                    return True
                    # Undo the current cell for backtracking
                grid[i][j] = 0
        return False

    def checkboard(self):
        copy_board = copy.deepcopy(self.board)
        
        if self.check_sudoku(copy_board):
            return self.solveSudoku(copy_board)
        else:
            return False

    def update_board(self, mouse, key):
        x = mouse[0]
        y = mouse[1]
        return self.unsolve

    def newboard(self):
        self.run = 0
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def getGame(self):
        return self.__game

    def isReplaceable(self):
        return self.__tag <= 0

    