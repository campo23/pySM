import pygame
from pygame.locals import *

class Button:
    def __init__(self, color, position, size):
        self.color = color
        self.position = position
        self.size = size
        self.button = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.mouse_pos = [-1, -1]    
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.button)
    def isClicked(self): 
        if(pygame.mouse.get_pressed() == (1, 0, 0)):
            self.mouse_pos = pygame.mouse.get_pos()

            if(self.mouse_pos[0] in (range(self.position[0], self.position[0]+self.size[0])) and self.mouse_pos[1] in range(self.position[1], self.position[1]+self.size[1])):
                self.mouse_pos = [-1, -1] 
                return 1
            else:
                return 0
