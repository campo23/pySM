import pygame
from pygame.locals import *

class Man:
    def __init__(self, go, up, wh,imgs):
        #movimento
        self.go = go
        #salto
        self.up = up
        #posizione salto
        self.wh = wh #0=none, 1=up, 2=down
	self.imgs = imgs
	self.index = 0
    
    def draw(self,screen):
	screen.blit(self.imgs[self.index],(self.go-50,self.up-50))

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
        if(self.wh == 1 and self.up > 300):
             self.up -= 4
        if(self.wh == 1 and self.up <= 300):
             self.wh = 2
        if(self.wh == 2 and self.up < 358):
             self.up += 4
        if(self.wh == 2 and self.up >= 358):
             self.wh = 0

h = 480
w = 1000



img = pygame.image.load("/home/andrea/Scrivania/andrea/pySM/spm.bmp")
img2 = pygame.image.load("/home/andrea/Scrivania/andrea/pySM/spm2.bmp")
man = Man(40, 358, 0,[img,img2])
screen = pygame.display.set_mode((w, h))
running = 1
 
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill((0, 0, 0))  
    key = pygame.key.get_pressed()
    man.move(key)
    man.jump(key)

    man.draw(screen)
    pygame.display.flip()
    pygame.time.wait(10)
