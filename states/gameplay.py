import pygame
from pygame.locals import *
from classes.player import Player
from .basestate import BaseState
class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        maze = [[0 for _ in range(20)] for _ in range(20)]
        self.player = Player(0, 0, maze)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                self.quit = True

            elif event.key == K_UP or event.key == K_w:
                self.player.move(0, -1)
     
            elif event.key == K_DOWN or event.key == K_s:
                self.player.move(0, 1)
         
            elif event.key == K_LEFT or event.key == K_a:
                self.player.move(-1, 0)
       
            elif event.key == K_RIGHT or event.key == K_d:
                self.player.move(1, 0)
       

    def draw(self, surface):
        self.player.draw(surface)