import pygame

class Player():
    def __init__(self, x, y, maze):
        self.x = x
        self.y = y
        self.cell_size = 40
        self.player_color = (255, 0, 0)
        # self.walkable_squares = [6,7]

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
# check if square your trying to go to is in maze perimeter and not a wall and sets self xy there
        if 0 <= new_x < 20 and 0 <= new_y < 20: #and self.maze[new_y][new_x] in self.walkable_squares:
            self.x = new_x
            self.y = new_y

# draws player
    def draw(self, surface):
        if self.x >= 0 and self.y >= 0:
            player_rect = pygame.Rect(self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(surface, self.player_color, player_rect)
            # surface.blit(self.player_image, (self.x * self.cell_size, self.y * self.cell_size))