import pygame

from Scenes import *
from Shared import *
import os

class Sudoku:

    def __init__(self):
        self.__run = 0

        pygame.init()
        pygame.display.set_caption("Sudoku by Gerasimos Delivorias")

        x = 100
        y = 100
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.RESIZABLE)

        self.__scenes = (
            PlayingGameScene(self),
        )
        self.__currentScene = 0

        self.__sounds = (
            pygame.mixer.Sound(GameConstants.SOUND_FILE_GAMEOVER),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_SCREEN)
        )

    def start(self):
        while True:

            self.screen.fill((205, 235, 235))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            # currentScene.displaybox(self.screen)
            currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    def reset(self):
        self.__run = 0


Sudoku().start()
