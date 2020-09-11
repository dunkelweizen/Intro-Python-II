class Item:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __str__(self):
        return self.name

class Treasure(Item):
    def __init__(self, name, attributes):
        super().__init__(name, attributes)

    def __self__
class Chest(Item):
    def __init__(self, name, attributes, locked=True):
        super().__init__(name, attributes)
        self.locked = locked

    def open(self, has_key):
        if has_key == False:
            result = "It's locked."
            get_coins = False
        else:
            result = "You open the chest to find a big pile of gold coins inside."
            get_coins = True
        return result, get_coins