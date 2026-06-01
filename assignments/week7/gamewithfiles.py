import time

#hello there, just copy-pasted the game here

#variables
current_situation = "start"
DEBUG = True

#addition
print("Welcome to the game!")

#watched a youtube video and looked up a bit on geeksforgeeks
#we imported time already but let's set the start time

start_time = time.time()

#let's get the name of the player to use it later on

user_name = input("What is your name?\n" + ">")
print(f"An intergalactic adventure awaits you... Your time starts now, {user_name}!" + " \n" * 3)

#player info dic
player = {
    "name": user_name,
    "calibration errors": 0,
    "time": 0
}

#dialogues/text
start_text = ["You slowly open your eyes.", "Your head kind of hurts and a slight nausea sits in your stomach.",
                 "Your look around. You're sitting in some kind of control console.",
                 "A big window is in front of you. But it is all black.",
                 "You look further, and notice a monitor underneath. "
                 "A touchpad, a joystick and many, many buttons.", "They blink and flash nicely."]

player_text = "Is this some kind of game?"

finale_text = ["Calibrating sensors complete", "We did it!", "Oh Robotilda, how much I'd love to caress you...",
               "Well, okay. No we can try to contact earth.", "Dial in the number 42 on the touch pad and let's",
               "see if you little ET can phone home.", "You type in the number and a dialing sound appears.",
               "Just like on the old telephone of your grandmother..",
               "Congratulations. You finished the game"]


#selection text
try_console_text = ["What do you want to do?",
                    "a. Try the joystick",
                    "b. Press the red blinking button",
                    "c. Try the touchpad"]

robo_talk_text = ["a. What happened?",
                  "b. Who are you?"]

info_talk_text = ["a. Wormhole? Milky Way? Why am I in space?",
                  "b. How long was I out?"]


#selection answer text
try_console_a = ["You move the joystick around. It seems to turn the whole thing you are sitting in.",
                 "Suddenly you notice white little dots out the window.",
                 "You turn even further and see a huge swirl of light.",
                 "Wait... Is that... the milky way?!"]

try_console_b = ["Red lights and an alarm tone appear.",
                 "Suddenly some kind of trap door opens above you and you get ejected into... space?",
                 "The vacuum hits you immediately. You feel your lungs deflating.",
                 "This is the end of your adventure, my friend. Farewell."]

try_console_c = ["You press the touchpad. A melodic robot voice starts taking:",
                 "Woah dude! I thought you were dead! Are you alright?"]


robo_talk_a = ["We hit a wormhole. It was hidden in the nebula, we tried to explore.",
               "It beamed us to the other side of the Milky Way, I think.",
               "The travel was rather turbulent and we took quite some damage. What a Voyager moment, right?",
               "Anyway, the gravity feature was down and you hit your head pretty hard."]

robo_talk_b = ["I am Robo-John! Your companion.",
               "Turns out, leave humans alone for too long and they'll lose their minds... ",
               "and then their lives.",
               "So I'm here to keep you sane, buddy! Haha. Fragile little things, you humans."]


info_talk_a = ["Damn, quite a chunk of your memory is missing!",
               "I'm always at awe how delicate you humans can be.",
               f"You are {user_name}. The first human to conquer space outside of the Milky Way.",
               "Our mission is to explore what we can."]
info_talk_b = ["It's hard to say.",
               "My sensors were down for some time.",
               "But I'd guess 3 to 4ish days?"]


who_am_i = [f"{user_name}...? Yeah, I remember.",
            "I studied in Warsaw.. I have a wife. And a dog?"]

who_am_i_robo = ["That's right. You left earth 6 years ago.",
                 "If you get the ship's sensors running again,",
                 "we could try and contact earth.",
                 "Maybe you could even talk with your wife.",
                 "They must be worried. No contact and no data for",
                 "a couple of days. That is not typical for us.",
                 "You need to recalibrate the sensors.",
                 "In order to do so, press the blue button"]


robo_john_text = ["Perfect, that starts the operation.",
                  "Now we need to be precise.",
                   "You need to turn the ship to the right angle",
                  "in order for the sensors to be able to generate",
                  "proper coordinates. Look at the touchpad.",
                  "You need to type the right number, although you",
                  "have a leeway of 10-20 degrees."]


angle_right = ["A female robotic voice speaks:",
               "Calibrating sensors. Please wait.",
               "Oh, my dear Robotilda. I missed your charming voice.",
               "Calibrating sensors. Please wait.",
               "John, please. Focus."]

angle_wrong = ["The ship shakes in a weird manner.",
               "A female robotic voice speaks:",
               "Angle of ship incorrect. Please try again"]

angle_way_off = ["A female robotic voice speaks:",
                 "You've studied physics. You know how angles work, right?",
                 "Robo-John sighs:",
                 "Oh, the sassy tone.",
                 "Dear Robotilda, I love it when you speak like this"]


#functions now
def gen_text(text, color=None):
    colors = {
        "green": "\033[92m",
        "yellow": "\033[93m",
    }
    color_code = colors.get(color, "")
    reset_code = "\033[0m"

    if isinstance(text, str): #yeah, he started to print letter by letter every line, so for the case I have only 1 string
        text = [text]

    for line in text:
        print(f"{color_code}{line}{reset_code}")
        time.sleep(1)
    print()

