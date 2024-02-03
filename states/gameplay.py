import pygame
from pygame.locals import *
from classes.player import Player
from .basestate import BaseState
class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        
        self.player1 = Player(0, 0, 0, 20, (255, 0, 0))
        self.player2 = Player(20, 0, 20, 40, (0, 255, 0))

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                self.quit = True

            elif event.key == K_UP or event.key == K_w:
                self.player1.move(0, -1)
                self.player2.move(0, -1)
            elif event.key == K_DOWN or event.key == K_s:
                self.player1.move(0, 1)
                self.player2.move(0, 1)
            elif event.key == K_LEFT or event.key == K_a:
                self.player1.move(-1, 0)
                self.player2.move(-1, 0)
       
            elif event.key == K_RIGHT or event.key == K_d:
                self.player1.move(1, 0)
                self.player2.move(1, 0)
       

    def draw(self, surface):
        self.player1.draw(surface)
        self.player2.draw(surface)