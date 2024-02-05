import pygame
from pytmx import load_pygame


class Tile_map():
    def __init__(self, tmx_map_file):
        self.map_data = load_pygame(tmx_map_file)
        
    def draw_tile_map(self):
        screen = pygame.display.get_surface()
    
        for layer in self.map_data.visible_layers:
            for x, y, image in layer.tiles():
                screen.blit(image, (x * 32, y * 32))

    def get_tile_properties(self, x, y):
        
        try:
            properties = self.map_data.get_tile_properties(x,y,1)
        except ValueError:

            properties = {"wall":0,"floor":0}
        if properties is None:

            properties = {"wall":0, "floor":0}
        return properties