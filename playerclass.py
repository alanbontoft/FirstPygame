import pygame
import gamedefs
import math

# class for player sprite
class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        if gamedefs.USEIMAGE == 1:
            self.image = pygame.image.load(gamedefs.IMAGE)
        else:
            self.image = pygame.Surface((gamedefs.SPRITE_WIDTH, gamedefs.SPRITE_HEIGHT))
            self.image.fill(gamedefs.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (gamedefs.WIDTH / 2, gamedefs.HEIGHT / 2)
        self.direction = "STOPPED"
    
    def update(self):
        if self.direction != "STOPPED":
            
            # if at far right, change to left
            if self.direction == "RIGHT":
                if math.fabs(self.rect.right - gamedefs.WIDTH) <= gamedefs.STEP:
                    self.direction = "LEFT"
        
            # if at far left, change to right
            if self.direction == "LEFT":
                if self.rect.left <= 0:
                    self.direction = "RIGHT"

            # if at top, change to down
            if self.direction == "UP":
                if self.rect.top <= 0:
                    self.direction = "DOWN"        

            # if at bottom, change to up
            if self.direction == "DOWN":
                if math.fabs(self.rect.bottom - gamedefs.HEIGHT) <= gamedefs.STEP:
                    self.direction = "UP"

            # change approprite coordinate
            if self.direction == "UP":
                    self.rect.y -= gamedefs.STEP

            if self.direction == "DOWN":
                    self.rect.y += gamedefs.STEP

            if self.direction == "LEFT":
                    self.rect.x -= gamedefs.STEP

            if self.direction == "RIGHT":
                    self.rect.x += gamedefs.STEP

    def reverse(self):
        if self.direction == "UP":
            self.direction = "DOWN"
        elif self.direction == "DOWN":
            self.direction = "UP"
        elif self.direction == "LEFT":
            self.direction = "RIGHT"
        elif self.direction == "RIGHT":
            self.direction = "LEFT"
        