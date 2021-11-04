# Midnight Rider

import random
import sys
import textwrap
import time
import midnight_rider_text

# A text-based game of intrigue and illusion

# CONSTANTS
MAX_FUEL = 50
MAX_TOFU = 3
MAX_HUNGER = 50

ENDGAME_REASONS = {
    "LOSE_AGENTS": 1,
    "LOSE_FUEL": 2,
    "LOSE_HUNGER": 3
}

class Game:
    """Represent our game engine

    Attribute:
        done: describes if the game is
            finished or not - bool
        distance_traveled: describe the distance
            that we've traveled so far this game
            in km
        amount_of_tofu: how much tofu we have
            left in our inventory
        agents_distance: describes the distance
            between the player and the agents
        fuel: describes the amount of fuel remaining
            starts off at 50
        hunger: describes how hungry our player is represented by a number
            between 0 and 50. If hunger goes beyond 50, game is over.
        endgame_reason: shows the index of the game ending
        text from midnight_rider_text.py
    """

    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL
        self.hunger = 0
        self.endgame_reason = 0

    def introduction(self):
        """Print the introduction text"""

        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect."""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choices(self) -> None:
        """Gets the user's choice and changes the environment"""
        # Get the user's response
        user_choice = input().strip(".,?/!").lower()


        # Based on their choice, change the attributes
        # of the class

        agents_distance_now = random.randrange(7, 15)

        if user_choice == "a":
            if self.amount_tofu > 0:
                self.amount_tofu -= 1

                self.hunger = 0

                print(midnight_rider_text.EAT_TOFU)

            else:
                # Tell the player they don't have tofu
                print(midnight_rider_text.NO_TOFU)

        elif user_choice == "b":
            player_distance_now = random.randrange(5, 10)

            self.distance_traveled += player_distance_now

            # Move the agents

            self.agents_distance += agents_distance_now - player_distance_now

            # Burn the fuel

            self.fuel -= random.randrange(3, 8)

            # Give the player some feedback
            print("-------You drive conservatively.")
            print(f"-------You traveled {player_distance_now} kms.\n")

        elif user_choice == "c":
            # Move the player
            player_distance_now = random.randrange(10, 16)

            self.distance_traveled += player_distance_now

            # Move the agents

            self.agents_distance += agents_distance_now - player_distance_now

            # Burn the fuel

            self.fuel -= random.randrange(5, 11)

            # Give the player some feedback
            print("-------ZOOOOOOOOOOOOOOOOM.")
            print(f"-------You traveled {player_distance_now} kms.\n")

        elif user_choice == "d":
            self.fuel = MAX_FUEL

            # Decide how far the agents go

            # Give the user feedback
            print(midnight_rider_text.REFUEL)
            time.sleep(2)

            self.agents_distance += agents_distance_now

        elif user_choice == "e":
            print("---Status Check---")
            print(f"Distance traveled: {self.distance_traveled} km")
            print(f"Fuel remaining: {self.fuel} L")
            print(f"Tofu Pieces left: {self.amount_tofu}")
            print(f"Agent's distance: {abs(self.agents_distance)} km behind")
            print("------")
            time.sleep(2)
        elif user_choice == "q":
            self.done = True
        time.sleep(1)

        # Increase hunger
        if user_choice in ["b", "c", "d"]:
            self.hunger += random.randrange(8,18)

    def upkeep(self) -> None:
        """Give the user reminders of hunger."""

        if self.hunger > 40:
            print(midnight_rider_text.SEVERE_HUNGER)
        elif self.hunger > 25:
           print(midnight_rider_text.HUNGER)

    time.sleep(1)

    time.sleep(1)

    def check_endgame(self) -> None:
        """Check to see if win/lose conditions are met.
        If they're met, change the self.done flag."""
        # TODO: LOSE - Agents catch up to the player

        # No elif no need to check all at once
        # Bad code cuz coupled: need to change in many different places

        if self.agents_distance >= 0:
            # Allows us to quit the while loop
            self.done = True
            # Helps with printing the right ending
            self.endgame_reason = ENDGAME_REASONS["LOSE_AGENTS"]

        if self.fuel <= 0:
            self.done = True
            self.endgame_reason = ENDGAME_REASONS["LOSE_FUEL"]

        if self.hunger > 50:
            self.done = True
            self.endgame_reason = ENDGAME_REASONS["LOSE_HUNGER"]
        # # TODO: WIN - Reach the goal
        # elif self.distance_traveled >= 100:
        #     self.done True

# main() is the function that will do all of the main stuff

# pass is a placeholder
def main() -> None:
    game = Game() # Starting a new game
    # game.introduction() # Spits out introduction

    # Main Loop
    while not game.done:
        game.upkeep()
        game.show_choices()
        game.get_choices()
        game.check_endgame()

    time.sleep(1)
    # Print out the ending.
    game.typewriter_effect(
        midnight_rider_text.ENDGAME_TEXT[game.endgame_reason]
    )

if __name__ == "__main__":
    main()