# module imports
import pygame
import playerclass
import blobclass
import gamedefs
import os

def title():
    return "Mygame, Pygame"

def checkBehind(player, blobs):
    
    result = False

    for i in range(4):
        if player.rect.center == blobs[i].rect.center:
            blobs[i].hit()
            result = True
            break

    return result

def main():
    # initialise pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((gamedefs.WIDTH,gamedefs.HEIGHT))
    pygame.display.set_caption(title())

    # create clock object to control refresh rate
    clock = pygame.time.Clock()

    # create sprite group
    all_sprites = pygame.sprite.Group()

    # starting score
    score = 0

    ########################################################
    # create player and blob objects and add to sprite group
    #

    # single player object
    player = playerclass.Player()

    # list of 4 blobs
    blobs = [   blobclass.Blob(100, 100),
                blobclass.Blob(700, 120),
                blobclass.Blob(120, 500),
                blobclass.Blob(720, 480)]

    # add to group
    all_sprites.add(player)
    all_sprites.add(blobs[0])
    all_sprites.add(blobs[1])
    all_sprites.add(blobs[2])
    all_sprites.add(blobs[3])

    # main game loop
    running = True

    pygame.font.init()

    # create font object - no name = default
    scoreFont = pygame.font.SysFont('', 50)

    while running:
        
        # wait for any remaining time in loop after 'process/update/draw' cycle
        clock.tick(gamedefs.FPS)
        
        # Process input/events
        for event in pygame.event.get():

            # close window if 'x' clicked
            if event.type == pygame.QUIT:
                running = False

            # change direction on mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.reverse()
            
            # key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.direction = "LEFT"
                if event.key == pygame.K_RIGHT:
                    player.direction = "RIGHT"
                if event.key == pygame.K_UP:
                    player.direction = "UP"
                if event.key == pygame.K_DOWN:
                    player.direction = "DOWN"
                if event.key == pygame.K_SPACE:
                    player.direction = "STOPPED"
                    if checkBehind(player, blobs):
                        player.playSound()
                        score += 10

        # Update sprites
        all_sprites.update()
        
        # Draw/render main screen and sprites
        screen.fill(gamedefs.BLACK)
        all_sprites.draw(screen)
        
        # create score text
        scoreText = "Score: %d" % score
        textsurface = scoreFont.render(scoreText, False, (255, 0, 0))
        screen.blit(textsurface, (10,10))
        
        pygame.display.flip()

    # quit pygame module
    pygame.quit()

# call main function
if __name__ == "__main__":
    main()