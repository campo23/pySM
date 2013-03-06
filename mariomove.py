import pygame
from pygame.locals import *
from Man import *

h = 480
w = 1000
f = 0
v = 0

fire = pygame.image.load("/home/andrea/Scrivania/andrea/pySM/images/fire.bmp")
img = pygame.image.load("/home/andrea/Scrivania/andrea/pySM/images/spm.bmp")
img2 = pygame.image.load("/home/andrea/Scrivania/andrea/pySM/images/spm2.bmp")
man = Man(40, 358, 0, [img, img2])
fireball = Fireball(0, 0, fire)
screen = pygame.display.set_mode((w, h))
running = 1
 
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill((0, 0, 0))  
    key = pygame.key.get_pressed()
    if (key[pygame.K_a]):
        v = 1
    if (key[pygame.K_d]):
        v = 0
    if(f == 0 and v == 1):
        fireball.v = 1
    if(f == 0 and v == 0):
        fireball.v = 0
    if(f == 0 and key[pygame.K_f]):
        f = 1
        fireball.x = man.go
        fireball.y = man.up

    if(fireball.x > 1000 or fireball.x < -50):
        f = 0

    man.move(key)
    man.jump(key)

    man.draw(screen)
    fireball.draw(screen, f)
    pygame.display.flip()
    pygame.time.wait(5)
    print fireball.v