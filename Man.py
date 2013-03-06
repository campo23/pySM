import pygame
from pygame.locals import *

class Man:
    def __init__(self, go, up, wh, imgs):
        #movimento
        self.go = go
        #salto
        self.up = up
        #posizione salto
        self.wh = wh #0=none, 1=up, 2=down

	self.imgs = imgs
	self.index = 0
    
    def draw(self,screen):
	    screen.blit(self.imgs[self.index], (self.go-50,self.up-50))

    def move(self, key):
        if(key[pygame.K_d] and self.go<938): 
            self.go += 2
            self.index = 0
        if(key[pygame.K_a] and self.go>40):
            self.go -= 2
            self.index = 1

    def jump(self, key):
        if(self.wh == 0 and key[pygame.K_w]):
             self.wh = 1
        if(self.wh == 1 and self.up > 280):
             self.up -= 3
        if(self.wh == 1 and self.up <= 280):
             self.wh = 2
        if(self.wh == 2 and self.up < 358):
             self.up += 3
        if(self.wh == 2 and self.up >= 358):
             self.wh = 0

class Fireball:
    def __init__(self, x, y, fire):
        self.x = x
        self.y = y
        self.imgf = fire
        self.v = 0

    def draw(self, screen, f):
        if(f == 1):
            if(self.v == 0):
                self.x += 4
            elif(self.v):
                self.x -= 4
            screen.blit(self.imgf, (self.x, self.y))
