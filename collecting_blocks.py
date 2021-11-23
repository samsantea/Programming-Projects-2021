# Collecting Blocks example
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
MIDDLE_YELLOW = (247, 231, 51)
CYCLAMEN = (232, 106, 146)
AQUAMARINE = (65, 226, 186)
PURPLE = (98, 0, 179)
BGCOLOUR = WHITE

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Collecting blocks"


class Player(pygame.sprite.Sprite):
    """ Describes a block object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]"""

    def __init__(self, width: int, height: int) -> None:
        # Call the superclass contructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.transform.scale(
            pygame.image.load("./images/kirby.png"),
            (width, height)
        )

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()


class Block(pygame.sprite.Sprite):
    """ Describes a block object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]"""

    def __init__(self, colour: tuple, width: int, height: int) -> None:
        """
        Arguments:
        :param colour: 3-tuple (r, g, b)
        :param width: width in pixels
        :param height: height in pixels
        """

        # Call the superclass contructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()



def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100
    score = 0

    # Create a group of sprites to hold Sprites
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()

    # Create all the block sprites and add to block_sprites

    for i in range(num_blocks):
        # Create a block (set its parameters)
        block = Block(MIDDLE_YELLOW, 20, 15)
        # Set a random location for the block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)
        # Add the block to the block_sprites Group
        block_sprites.add(block)

        # Add the block to the all_sprites Group
        all_sprites.add(block)

    # Create the Player block
    player = Player(21, 18)

    all_sprites.add(player)

    pygame.mouse.set_visible(False)

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x, player.rect.y = mouse_pos

        # Check all collisions between player and the blocks
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites, True)

        for block in blocks_collided:
            score += 1
            print(f"Score: {score}")

        # ----------- DRAW THE ENVIRONMENT
        # Draw the background image
        screen.fill(BGCOLOUR)

        # Draw all sprites
        all_sprites.draw(screen)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()