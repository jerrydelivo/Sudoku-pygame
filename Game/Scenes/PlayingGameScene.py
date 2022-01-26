from unittest import result
import pygame
from Scenes.Scene import Scene
from Board.Board import Board
from Shared.GameConstants import GameConstants

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

        self.game = game
        self.Board = Board()
        self.screen = pygame.display.set_mode((800,600), 0, 32)
        self.counter = 0
        self.time = ''
        self.mouse = []
        self.key = None
        self.score = None
        self.result = None
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        self.__num_picked = pygame.image.load(GameConstants.TILE_PATH + '/' + str(0) + '.jpg')
        self.__correct = pygame.image.load(GameConstants.CORRECT_IMAGE)
        self.__wrong = pygame.image.load(GameConstants.WRONG_IMAGE)

    def render(self):
        super(PlayingGameScene, self).render()
        self.getGame().screen.blit(self.__num_picked, (600, 50))

        game = self.getGame()

        tiles = self.Board.tiles()
        
        if self.key == None or len(self.mouse) == 0:
            if self.key in range(10):
                
                self.__num_picked = pygame.image.load(GameConstants.TILE_PATH + '/' + str(self.key) + '.jpg')
            PlayingGameScene.makeboard(self, game , tiles)
            self.Board.run += 1
        elif 0 <= self.mouse[0] < 9 and 0 <= self.mouse[1] < 9:
            key = self.key
            x = self.mouse[0]
            y = self.mouse[1]
            tiles[x][y] = key
            
            self.result = PlayingGameScene.makeboard(self, game, tiles, calculate=True)
            
        if self.result in (True, False):
            if self.result == True:
                self.getGame().screen.blit(self.__correct, (550, 100))
            else:
                self.getGame().screen.blit(self.__wrong, (580, 200))
        self.mouse = []
        self.draw_cell_borders()

    def draw_cell_borders(self):
        pygame.draw.line(self.screen, (0,0,255), (75,225), (525,225), 3)
        pygame.draw.line(self.screen, (0,0,255), (75,375), (525,375), 3)

        pygame.draw.line(self.screen, (0,0,255), (375,75), (375,525), 3)
        pygame.draw.line(self.screen, (0,0,255), (225,75), (225,525), 3)

    def displaybox(self, screen):
        pygame.draw.rect(self.screen, (86, 47, 14), [50, 50, 500, 500], 25)
        

    def makeboard(self, game, tiles, calculate=False):
        bag = []
        for i in range(0, 9):
            for j in range(0, 9):
                num = tiles[i][j]
                name = GameConstants.TILE_PATH + '/' + str(num) + '.jpg'
                bag.append(name)
        numbers = []

        for i in range(0, len(bag)):
            board = pygame.image.load(bag[i])
            numbers.append(board)

        n = 0
        for i in range(0, 9):
            for j in range(0, 9):
                game.screen.blit(numbers[n], (75 + GameConstants.TILE_SIZE[0] * i, 75 + GameConstants.TILE_SIZE[1] * j))
                n = n + 1
        
        return self.Board.checkboard() if calculate else None

    def cursor(self, pos):
        x = int(pos[0])
        y = int(pos[1])
        if (x > 75 and x < 525) and (y > 75 and y <525):
            i = (x - 75) / 50
            j = (y - 75) / 50
            return (int(i), int(j))
        else:
            return pos

    def keyboard(self, key):
        if key == 256 or key == 48:
            flag = 0
        if key == 257 or key == 49:
            flag = 1
        if key == 258 or key == 50:
            flag = 2
        if key == 259 or key == 51:
            flag = 3
        if key == 260 or key == 52:
            flag = 4
        if key == 261 or key == 53:
            flag = 5
        if key == 262 or key == 54:
            flag = 6
        if key == 263 or key == 55:
            flag = 7
        if key == 264 or key == 56:
            flag = 8
        if key == 265 or key == 57:
            flag = 9
        return flag

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                if mouse[0] == 1:
                    point = PlayingGameScene.cursor(self, pos)
                    self.mouse = point

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.Board = Board()

                if event.key == pygame.K_n:
                    if self.result:
                        self.Board.next_move()

                if event.key == pygame.K_F4:
                    exit()

                key = event.key

                if (key >= 48 and key <= 57) or (key >= 256 and key <= 265):
                    final = PlayingGameScene.keyboard(self, key)

                else:
                    final = 0

                self.key = final

            if event.type == pygame.USEREVENT:
                self.counter += 1
