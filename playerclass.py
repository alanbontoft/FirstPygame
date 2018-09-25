import pygame
import gamedefs

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(gamedefs.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (gamedefs.WIDTH / 2, gamedefs.HEIGHT / 2)
        self.forward = True
    
    def update(self):
        if self.rect.x == (gamedefs.WIDTH - self.rect.width):
            self.forward = False
        
        if self.rect.x == 0:
            self.forward = True
        
        if self.forward == True:
            self.rect.x += 5
        else:
            self.rect.x -= 5