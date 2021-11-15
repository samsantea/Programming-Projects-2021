# Pygme_Drawing
# Author: Ubial
# 9 November 2021

# Get introduced to Pygame and draw objects on screen

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,  0,   0)
RED = (255, 0,  0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TAN = (218, 146, 104)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN LOOP
    while not done:
        # Make space for the event listener    """Driver of the Python script"""
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ----------- CHANGE ENVIRONMENT

        # --------------- DRAW THE ENVIRONMENT
        screen.fill(WHITE) # This is a fill with background colour
        for i in range(10):

            pygame.draw.ellipse(screen, TAN, [200, 50, 300, 250])
            pygame.draw.ellipse(screen, TAN, [160, 80, 80, 80])
            pygame.draw.ellipse(screen, TAN, [465, 80, 80, 80])
            pygame.draw.ellipse(screen, BLACK, [390, 190, 20, 20])
            pygame.draw.ellipse(screen, BLACK, [300, 190, 20, 20])
            pygame.draw.polygon(screen, BLACK, [[330, 220], [370, 220], [350, 240]])
            # pygame.draw.arc(screen, BLACK, [[310, 230], [330, 250], [350, 230]], 0,p i)

        # Update the environment
        pygame.display.flip()

        # --------------- CLOCK TICK
        clock.tick((75))


if __name__ == "__main__":
    main()