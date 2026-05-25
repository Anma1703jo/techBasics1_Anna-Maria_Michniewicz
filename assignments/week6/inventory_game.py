from unittest import case

# --- Game State ---

inventory = []

items = [
    {"name": "cereal", "type": "food", "description": "Pretty dry on its own. Get some milk."},
    {"name": "biscuits", "type": "food", "description": "The brits love it."},
    {"name": "tuna", "type": "food", "description": "A can of tuna"},
    {"name": "chocolate", "type": "food", "description": "The best thing the world came up with"},
    {"name": "chips", "type": "food", "description": "A salty and fatty guilty pleasure."},
    {"name": "baguette", "type": "food", "description": "Hon Hon, take ze baguette."},
    {"name": "sausage roll", "type": "food", "description": "Mystery filling, but a great snack non the less"},
    {"name": "croissant", "type": "food", "description": "Buttery and fluffy pastry."},
    {"name": "flash light", "type": "tool", "description": "May it light your way"},
    {"name": "keys", "type": "tool", "description": "Who the hell sells keys? What are they for?"},
    {"name": "postcard", "type": "souvenir", "description": "It shows a picture of some family. Underneath the text: You're not alone."},
    {"name": "window cleaner", "type": "tool", "description": "There is nothing worse than dirty windows while driving."},
    {"name": "alien plushie", "type": "souvenir", "description": """A cute plushie in the shape of an alien. It's kind of eerie. 
    You may have noticed a red blinking in the eyes, but the suspicion vanishes quickly. 
    You just know, you have to buy it."""},
    {"name": "coke light", "type": "beverage", "description": "Highly addictive, but man is it good."},
    {"name": "peach ice tea", "type": "beverage", "description": "The gamer drink of all times."},
    {"name": "water", "type": "beverage", "description": "Hydration, babyyyyyy"},
    {"name": "motor oil", "type": "tool", "description": "Who the hell puts motor oil in the fridge. It's solid now??"},
]

shelves = [
    {
        "shelf_name": "food shelf",
        "shelf_content": ["cereal", "biscuits", "tuna", "chocolate", "chips"] },
    {
        "shelf_name": "shelf with baked goods",
        "shelf_content": ["baguette", "sausage roll", "croissant"] },
    {
        "shelf_name": "tool and souvenir shelf",
        "shelf_content": ["flash light", "keys", "postcard", "window cleaner", "alien plushie"] },
    {
        "shelf_name": "fridge",
        "shelf_content": ["coke light", "peach ice tea", "water", "motor oil" ] },
]

room = ["food shelf", "shelf with baked goods", "tool and souvenir shelf", "fridge"]



# length shall be larger than max inventory size if there is only one room
MAX_INVENTORY_SIZE = 5

# --- Functions ---

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    if len(inventory) == 0:
        print("Your hands are empty")
    else:
        print("Items in your Inventory:")
        for item in inventory:
            print(item["name"])


def show_room_items():
    # list all items in current room
    #let's spice it up and list in categories, shelf by shelf
    print("You look around. You see many items on the shelves in this little weird gas station.")
    #call the shelf names
    for shelf_name in room:
        print(f"There is a {shelf_name}.")
        print("  " + "It is filled with...")
    #search for the objects
        for shelf in shelves:
            if shelf["shelf_name"] == shelf_name: #found it? show me the items it contains
                for item in shelf["shelf_content"]:
                    print(" " * 5 + item)


def pick_up(item_name):
    # pick up an item from the room if inventory limit is not met yet
    for item in items:
        if item["name"] == item_name: #search for the proper item in dic in list
            if len(inventory) < MAX_INVENTORY_SIZE:
                inventory.append(item) #add to inventory
                print("You've picked up: " + item_name)
                items.remove(item) #remove from items in room list
                return
            else:
                print("Your hands are full!")


def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    for item in inventory:
        if item["name"] == item_name:

            if item["name"] == "alien plushie":
                print("A strong feeling urges you to keep this.") #the player can't drop the alien plushie
                return

            inventory.remove(item) #remove from inventory
            items.append(item) #add again to item list
            print("You dropped " + item["name"])
            return


def use(item_name):
    # Ex: use the item differently depends on the type
    for item in items:
        if item["name"] == item_name:
            if item["type"] == "food" or item["type"] == "beverage":
                print("You try to open it.")
                print('The casher shouts at you: "HEY! You have to pay first!!" ')
            elif item["type"] == "tool":
                print("I have no use for this now")
            elif item["type"] == "souvenir":
                print("I never understood why people bought this stuff.")


def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    for item in items + inventory:
        if item["name"] == item_name:
            print("You look at the " + item["name"] + " closely." )
            print(item["description"])


# --- Game Loop ---

def game_loop():
    print("Hey there! Welcome to SpaceFuel! How can I help you today?")
    print("You look around. It's a small gas station, but something seems off")
    print("Before you can pin it down, a warm fog surrounds your brain.")
    print("It is a magical place.")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()

        # As an example, here I used the match/case syntax to replace long if/else statements
        # This feature is only supported from Python 3.10 and above

        match command.split():
            case ["help"]:
                print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
            case ["inventory"]:
                show_inventory()
            case ["look"]:
                show_room_items()
            case ["pickup", *item_parts]:
                item_name = " ".join(item_parts) #it didn't accept the command, because the string (item) consisted of 2 words with a space
                pick_up(item_name)
            case ["drop", *item_parts]:
                item_name = " ".join(item_parts)
                drop(item_name)
            case ["use", *item_parts]:
                item_name = " ".join(item_parts)
                use(item_name)
            case ["examine", *item_parts]:
                item_name = " ".join(item_parts)
                examine(item_name)
            case ["quit"]:
                print("""
                You wake up in your car. Your boss is calling you.
                You see that it is 8pm. How did you spent 4 hours at the gas station??
                The gas is full and next to you are your purchases.
                You don't remember anything from the visit.
                The alien plushie looks at you and you feel shivers down your spine.
                """)
                break
            case _: # else
                print("Unknown command. Type 'help' to see available commands.")



if __name__ == "__main__":
    game_loop()
