# Midnight Rider

import sys
import textwrap
import time
import midnight_rider_text

# A text-based game of intrigue and illusion

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
    """

    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_tofu = 3
        self.agents_distance = -20

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
        if user_choice == "e":
            print("---Status Check---")
            print(f"Distance traveled: {self.distance_traveled} km")
            print(f"Tofu Pieces left: {self.amount_tofu}")
            print(f"Agent's distance: {abs(self.agents_distance)} km behind")
            print("------")
            time.sleep(2)
        elif user_choice == "q":
            self.done = True


# main() is the function that will do all of the main stuff

# pass is a placeholder
def main() -> None:
    game = Game() # Starting a new game
    # game.introduction() # Spits out introduction

    # Main Loop
    while not game.done:
        game.show_choices()
        game.get_choices()
        # TODO: Check win/lose conditions

if __name__ == "__main__":
    main()