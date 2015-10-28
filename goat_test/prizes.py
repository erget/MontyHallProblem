#!/usr/local/bin/python3
# encoding: utf-8

"""Fabulous prizes to be had!"""


class Prize(object):

    """A prize you can win."""

    def __eq__(self, other):
        """One Prize with the same child class is the same as another."""
        return isinstance(other, self.__class__)


class Goat(Prize):

    """Probably not what you wanted."""

    def __repr__(self):
        return "Goat()"


class Car(Prize):

    """Any color you want... As long as it's black."""

    def __repr__(self):
        return "Car()"
