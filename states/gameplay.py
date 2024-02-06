import pygame
from pygame.locals import *
from classes.player import Player
from .basestate import BaseState
from classes.tile_map_loader import Tile_map

class Gameplay(BaseState):
    def __init__(self, network):
        super(Gameplay, self).__init__()
        self.tile_map = Tile_map("tilemaps/full_screen_tile_map.tmx")
        self.network = network
        startPos = self.network.read_pos(network.getPos())
        self.player1 = Player(startPos[0], startPos[1], color=(255, 0, 0), player_number=1)
        self.player2 = Player(x=30, y=10, color=(0, 255, 0), player_number=2)
        self.player_speed = .01  
        self.player1_moving = {'up': False, 'down': False, 'left': False, 'right': False}
        self.player2_moving = {'up': False, 'down': False, 'left': False, 'right': False}
        self.clock = pygame.time.Clock()

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                self.quit = True
        self.player1.move()
        #     elif event.key == K_w:
        #         self.player1_moving['up'] = False
        #     elif event.key == K_s:
        #         self.player1_moving['down'] = False
        #     elif event.key == K_a:
        #         self.player1_moving['left'] = False
        #     elif event.key == K_d:
        #         self.player1_moving['right'] = False

        #     elif event.key == K_UP:
        #         self.player2_moving['up'] = False
        #     elif event.key == K_DOWN:
        #         self.player2_moving['down'] = False
        #     elif event.key == K_LEFT:
        #         self.player2_moving['left'] = False
        #     elif event.key == K_RIGHT:
        #         self.player2_moving['right'] = False

        # elif event.type == pygame.KEYDOWN:
        #     # Player 1 buttons
        #     if event.key == K_w:
        #         self.player1_moving['up'] = True
                
        #     if event.key == K_s:
        #         self.player1_moving['down'] = True
        #     if event.key == K_a:
        #         self.player1_moving['left'] = True
        #     if event.key == K_d:
        #         self.player1_moving['right'] = True
        #     # player 2 buttons
        #     if event.key == K_UP:
        #         self.player2_moving['up'] = True
       
        #     if event.key == K_DOWN:
        #         self.player2_moving['down'] = True
         
        #     if event.key == K_LEFT:
        #         self.player2_moving['left'] = True
        
        #     if event.key == K_RIGHT:
        #         self.player2_moving['right'] = True
         

    def update(self, dt):
        self.clock.tick(60)
        p2Pos = self.network.read_pos(self.network.send(self.network.make_pos((self.player1.x, self.player1.y))))
        self.player2.x = p2Pos[0]
        self.player2.y = p2Pos[1]
        self.player2.update()
    #     # player 1 updates
    #     if self.player1_moving['up']:
    #         self.player1.move(0, -.3)
    #     if self.player1_moving['down']:
    #         self.player1.move(0, .3)
    #     if self.player1_moving['left']:
    #         self.player1.move(-.3, 0)
    #     if self.player1_moving['right']:
    #         self.player1.move(.3, 0)
    #     # player 2 updates
    #     if self.player2_moving['up']:
    #         self.player2.move(0, -.3)
    #     if self.player2_moving['down']:
    #         self.player2.move(0, .3)
    #     if self.player2_moving['left']:
    #         self.player2.move(-.3, 0)
    #     if self.player2_moving['right']:
    #         self.player2.move(.3, 0)


    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.tile_map.draw_tile_map()
        self.player1.draw(surface)
        self.player2.draw(surface)
        pygame.display.flip()