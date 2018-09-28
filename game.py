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

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    # create player object and add to sprite group
    player = playerclass.Player()
    all_sprites.add(player)

    # main game loop
    running = True

    while running:
        clock.tick(gamedefs.FPS)
        # Process input/events
        for event in pygame.event.get():

            # close window event
            if event.type == pygame.QUIT:
                running = False

            # change direction on mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.reverse()
            
            # arrow key event
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

        # Update
        all_sprites.update()
        # Draw/render
        screen.fill(gamedefs.BLACK)
        all_sprites.draw(screen)
        # screen.Draw()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()