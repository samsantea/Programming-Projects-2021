# Midnight Rider

import midnight_rider_text

# A text-based game of intrigue and illusion

class Game:
    """Represent our game engine

    """

    def introduction(self):
        """Print the introduction text"""

        print(midnight_rider_text.INTRODUCTION)


# main() is the function that will do all of the main stuff
# pass is a placeholder
def main() -> None:
    game = Game() # Starting a new game
    game.introduction()

if __name__ == "__main__":
    main()