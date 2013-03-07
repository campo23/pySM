import pygame
from pygame.locals import *

class Man:
    def __init__(self, go, up, wh, imgs):
        #movement
        self.go = go
        #jump
        self.up = up
        #jump position
        self.wh = wh #0=none, 1=up, 2=down

        self.imgs = imgs
        self.index = 0
        self.fireballs = []
        self.timeNewF = 0
    
    def fire(self,v):
        if len(self.fireballs) < 1 or self.timeNewF > 50:
            self.fireballs.append(Fireball(self.go,self.up,self.imgs[2],v))
            self.timeNewF = 0
        else:
            self.timeNewF += 1
    
    def draw(self,screen):
        deleteF = []
        for f in self.fireballs:
            if f.x > 1000:
                deleteF.append(f)
            if f.x < 0:
                deleteF.append(f)
            f.draw(screen)
        screen.blit(self.imgs[self.index], (self.go-50,self.up-50))
        
        for f in deleteF:
            self.fireballs.remove(f)

    def move(self, key, rectMan, rectOst):
        rectman = rectMan
        #move the character only if it's inside the screen
        if(key[pygame.K_d] and self.go<938): 
            if(rectMan.colliderect(rectOst) != 1 or rectMan.colliderect(rectOst) == 1 and self.index == 1):
                self.go += 2
                rectman = rectMan.move(2, 0)
            self.index = 0
            
        if(key[pygame.K_a] and self.go>40):
            if(rectMan.colliderect(rectOst) != 1 or rectMan.colliderect(rectOst) == 1 and self.index == 0):
                self.go -= 2
                rectman = rectMan.move(-2, 0)
            self.index = 1
            
        return rectman

    def jump(self, key, rectMan, rectOst):
        rectman = rectMan
        if(self.wh == 0 and key[pygame.K_w]):
             self.wh = 1
        if(self.wh == 1 and self.up > 260):
             self.up -= 3
             rectman = rectMan.move(0, -3)
        if(self.wh == 1 and self.up <= 260):
             self.wh = 2
        if(self.wh == 2 and self.up < 358):
             if(rectMan.colliderect(rectOst) != 1):
                 self.up += 3
                 if(rectMan.y < 318):
                    rectman = rectMan.move(0, 3)
             else:
                 self.wh = 0
        if(self.wh == 2 and self.up >= 358):
             self.wh = 0
        return rectman

class Fireball:
    def __init__(self, x, y, fire, v):
        self.x = x
        self.y = y
        self.imgf = fire
        self.v = v

    def draw(self, screen):
        if(self.v == 0):
            self.x += 4
        elif(self.v):
            self.x -= 4
        screen.blit(self.imgf, (self.x, self.y))
