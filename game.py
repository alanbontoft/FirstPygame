import pygame
import playerclass
import gamedefs




# initialise pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((gamedefs.WIDTH,gamedefs.HEIGHT))
pygame.display.set_caption("My Game, Py Game")

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = playerclass.Player()
all_sprites.add(player)

# game loop
running = True

while running:
    clock.tick(gamedefs.FPS)
    # Process input/events
    for event in pygame.event.get():

        # close window event
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    # Draw/render
    screen.fill(gamedefs.BLACK)
    all_sprites.draw(screen)
    # screen.Draw()
    pygame.display.flip()

pygame.quit()
