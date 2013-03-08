import pygame
from pygame.locals import *
from Man import *

def run():

    pygame.init()
    start = 0
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
    
    rectPlayex = pygame.Rect(w/2-53, h/2-28, 106, 56)
    rectPlay = pygame.Rect(w/2-50, h/2-25, 100, 50)
    rectMan = pygame.Rect(man.go-35, man.up-40, 95, 160)
    rectOst = pygame.Rect(500, 430, 50, 50)

    text = pygame.font.SysFont('arial.ttf', 30)
    startText = text.render("START", True, (0,0,0))

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        
        screen.fill((0, 0, 0))  
        if(start == 0):
            pygame.draw.rect(screen, (39, 139, 34), rectPlayex)
            pygame.draw.rect(screen, (173, 255, 47), rectPlay)
            screen.blit(startText, (465, 230))
            if(pygame.mouse.get_pressed() == (1, 0, 0)):
                mouse_pos = pygame.mouse.get_pos()
                print mouse_pos
                if(mouse_pos[0] in (range(450, 550)) and mouse_pos[1] in range(215, 255)):
                    start = 1
        elif(start == 1):
            pygame.draw.rect(screen, color, rectMan)
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

            rectMan = man.move(key, rectMan, rectOst)
            rectMan = man.jump(key, rectMan, rectOst)
            #draw the character 
            man.draw(screen)

        pygame.display.flip()
        pygame.time.wait(5)

if __name__ == '__main__':
    exit(run())
