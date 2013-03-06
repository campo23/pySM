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

    #load images
    fire = pygame.image.load("/home/andrea/Scrivania/andrea/pySM/images/fire.bmp")
    img = pygame.image.load("/home/andrea/Scrivania/andrea/pySM/images/spm.bmp")
    img2 = pygame.image.load("/home/andrea/Scrivania/andrea/pySM/images/spm2.bmp")
    #load and play music
    pygame.mixer.init(44100, -16, 2, 2048)
    pygame.mixer.music.load("/home/andrea/Scrivania/andrea/pySM/song.mp3")
    pygame.mixer.music.play(0, 0.0)
    
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
        #if the ball isn't present in the screen, it changes
        #the direction of the ball
        if(f == 0 and v == 1):
            fireball.v = 1
        if(f == 0 and v == 0):
            fireball.v = 0
        #if the user press f key, initialize the variables
        #based on the position of the ball
        if(f == 0 and key[pygame.K_f]):
            f = 1
            fireball.x = man.go
            fireball.y = man.up

        if(fireball.x > 1000 or fireball.x < -50):
            f = 0

        man.move(key)
        man.jump(key)
        #draw the character and the ball
        man.draw(screen)
        fireball.draw(screen, f)

        pygame.display.flip()
        pygame.time.wait(5)

if __name__ == '__main__':
    exit(run())
