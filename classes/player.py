import pygame

class Player():
    def __init__(self, x, y,min_x, max_x, color, player_number):
        self.x = x
        self.y = y
        self.cell_size = 32
        self.player_color = color
        self.min_x = min_x
        self.max_x = max_x
        self.player_image = pygame.image.load("images/player1_tiny.png") if player_number == 1 else pygame.image.load("images/player2_tiny.png")
        
    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
# check if square your trying to go to is in maze perimeter and not a wall and sets self xy there
        if self.min_x <= new_x < self.max_x and 0 <= new_y < 19:
            self.x = new_x
            self.y = new_y

# draws player
    def draw(self, surface):
        if self.x >= 0 and self.y >= 0:
            #player_rect = pygame.Rect(self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size)
            #pygame.draw.rect(surface, self.player_color, player_rect)
            surface.blit(self.player_image, (self.x * self.cell_size, self.y * self.cell_size))