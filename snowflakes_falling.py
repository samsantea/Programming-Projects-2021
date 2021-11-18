# Relaxing Snowscape
# Author: Sam
# 2021 Version

import random
import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = BLACK

SCREEN_WIDTH  = 960
SCREEN_HEIGHT = 540
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Relaxing Snowscape"

class Snowflake:
    """Represents a snowflake on screen.

    Attributes:
        size: radius of snowflake in px
        coords: {x: int, y: int}
        y_vel: falling velocity in px/sec
        colour: (r, g, b) tuple
    """

    def __init__(self):
        self.size = 2

        # randomly place the snow on the screen
        self.coords = [
            random.randrange(0, SCREEN_WIDTH),
            random.randrange(0, SCREEN_HEIGHT)
        ]

        # self.x_vel = random.randrange(-1, 1)
        self.y_vel = 2
        self.colour = WHITE

    def update(self):
        """Update the location of the snow"""

        self.coords[1] += self.y_vel
        # self.coords[0] += self.x_vel

        # reset position of snowflake if it reaches bottom
        if self.coords[1] == SCREEN_HEIGHT:
            self.coords = [
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(-15, 0)
            ]
        # TODO: IF self.coords[0] == SCREEN_WIDTH
        else:
            pass

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_snowflakes = 250
    snowflakes = []

    # Create snowflakes in foreground
    snowflakes = []
    for i in range(100):
        close_snowflake = Snowflake()
        close_snowflake.size = 3
        close_snowflake.y_vel = 3
        snowflakes.append(close_snowflake)

    # Create snowflakes in background

    for i in range(num_snowflakes):
        snowflakes.append(Snowflake())

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT

        for snow in snowflakes:
            snow.update()

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        # draw the snowflakes

        for snow in snowflakes:
            pygame.draw.circle(screen, snow.colour, snow.coords, snow.size)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()