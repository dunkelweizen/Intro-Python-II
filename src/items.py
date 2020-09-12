
class Item:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def __str__(self):
        return self.name

class Treasure(Item):
    def __init__(self, name, attributes):
        super().__init__(name, attributes)


class Chest(Item):
    def __init__(self, name, attributes):
        super().__init__(name, attributes)

    def open(self):
        print("You open the chest to find a big pile of gold coins inside.")

