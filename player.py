import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    # draws player on screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)


    # checks if any keys were pressed and updates player 
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


    # updates rect for the draw function
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
