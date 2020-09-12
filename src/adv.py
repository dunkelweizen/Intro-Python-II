from room import Room
from player import Player
from items import Item, Treasure, Chest
import sys

rocks = Item("a pile of rocks", "It's just a pile of rocks.")
bones = Item("some dusty old bones", "You think they might be human bones. They've clearly been here a long time.")
key = Item("a key", "An old brass key. You wonder what it might be for.")
gems = Treasure("a pile of gems", "It's a big pile of shiny precious gemstones. Probably quite valuable.")
goblet = Treasure("a golden goblet", "A large golden goblet with rubies inlaid around the rim.")
chest = Chest("a treasure chest", "A large wooden chest with brass bands. Full of something enticing.")
coins = Treasure("a pile of gold coins", "A big pile of gold coins. You could buy a lot with this.")

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", [rocks, bones]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [key]),

    'grand overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow passage': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber!""", [chest, gems, goblet])
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['grand overlook']
room['foyer'].e_to = room['narrow passage']
room['grand overlook'].s_to = room['foyer']
room['narrow passage'].w_to = room['foyer']
room['narrow passage'].n_to = room['treasure chamber']
room['treasure chamber'].s_to = room['narrow passage']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def playgame():
    player_name = input("Enter your name:")
    player = Player(name=player_name)
    valid_moves = ["n", "s", "e", "w"]
    valid_inventory_choices = ["get", "drop"]
    room_describe_counter = 0
    while True:
        if room_describe_counter == 0:
            current_room = player.current_room
            print(room[current_room.lower()])
            room_describe_counter += 1
        current_input = input("What do you want to do now? To see your character's current status, type 'status'. "
                              "To look around, type 'look'.\n")
        if current_input == "q":
            sys.exit()
        elif current_input.split()[0] == "look":
            if len(current_input) == 1:
                print(room[current_room.lower()])
                continue
            else:
                for item in current_input.split():
                    for value in player.inventory:
                        if item in value.name:
                            print(value.attributes)
        elif current_input == "status":
            print(player)
            continue
        elif current_input in valid_moves:
            next_move = room[current_room.lower()].make_move(current_input)
            if next_move is None:
                print("There's nowhere to go in that direction. Try something else.")
                continue
            else:
                room_name = next_move.name
                player.current_room = room[room_name.lower()].name
                room_describe_counter = 0
                continue
        elif current_input.split()[0] in valid_inventory_choices:
            if current_input.split()[0] == "get":
                for item in room[current_room.lower()].items_in_room:
                    if current_input.split()[1] in item.name.split():
                        player.get_item(item)
                        room[current_room.lower()].remove_item(item)
                        continue
            elif current_input.split()[0] == "drop":
                for item in player.inventory:
                    if current_input.split()[1] in item.name.split():
                        player.drop_item(item)
                        room[current_room.lower()].add_item(item)
                        continue
        else:
            print("I don't understand what you want to do.")





if __name__ == "__main__":
    playgame()

