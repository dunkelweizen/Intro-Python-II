# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = "outside"
        self.inventory = []

    def __str__(self):
        s = f"Player {self.name} is in room {self.current_room}"
        if len(self.inventory) > 0:
            s += f"\nYou are currently holding {self.inventory}"
        return s

    def get_item(self, item):
        current_inventory = self.inventory
        current_inventory.append(item)
        self.inventory = current_inventory
        print(f"You have added {item} to your inventory.")
