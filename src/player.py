# Write a class to hold player information, e.g. what room they are in
# currently.
from items import Chest


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = "outside"
        self.inventory = []

    def __str__(self):
        s = f"Player {self.name} is in {self.current_room}"
        if len(self.inventory) > 0:
            inv = 'You are currently holding: '
            for item in self.inventory:
                inv += item.name + ", "
            inv = inv.rstrip(", ")
            inv += "."
            s += "\n" + inv
        return s

    def get_item(self, item):
        current_inventory = self.inventory
        current_inventory.append(item)
        self.inventory = current_inventory
        print(f"You have added {item} to your inventory.")
        if type(item) == Chest:
            if "a key" not in [x.name for x in self.inventory]:
                print(self.inventory)
                print("It's locked.")
            else:
                item.open()
                self.inventory.get_item("coins")


    def drop_item(self, item):
        current_inventory = self.inventory
        current_inventory.pop(current_inventory.index(item))
        self.inventory = current_inventory
        print(f"You have dropped {item} from your inventory.")