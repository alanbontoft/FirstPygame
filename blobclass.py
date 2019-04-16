# module imports
import pygame
import gamedefs
import math
import os


# class for player sprite
class Blob(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        # get os-independent folder name
        root_dir = os.path.dirname(__file__)
        self.img_dir = os.path.join(root_dir, "img")
        
        self.image = pygame.image.load(os.path.join(self.img_dir, gamedefs.BLOB_INIT))
        
        # set rect member to the images rect
        self.rect = self.image.get_rect()

        # set rect center to screen center
        self.rect.center = (x, y)
    
    def hit(self):
        self.image = pygame.image.load(os.path.join(self.img_dir, gamedefs.BLOB_HIT))
