import pygame

import Level
from Scenes import *
from Shared import *
import os

class Sudoku:

    def __init__(self):
        # self.__score = 0
        # self.__time = ''
        self.__run = 0

        pygame.init()
        # pygame.mixer.init()
        pygame.display.set_caption("Sudoku by Gerasimos Delivorias")

        # self.__clock = pygame.time.Clock()
        x = 100
        y = 100
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.RESIZABLE)

        self.__scenes = (
            PlayingGameScene(self),
        )
        self.__currentScene = 0

        self.__sounds = (
            pygame.mixer.Sound(GameConstants.SOUND_FILE_CLICK),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_GAMEOVER),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_SCREEN)
        )

    def start(self):
        while True:
            # self.__clock.tick(100)

            self.screen.fill((205, 235, 235))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            # currentScene.displaybox(self.screen)
            currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene


    # def getLevel(self):
    #     return self.__level

    # def getScore(self):
    #     return self.__time

    # def getTime(self):
    #     return self.__time

    # def setTime(self, time):
    #     self.__time = time

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

    # def reduceTime(self):
    #     self.__time += 1

    def reset(self):
        self.__run = 0


Sudoku().start()
