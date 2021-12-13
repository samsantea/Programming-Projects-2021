# Collecting Blocks example
# Author: Sam
# 2021 Version

import time
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
WINDOW_TITLE  = "Kirby Invaders"


class Player(pygame.sprite.Sprite):
    """ Describes a block object
    A subclass of pygame.sprite.Sprite

    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
        hp: describe how much
            health our player has
    """

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

        # Initial hp
        self.hp = 25

    def hp_remaining(self) -> int:
        """Return the percent of health remaining"""
        return self.hp / 25

class Enemy(pygame.sprite.Sprite):
    """The enemy sprites

    Attributes:
        image: Surface that is the visual representation
        rect: (x, y, width, height)
        x_vel: x velocity
        y_vel: y velocity
    """
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale(
            pygame.image.load("./images/spaceinvaders.png"),
            (56, 40)
        )

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH - self.rect.width),
            random.randrange(SCREEN_HEIGHT - self.rect.height)
        )

        # Define the initial velocity

        self.x_vel = random.choice([-4, -3, 3, 4])
        self.y_vel = random.choice([-4, -3, 3, 4])

    def update(self):
        """Calculate movement"""
        # Update the x-coordinate
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Constrain movement
        # X -
        if self.rect.left < 0:
            self.rect.x = 0
            self.x_vel = -self.x_vel
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = -self.x_vel
        # Y -
        if self.rect.y < 0:
            self.rect.y = 0
            self.y_vel = -self.y_vel
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel

class Bullet(pygame.sprite.Sprite):
    """Bullet

    Attributes:
        image: visual representation
        rect: mathematical representation (hit box)
        vel_y: y velocity in px/sec"""

    def __init__(self, coords: tuple):
        """

        Arguments:
            coords: tuple of (x,y) to represent initial location
        """

        super().__init__()

        self.image = pygame.Surface((5, 10))
        self.image.fill(MIDDLE_YELLOW)

        self.rect = self.image.get_rect()

        # Set the middle of the bullet to be at coords
        self.rect.center = coords

        self.vel_y = 5

    def update(self):
        self.rect.y -= self.vel_y

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_enemies = 15
    score = 0
    time_start = time.time()
    time_invincible = 5     # seconds
    game_state = "running"
    endgame_cooldown = 5        # seconds
    time_ended = 0.0

    endgame_messages = {
        "win": "Congratulations, you won!",
        "lose": "Sorry, they got you. Play again!",

    }

    font = pygame.font.SysFont("Arial", 25)

    # Create a group of sprites to hold Sprites
    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()

    # Create all the block sprites and add to block_sprites

    for i in range(num_enemies):
        # Create an enemy
        enemy = Enemy()
        # Add it to the sprites list (enemy_sprites and all_sprites)
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)

    # Create the Player block
    player = Player(50,48)

    all_sprites.add(player)

    pygame.mouse.set_visible(False)

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONUP:
                # Create a bullet
                # We can't create a bullet when:
                # Initial cooldown
                # There are 3 bullets on screen
                if len(bullet_sprites) < 3 and time.time() - time_start > time_invincible and game_state == "running":
                    time_bullet =  time.time()
                    bullet = Bullet(player.rect.midtop)
                    all_sprites.add(bullet)
                    bullet_sprites.add(bullet)


        # End-game listener
        # Order of conditions matters

        if len(enemy_sprites) == 0:
            game_state = "won"

            if time_ended == 0:
                time_ended = time.time()

            # Set parameters to keep the screen alive

            # Wait 4 seconds to kill the screen
            if time.time() - time_ended >= endgame_cooldown:
                done = True


        if player.hp_remaining() < 0:
            game_state = "lost"

            if time_ended == 0:
                time_ended = time.time()

            # Set parameters to keep the screen alive

            # Wait 4 seconds to kill the screen
            if time.time() - time_ended >= endgame_cooldown:
                done = True

        # ----------- CHANGE ENVIRONMENT

        all_sprites.update()

        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x, player.rect.y = mouse_pos[0] - player.rect.width / 2, mouse_pos[1] - player.rect.height / 2

        # Check all collisions between player and the blocks

        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)

        # Set a time for invincibility at the beginning of the game
        if time.time() - time_start > time_invincible and game_state == "running":

            for enemy in enemies_collided:
                player.hp -= 1

        # Check bullet collisions with enemies
        # Kill the bullets when they've left the screen
        for bullet in bullet_sprites:
            enemies_bullet_collided = pygame.sprite.spritecollide(
                bullet,
                enemy_sprites,
                True)

            # If the bullet has struck some enemy
            if len(enemies_bullet_collided) > 0:
                bullet.kill()
                score += 1

            if bullet.rect.y < 0:
                bullet.kill()

        # ----------- DRAW THE ENVIRONMENT
        # Draw the background image
        screen.fill(BGCOLOUR)

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw a health bar
        # Draw the background rectangle
        pygame.draw.rect(screen, AQUAMARINE, [580, 5, 215, 20])

        # Draw the foreground rectangle which represents the remaining health
        life_remaining = 215 - int(215 * player.hp_remaining())

        # Keeps bar at proper length
        if life_remaining > 215:
            life_remaining = 215

        pygame.draw.rect(screen, CYCLAMEN, [580, 5, life_remaining, 20])

        # Draw the score on the screen

        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5, 5)
        )

        if time.time() - time_start <= time_invincible:
            screen.blit(
                font.render("Welcome to Kirby Invaders!", True, BLACK),
                (SCREEN_WIDTH / 3.5, SCREEN_HEIGHT / 3)
            )

            screen.blit(
                font.render("Shoot and evade the invaders to win!",
                            True, BLACK),
                (SCREEN_WIDTH / 5, SCREEN_HEIGHT / 2.5)
            )

        # if we've won, draw the text on the screen
        if game_state == "won":
            screen.blit(
                font.render(endgame_messages["win"], True, AQUAMARINE),
                (SCREEN_WIDTH / 3.5, SCREEN_HEIGHT / 2.5)
            )
        elif game_state == "lost":
            screen.blit(
                font.render(endgame_messages["lose"], True, CYCLAMEN),
                (SCREEN_WIDTH / 3.5, SCREEN_HEIGHT / 2.5)
            )

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()