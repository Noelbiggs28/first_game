import pygame
from pygame.locals import *
from classes.player import Player
from .basestate import BaseState
class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        
        self.player1 = Player(0, 0, 0, 20, (255, 0, 0))
        self.player2 = Player(20, 0, 20, 40, (0, 255, 0))
        self.player_speed = .01  
        self.player1_moving = {'up': False, 'down': False, 'left': False, 'right': False}
        self.player2_moving = {'up': False, 'down': False, 'left': False, 'right': False}


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                self.quit = True
            elif event.key == K_w:
                self.player1_moving['up'] = False
            elif event.key == K_s:
                self.player1_moving['down'] = False
            elif event.key == K_a:
                self.player1_moving['left'] = False
            elif event.key == K_d:
                self.player1_moving['right'] = False

            elif event.key == K_UP:
                self.player2_moving['up'] = False
            elif event.key == K_DOWN:
                self.player2_moving['down'] = False
            elif event.key == K_LEFT:
                self.player2_moving['left'] = False
            elif event.key == K_RIGHT:
                self.player2_moving['right'] = False

        elif event.type == pygame.KEYDOWN:
            # Player 1 buttons
            if event.key == K_w:
                self.player1_moving['up'] = True
            elif event.key == K_s:
                self.player1_moving['down'] = True
            elif event.key == K_a:
                self.player1_moving['left'] = True
            elif event.key == K_d:
                self.player1_moving['right'] = True
            # player 2 buttons
            elif event.key == K_UP:
                self.player2_moving['up'] = True
                print('up')
            elif event.key == K_DOWN:
                self.player2_moving['down'] = True
                print('down')
            elif event.key == K_LEFT:
                self.player2_moving['left'] = True
                print('left')
            elif event.key == K_RIGHT:
                self.player2_moving['right'] = True
                print('right')

    def update(self, dt):
        # player 1 updates
        if self.player1_moving['up']:
            self.player1.move(0, -self.player_speed * dt)
        elif self.player1_moving['down']:
            self.player1.move(0, self.player_speed * dt)
        elif self.player1_moving['left']:
            self.player1.move(-self.player_speed * dt, 0)
        elif self.player1_moving['right']:
            self.player1.move(self.player_speed * dt, 0)
        # player 2 updates
        elif self.player2_moving['up']:
            self.player2.move(0, -self.player_speed * dt)
        elif self.player2_moving['down']:
            self.player2.move(0, self.player_speed * dt)
        elif self.player2_moving['left']:
            self.player2.move(-self.player_speed * dt, 0)
        elif self.player2_moving['right']:
            self.player2.move(self.player_speed * dt, 0)


    def draw(self, surface):
        self.player1.draw(surface)
        self.player2.draw(surface)