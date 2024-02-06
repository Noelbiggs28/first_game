import pygame
from .tile_map_loader import Tile_map
class Player():
    def __init__(self, x, y,color, player_number):
        self.tile_map = Tile_map("tilemaps/full_screen_tile_map.tmx")
        self.x = x
        self.y = y
        self.cell_size = 32
        self.player_color = color
        self.player_image = pygame.image.load("images/player1_tiny.png") if player_number == 1 else pygame.image.load("images/player2_tiny.png")
        self.vel = 1
        self.position = (x,y)
        
# draws player
    def draw(self, surface):
        #player_rect = pygame.Rect(self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size)
        #pygame.draw.rect(surface, self.player_color, player_rect)
        surface.blit(self.player_image, (self.x * self.cell_size, self.y * self.cell_size))
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.pos = (self.x, self.y)
     
# # check if square your trying to go to is in maze perimeter and not a wall and sets self xy there
#         if 0 <= new_x < 45 and 0 <= new_y < 30 and next_square['wall']==0:
#             self.x = new_x
#             self.y = new_y