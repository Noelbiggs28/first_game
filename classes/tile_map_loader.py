import pygame
from pytmx import load_pygame

def draw_tile_map(tmx_map_file):
    screen = pygame.display.get_surface()
    tmx_map = load_pygame(tmx_map_file)
    for layer in tmx_map.visible_layers:
        for x, y, image in layer.tiles():
            screen.blit(image, (x * 32, y * 32))