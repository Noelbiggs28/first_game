import pygame
from .basestate import BaseState

class Menu(BaseState):
    def __init__(self):
        super(Menu, self).__init__()
        self.active_index = 0
        self.options = ["Start Game", "Quit Game"]
        self.next_state = "GAMEPLAY"

    def render_text(self, index):
        color = pygame.Color("white")
        return self.font.render(self.options[index], True, color)
    
    def get_text_position(self, text, index):
        center = (self.screen_rect.centerx, self.screen_rect.centery + (index * 50))
        return text.get_rect(center=center)
    
    def handle_action(self, index):
        if index == 0:
            self.next_state = "GAMEPLAY"
            self.done = True
        elif index ==1:
            self.quit = True

    def handle_click(self, mouse_pos):
        for index, option in enumerate(self.options):
            text_position = self.get_text_position(self.render_text(index), index)
            if text_position.collidepoint(mouse_pos):
                self.handle_action(index)
                break

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.handle_click(pygame.mouse.get_pos())

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            text_position = self.get_text_position(text_render, index)

            if text_position.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(surface, pygame.Color("red"), text_position)
            else:
                pygame.draw.rect(surface, pygame.Color("black"), text_position)

            surface.blit(text_render, text_position)