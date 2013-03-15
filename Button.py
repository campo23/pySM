import pygame
from pygame.locals import *

class Button:
    def __init__(self, position, size):
        self.colorIn = (124, 252, 0)
        self.colorMid = (0, 128, 0)
        self.colorEx = (50, 205, 50)
        self.position = position
        self.size = size
        self.buttonIn = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.buttonMid = pygame.Rect(self.position[0]-3, self.position[1]-3, self.size[0]+6, self.size[1]+6)
        self.buttonEx = pygame.Rect(self.position[0]-6, self.position[1]-6, self.size[0]+12, self.size[1]+12)
        self.mouse_pos = [-1, -1]    
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.colorEx, self.buttonEx)
        pygame.draw.rect(screen, self.colorMid, self.buttonMid)
        pygame.draw.rect(screen, self.colorIn, self.buttonIn)
        
        
    def isClicked(self): 
        if(pygame.mouse.get_pressed() == (1, 0, 0)):
            self.mouse_pos = pygame.mouse.get_pos()

            if(self.mouse_pos[0] in (range(self.position[0], self.position[0]+self.size[0])) and self.mouse_pos[1] in range(self.position[1], self.position[1]+self.size[1])):
                self.mouse_pos = [-1, -1] 
                return 1
            else:
                return 0
