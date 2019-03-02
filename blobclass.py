# module imports
import pygame
import gamedefs
import math

# class for player sprite
class Blob(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(gamedefs.BLOB)
        
        # set rect member to the images rect
        self.rect = self.image.get_rect()

        # set rect center to screen center
        self.rect.center = (x, y)
