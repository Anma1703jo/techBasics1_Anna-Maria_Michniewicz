#Hi, sorry I was kinda lazy and didn't want to rearrange my code / break it with this extra task
#so i just took the enter user_name thing and made a function out of it
#the idea is, that the player is only allowed to enter letters (no special chars or digits)
#so I looked up the .isalpha() method to make it easier
#Yeah, I hope that's fine. Sorry I made an extra file for this

player = {
    "name": "",
    "errors": 0,
    "time": 0
}

def user_name():
    name = input("What is your name?\n" + ">")

    try:

        if not name.isalpha():
            raise TypeError("Only letters are allowed")

        player["name"] = name
        print("Success! What a beautiful name.")

    except TypeError as error:
        print("Please enter your real name. Only letters are allowed")
        return user_name()


user_name()
print()
print(player) #check if the proper name is added to the dic


