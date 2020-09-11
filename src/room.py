# Implement a class to hold room information. This should have name and
# description attributes.
import sys


class Room:
    def __init__(self, name, description, items_in_room=[]):
        self.name = name
        self.description = description
        self.items_in_room = items_in_room
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        s = f"You are at {self.name}, {self.description}"
        if len(self.items_in_room) == 1:
            s += f"\n There is {self.items_in_room[0]} here."
        elif len(self.items_in_room) > 1:
            ns = "\nThere are "
            for item in self.items_in_room:
                ns += item + " and "
            ns = ns.rstrip(" and ")
            s += ns + " here."
        return s

    def make_move(self, move):
        if move.lower() == "n":
            next_move = self.n_to
        elif move.lower() == "s":
            next_move = self.s_to
        elif move.lower() == "e":
            next_move = self.e_to
        elif move.lower() == "w":
            next_move = self.w_to
        return next_move

    def remove_item(self, item):
        self.items_in_room.pop(self.items_in_room.index(item))

    def add_item(self, item):
        self.items_in_room.append(item)