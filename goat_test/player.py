#!/usr/local/bin/python3
# encoding: utf-8

"""This here's a player's game."""


from argparse import ArgumentParser
from random import randint

from game import Game
from prizes import Goat, Car


class PlayerStrategy(object):

    """The Player's strategy."""

    def play(self, game, choice):
        """Play the game."""


class Confidence(PlayerStrategy):

    """You draw the line in the sand and stick to it."""

    def play(self, game, choice):
        """Don't let the announcer get into your head."""
        return game.doors[choice]
    

class Switcheroo(PlayerStrategy):
    
    """Snatch the pebble from my hand, grasshopper."""
    
    def play(self, game, choice):
        """Knowledge is my sword, honed by statistics."""
        goat = game.show_goat(choice)
        final_choice = [x for x in range(len(game.doors))
                        if x != choice and x != goat][0]
        return game.doors[final_choice]
    

class Renegade(PlayerStrategy):
    
    """Play it by hand."""
    
    def play(self, game, choice=False):
        """Use the Force, Luke."""
        if not type(choice) == int:
            choice = int(input("Pick a door number between 0 and {}."
                               "\n".format(len(game.doors - 1))))
        print("You chose {}.".format(choice))
        goat = game.show_goat(choice)
        print("There's a goat behind door {}.".format(goat))
        switch = not bool(raw_input("Would you like to switch doors? " +
                                    "Enter for yes, n for no.\n"))
        if switch:
            prize = Switcheroo().play(game, choice)
        else:
            prize = Confidence().play(game, choice)
        return prize


class Player(object):

    """You. Or a model of you."""

    def __init__(self, strategy=Renegade()):
        """Hustle round, it's time to get warmed up."""
        self.choice = 0
        self.strategy = strategy



if __name__ == "__main__":
    """Player's gonna play."""
    description = ("A fabulous quiz game! \n\n"
                   "You see before you 3 doors. Behind 1 is a car. "
                   "Behind the others are goats. \n"
                   "Play manually or automate the program for extremely "
                   "efficient goat-choosing!")
    parser = ArgumentParser(description=description)
    parser.add_argument("-i", action="store_true",
                        help="Choose your goat interactively. "
                        "Overrides automatic modes.")
    parser.add_argument("tries", default=50, type=int,
                        help="How many times should your automatic goat "
                        "chooser try its luck? Default: 50")
    parser.add_argument("-c", action="store_true",
                        help="Confident mode. Your automatic goat chooser "
                        "sticks to its first choice. This is the default mode.")
    parser.add_argument("-d", action="store_true",
                        help="Doubting mode. Your automatic goat chooser "
                        "switches its first choice.")
    args = parser.parse_args()
    strategy = None
    need_random = True
    if args.i:
        strategy = Renegade()
        need_random = False
    elif args.d:
        strategy = Switcheroo()
    else:
        strategy = Confidence()
    g = Game()
    p = Player(strategy)
    prizes = []
    for i in range(args.tries):
        if need_random:
            choice = randint(0, len(g.doors) - 1)
        else:
            choice = False
        prize = p.strategy.play(g, choice)
        if args.i:
            if prize == Car():
                print("Congrats, you got a car.")
            else:
                print("Shucks, a goat.")
        prizes.append(prize)
    ngoats = len([x for x in prizes if x == Goat()])
    ncars = len(prizes) - ngoats
    print("You got {} goats and {} cars.".format(ngoats, ncars))
    try:
        ratio = ngoats / float(ncars)
    except ZeroDivisionError:
        ratio = "infinite"
    print("Your goat to car ratio was {}".format(ratio))
