import pygame
from pytmx import load_pygame

def draw_tile_map(tmx_map_file):
    screen = pygame.display.get_surface()
    tmx_map = load_pygame(tmx_map_file)
    for layer in tmx_map.visible_layers:
        for x, y, image in layer.tiles():
            screen.blit(image, (x * 32, y * 32))

def get_tile_properties(tmx_map_file, x, y):
    tmx_map = load_pygame(tmx_map_file)
    try:
        properties = tmx_map.get_tile_properties(x,y,0)
    except ValueError:

        properties = {"wall":0,"floor":0}
    if properties is None:

        properties = {"wall":0, "floor":0}
    return properties