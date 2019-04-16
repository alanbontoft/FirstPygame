# module imports
import pygame
import gamedefs
import math
import os


# class for player sprite
class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # get os-independant folder name
        root_dir = os.path.dirname(__file__)
        img_dir = os.path.join(root_dir, "img")
        sound_dir = os.path.join(root_dir, "sound")

        # use image or plain rectangle
        if gamedefs.USEIMAGE == 1:
            self.image = pygame.image.load(os.path.join(img_dir, gamedefs.IMAGE))
        else:
            self.image = pygame.Surface((gamedefs.SPRITE_WIDTH, gamedefs.SPRITE_HEIGHT))
            self.image.fill(gamedefs.GREEN)
        
        # set rect member to the images rect
        self.rect = self.image.get_rect()

        # set rect center to screen center
        self.rect.center = (gamedefs.WIDTH / 2, gamedefs.HEIGHT / 2)
        
        # set direction member to 'STOPPED'
        self.direction = "STOPPED"

        # create a sound object member and load the file
        self.Sound = pygame.mixer.Sound(os.path.join(sound_dir, gamedefs.SOUNDFILE))
    
    def update(self):
        if self.direction != "STOPPED":
            
            # if at far right, change to left
            if self.direction == "RIGHT":
                if math.fabs(self.rect.right - gamedefs.WIDTH) <= gamedefs.STEP:
                    self.direction = "LEFT"
                    # self.Sound.play()
        
            # if at far left, change to right
            elif self.direction == "LEFT":
                if self.rect.left <= 0:
                    self.direction = "RIGHT"
                    # self.Sound.play()

            # if at top, change to down
            elif self.direction == "UP":
                if self.rect.top <= 0:
                    self.direction = "DOWN"        
                    # self.Sound.play()

            # if at bottom, change to up
            elif self.direction == "DOWN":
                if math.fabs(self.rect.bottom - gamedefs.HEIGHT) <= gamedefs.STEP:
                    self.direction = "UP"
                    # self.Sound.play()

            # change approprite coordinate
            if self.direction == "UP":
                    self.rect.y -= gamedefs.STEP

            elif self.direction == "DOWN":
                    self.rect.y += gamedefs.STEP

            elif self.direction == "LEFT":
                    self.rect.x -= gamedefs.STEP

            elif self.direction == "RIGHT":
                    self.rect.x += gamedefs.STEP

    # reverse the current direction
    def reverse(self):
        if self.direction == "UP":
            self.direction = "DOWN"
        elif self.direction == "DOWN":
            self.direction = "UP"
        elif self.direction == "LEFT":
            self.direction = "RIGHT"
        elif self.direction == "RIGHT":
            self.direction = "LEFT"

    def playSound(self):
        self.Sound.play()
        
