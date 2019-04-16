# module imports
import pygame
import playerclass
import blobclass
import gamedefs


def title():
    return "Mygame, Pygame"


def checkbehind(player, blobs):
    
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
    screen = pygame.display.set_mode((gamedefs.WIDTH, gamedefs.HEIGHT))
    pygame.display.set_caption(title())

    # create clock object to control refresh rate
    clock = pygame.time.Clock()

    # create sprite groups
    player_group = pygame.sprite.Group()
    blobs_group = pygame.sprite.Group()

    # starting score
    shots = 0

    ########################################################
    # create player and blob objects and add to sprite group
    #

    # single player object
    player = playerclass.Player()

    # list of 4 blobs
    blobs = [blobclass.Blob(100, 100),
             blobclass.Blob(700, 120),
             blobclass.Blob(120, 500),
             blobclass.Blob(720, 480)]

    # add to group
    player_group.add(player)

    blobs_group.add(blobs[0])
    blobs_group.add(blobs[1])
    blobs_group.add(blobs[2])
    blobs_group.add(blobs[3])

    # main game loop
    running = True

    pygame.font.init()

    # create font object - no name = default
    scorefont = pygame.font.SysFont('', 50)

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
                if (event.pos[0] > (gamedefs.WIDTH / 2)) and (event.pos[1] > (gamedefs.HEIGHT / 2)):
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
                    shots += 1
                    if checkbehind(player, blobs):
                        player.playSound()
                        # score += 10

        # Update sprites
        player_group.update()
        blobs_group.update()
        
        # Draw/render main screen and sprites
        screen.fill(gamedefs.BLACK)
        # draw ball group first, holes second
        player_group.draw(screen)
        blobs_group.draw(screen)

        # create score text
        scoretext = "Shots: %d" % shots
        textsurface = scorefont.render(scoretext, False, (255, 0, 0))
        screen.blit(textsurface, (10, 10))
        
        pygame.display.flip()

    # quit pygame module
    pygame.quit()


# call main function
if __name__ == "__main__":
    main()
