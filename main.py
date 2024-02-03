import sys
import pygame

from states.menu import Menu
from states.gameplay import Gameplay
from game import Game

pygame.init()

# set screen dimensions
screen = pygame.display.set_mode((1600, 800))

# create and store all possible screens
states = {
    "MENU": Menu(),
    "GAMEPLAY": Gameplay()
}

# create game instance and pass in screen, all screeens, startings screen
game = Game(screen, states, "MENU")

# start game
game.run()

# quit game
pygame.quit()
sys.exit()