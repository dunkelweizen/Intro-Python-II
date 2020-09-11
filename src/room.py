# Implement a class to hold room information. This should have name and
# description attributes.
import sys


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items_in_room = []

    def __str__(self):
        return f"You are at {self.name}, {self.description}"

    def make_move(self, move):
        if move.lower() == "n":
            next_move = self.n_to
        elif move.lower() == "s":
            next_move = self.s_to
        elif move.lower() == "e":
            next_move = self.e_to
        elif move.lower() == "w":
            next_move = self.w_to
        elif move.lower() == "q":
            sys.exit()
        else:
            next_move = False
        return next_move

    def take_item(self, item):
        self.items_in_room.pop(self.items_in_room.index(item))