#function for the print char after char "robo-like"
def robo_speak(text, color):
    colors = {
        "cyan": "\033[96m",
        "pink": "\033[95m"
    }

    color_code = colors.get(color, "")
    reset_code = "\033[0m"

    if isinstance(text, str):
        text = [text]

    for line in text:
        print(" " * 15, end="") #wanted to add indent to the robo dialogue

        for char in line:
            print(f"{color_code}{char}{reset_code}", end="")
            time.sleep(0.01)

        time.sleep(0.05)
        print()

    print()

#function for input
def selection(valid_choices):
    first_input = True

    while True:
        if not first_input:
            print(f"Please choose: {', '.join(valid_choices)}")
        else:
            first_input = False
        user_input = input("> ").lower()

        if user_input in valid_choices:
            return user_input

#function for the one case where you die
def death():
    print("Do you want to start over?")
    selection = input("> ").lower()
    if selection == "yes":
        print("\n" * 50)
        return "start"
    else:
        print("It has been short, but enjoyable.")
        return "end"


#nice, we have the functions down to avoid repetitions
#let's do the rooms next
def start():
    gen_text(start_text)
    gen_text(player_text, "green")
    return "try_console"

def try_console():
    gen_text(try_console_text, "yellow")

    selection_choice = selection(["a", "b", "c"])

    if selection_choice == "a":
        gen_text(try_console_a[0:3])
        gen_text(try_console_a[-1], "green")
        return "try_console"

    elif selection_choice == "b":
        gen_text(try_console_b[0:3])
        robo_speak(try_console_b[-1], "cyan")
        return death()

    elif selection_choice == "c":
        gen_text(try_console_c[0])
        robo_speak(try_console_c[1], "cyan")
        return "robo_talk"

def robo_talk():
    gen_text(robo_talk_text, "yellow")

    selection_choice = selection(["a", "b"])

    if selection_choice == "a":
        robo_speak(robo_talk_a, "cyan")
        return "info_talk"

    elif selection_choice == "b":
        robo_speak(robo_talk_b, "cyan")
        return "robo_talk"

def info_talk():
    gen_text(info_talk_text, "yellow")

    selection_choice = selection(["a", "b"])

    if selection_choice == "a":
        robo_speak(info_talk_a, "cyan")
        return "wojtek"

    elif selection_choice == "b":
        robo_speak(info_talk_b, "cyan")
        return "info_talk"

def wojtek():
    gen_text(who_am_i, "green")
    robo_speak(who_am_i_robo, "cyan")
    return "press_button"

def press_button():
    print("Type 'Press' to continue.")

    writing = input("> ").lower()

    if writing == "press":
        return "calibrate"

    else:
        print("Please write 'Press' to continue.")
        writing = input("> ").lower()
        return "press_button"

def calibrate():
    robo_speak(robo_john_text, "cyan")
    gen_text("Type in the angle to calibrate the sensors.")
    return "feingefuehl"


def feingefuehl():
    angle = int(input("> "))

    if angle >= 135 and angle <= 155:
        gen_text(angle_right[0])
        robo_speak(angle_right[1], "pink")
        robo_speak(angle_right[2], "cyan")
        robo_speak(angle_right[3:5], "pink")
        return "finale"

    elif angle > 0 and angle < 135:
        gen_text(angle_wrong[0:2])
        robo_speak(angle_wrong[2], "pink")
        player["calibration errors"] += 1
        return "feingefuehl"

    elif angle > 155 and angle < 360:
        gen_text(angle_wrong[0:2])
        robo_speak(angle_wrong[2], "pink")
        player["calibration errors"] += 1
        return "feingefuehl"

    else:
        gen_text(angle_way_off[0])
        robo_speak(angle_way_off[1], "pink")
        robo_speak(angle_way_off[2:5], "cyan")
        gen_text("Please try again.")
        player["calibration errors"] += 1
        return "feingefuehl"

def finale():
    robo_speak(finale_text[0], "pink")
    robo_speak(finale_text[1:6], "cyan")
    gen_text(finale_text[6:8],)
    robo_speak(finale_text[-1], "cyan")
    return "end"


#and now the whole while loop to control all this code
while current_situation != "end":

    if current_situation == "start":
        current_situation = start()

    elif current_situation == "try_console":
        current_situation = try_console()

    elif current_situation == "robo_talk":
        current_situation = robo_talk()

    elif current_situation == "info_talk":
        current_situation = info_talk()

    elif current_situation == "wojtek":
        current_situation = wojtek()

    elif current_situation == "press_button":
        current_situation = press_button()

    elif current_situation == "calibrate":
        current_situation = calibrate()

    elif current_situation == "feingefuehl":
        current_situation = feingefuehl()

    elif current_situation == "finale":
        current_situation = finale()


print("Thanks for playing!")

#let's continue with the time, we do the end time first
end_time = time.time()

#little substraction to get the time passed while playing
elapsed_time = end_time - start_time

#since the format is kinda freaky I make an int out of it
print(f"Good job, {user_name}! You took {int(elapsed_time)} seconds.")
print("I hope we meet again one day.." + "\n" * 2)

#add the elapsed time to player dic
player["time"] = int(elapsed_time)

#just little print of player dic
for key in player:
    print(f"{key}: {player[key]}")

#now let's add this to a file to store data
with open("user_data.txt", "a") as file:
    for key in player:
        file.write(f"{key}: {player[key]}\n")
    file.write("\n")

print(" \n" * 10 + "Score history: ")

with open("user_data.txt") as file:
   print(file.read())