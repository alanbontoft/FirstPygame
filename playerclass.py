import pygame
import gamedefs

# class for player sprite
class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(gamedefs.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (gamedefs.WIDTH / 2, gamedefs.HEIGHT / 2)
        self.direction = "STOPPED"
    
    def update(self):
        if self.direction != "STOPPED":
            
            # if at far right, change to left
            if self.direction == "RIGHT":
                if self.rect.x == (gamedefs.WIDTH - self.rect.width):
                    self.direction = "LEFT"
        
            # if at far left, change to right
            if self.direction == "LEFT":
                if self.rect.x == 0:
                    self.direction = "RIGHT"

            # if at top, change to down
            if self.direction == "UP":
                if self.rect.y == 0:
                    self.direction = "DOWN"        

            # if at bottom, change to up
            if self.direction == "DOWN":
                if self.rect.y == (gamedefs.HEIGHT - self.rect.height):
                    self.direction = "UP"

            # change approprite coordinate
            if self.direction == "UP":
                    self.rect.y -= 5

            if self.direction == "DOWN":
                    self.rect.y += 5

            if self.direction == "LEFT":
                    self.rect.x -= 5

            if self.direction == "RIGHT":
                    self.rect.x += 5

    def reverse(self):
        if self.direction == "UP":
            self.direction = "DOWN"
        elif self.direction == "DOWN":
            self.direction = "UP"
        elif self.direction == "LEFT":
            self.direction = "RIGHT"
        elif self.direction == "RIGHT":
            self.direction = "LEFT"
        