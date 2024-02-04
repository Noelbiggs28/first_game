import pygame
from classes.tile_map_loader import get_tile_properties
class Player():
    def __init__(self, x, y,color, player_number):
        self.x = x
        self.y = y
        self.cell_size = 32
        self.player_color = color
        self.player_image = pygame.image.load("images/player1_tiny.png") if player_number == 1 else pygame.image.load("images/player2_tiny.png")
        
    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        # next_x = self.x + dx*32
        # next_y = self.y + dx*32
        # next_square = get_tile_properties("tilemaps/first_tile_map.tmx",new_x,new_y)

# check if square your trying to go to is in maze perimeter and not a wall and sets self xy there
        if 0 <= new_x < 40 and 0 <= new_y < 20: #and next_square['wall']==0:
            self.x = new_x
            self.y = new_y
# draws player
    def draw(self, surface):
        if self.x >= 0 and self.y >= 0:
            #player_rect = pygame.Rect(self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size)
            #pygame.draw.rect(surface, self.player_color, player_rect)
            surface.blit(self.player_image, (self.x * self.cell_size, self.y * self.cell_size))