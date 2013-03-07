import pygame
from pygame.locals import *
from Man import *

def run():

    #heigth
    h = 480
    #width
    w = 1000
    #control if the ball is on the screen
    f = 0
    #direction of the character
    v = 0

    color = (0, 255, 0)
    #load images
    fire = pygame.image.load("pySM/images/fire.bmp")
    img = pygame.image.load("pySM/images/spm.bmp")
    img2 = pygame.image.load("pySM/images/spm2.bmp")
    #load and play music
    pygame.mixer.init(44100, -16, 2, 2048)
    pygame.mixer.music.load("pySM/music/song.mp3")
    pygame.mixer.music.play(0, 0.0)
    
    man = Man(40, 358, 0, [img, img2, fire])
    screen = pygame.display.set_mode((w, h))
    
    running = 1
    
    rectMan = pygame.Rect(man.go-40, man.up-40, 105, 160)
    rectOst = pygame.Rect(500, 410, 70, 70)
     
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        
        screen.fill((0, 0, 0))  
        pygame.draw.rect(screen, (0, 0, 0), rectMan)
        pygame.draw.rect(screen, color, rectOst)
        
        if(rectOst.colliderect(rectMan)):
            if(color == (0, 255, 0)):
                color = (255, 0 ,0)
            else:
                color = (0, 255, 0)
        key = pygame.key.get_pressed()
        if (key[pygame.K_a]):
            v = 1
        if (key[pygame.K_d]):
            v = 0
        
        #if the user press f key, initialize the variables
        #based on the position of the ball
        if(key[pygame.K_f]):
            man.fire(v)

        rectMan = man.move(key, rectMan)
        man.jump(key)
        #draw the character 
        man.draw(screen)

        pygame.display.flip()
        pygame.time.wait(5)

if __name__ == '__main__':
    exit(run())
