import sys
import pygame

from states.menu import Menu
from states.gameplay import Gameplay
from game import Game
from classes.network import Network
pygame.init()


clientNumber = 0
# set screen dimensions
screen = pygame.display.set_mode((1600, 896))
# screen = pygame.display.set_mode((1600, 896), pygame.FULLSCREEN | pygame.SCALED)
# create and store all possible screens
n = Network()
states = {
    "MENU": Menu(),
    "GAMEPLAY": Gameplay(n)
}

# create game instance and pass in screen, all screeens, startings screen
game = Game(screen, states, "MENU")

# start game
game.run()

# quit game
pygame.quit()
sys.exit()