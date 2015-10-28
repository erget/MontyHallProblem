#!/usr/local/bin/python3
# encoding: utf-8

"""Step right up!"""

# sys.path.append("/home/dlee/development/eclipse/goatTest/goat_test")

from random import randint
from prizes import Goat, Car


class Game(object):
    
    """A game that proves that statistics can work in the real world."""
    
    def __init__(self, ndoors=3):
        """
        Setup game.

        Initialize doors with Goats, then replace a random door with a Car.
        """
        self.doors = [Goat()] * ndoors
        self.doors[randint(0, ndoors - 1)] = Car()

    def show_goat(self, choice):
        """Show a Goat that's not indexed at ``choice``."""
        index = self.doors.index(Goat())
        if index == choice:
            index = self.doors.index(Goat(), choice + 1)
        return index

if __name__ == "__main__":
    g = Game()
    print(g.doors)
