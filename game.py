# module imports
import pygame
import playerclass
import gamedefs

def title():
    return "Mygame, Pygame"

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

    # create player object and add to sprite group
    player = playerclass.Player()
    all_sprites.add(player)

    # main game loop
    running = True

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

        # Update sprites
        all_sprites.update()
        
        # Draw/render main screen and sprites
        screen.fill(gamedefs.BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()

    # quit pygame module
    pygame.quit()

# call main function
if __name__ == "__main__":
    main()