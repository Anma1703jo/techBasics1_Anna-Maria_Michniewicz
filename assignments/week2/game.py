#space_game.py

import time

current_situation = "start"


def abc_text(output_string):
    print(f"\033[93m{output_string}\033[0m", end="")
    time.sleep(0.5)
    print()

def user_text(output_string):
    print(f"\033[92m{output_string}\033[0m")
    time.sleep(1)
    print()

def robo_john_text(output_string):
    for x in output_string:
        print(f"\033[96m{x}\033[0m", end="")
        time.sleep(0.01)
    print()

def robotina_text(output_string):
    for x in output_string:
        print(f"\033[95m{x}\033[0m", end="")
        time.sleep(0.01)
    print()



def room_start():
    print("You slowly open your eyes.")
    time.sleep(2)
    print()
    print("Your head kind of hurts and a slight nausea sits in your stomach ")
    time.sleep(2)
    print()
    print("""Your look around. 
    You're sitting in some kind of control console.""")
    time.sleep(2)
    print()
    print("""A big window is in front of you.
    But it is all black.""")
    time.sleep(2)
    print()
    print("""You look further, and notice a monitor underneath.
    A touchpad, a joystick and many, many buttons. They blink and flash nicely.""")
    print()
    user_text("Is this some kind of game?")
    time.sleep(3)


def finale():
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("That female robotic voice again")
    time.sleep(1)
    robotina_text("""
        Calibrating sensors complete""")
    print()
    time.sleep(1)
    print("Robo-John chimes in:")
    time.sleep(1)
    robo_john_text("""
        We did it!
        Oh Robotilda, how much I'd love to caress you...
        Well, okay. No we can try to contact earth.
        Dial in the number 42 on the touch pad and let's
        see if you little ET can phone home.""")
    print()
    time.sleep(1)
    print("""You type in the number and a dialing sound appears.
    Just like on the old telephone of your grandmother...
    """)
    time.sleep(1)
    robo_john_text("""
        Congratulations. You finished the game.""")
    print()
    return "end"

#current_situation = finale()


def choice_5b():
    angle = int(input("> "))

    if angle >= 135 and angle <= 155:
        print("A female robotic voice speaks:")
        time.sleep(1)
        robotina_text("""
        Calibrating sensors. 
        Please Wait.""")
        print()
        time.sleep(1)
        robo_john_text("""
        Oh, my dear Robotilda. I missed your charming voice.""")
        print()
        time.sleep(1)
        robotina_text("""
        Calibrating sensors.
        Please Wait.
        John, please focus.""")
        print()
        return "finale"
    elif angle > 0 and angle < 135:
        print("""The ship shakes in a weird manner.
        A female robotic voice speaks:""")
        time.sleep(1)
        robotina_text("""
        Angle of the ship incorrect.
        Please try again.""")
        return "choice_5b"
    elif angle > 155 and angle < 360:
        print("""The ship shakes in a weird manner.
        A female robotic voice speaks:""")
        time.sleep(1)
        robotina_text("""
        Angle of the ship incorrect.
        Please try again.""")
        return "choice_5b"
    else:
        print("A female robotic voice speaks:")
        time.sleep(1)
        robotina_text("""
        You've studied physics. 
        You know how angles work, right?""")
        print()
        time.sleep(1)
        print("Robo-John sighs:")
        time.sleep(1)
        robo_john_text("""
        Oh, the sassy tone. 
        Dear Robotilda, I love it 
        when you talk like that.""")
        print()
        time.sleep(1)
        print("Please try again.")
        return "choice_5b"

#current_situation = choice_5b()


def choice_5():
    robo_john_text("""
        Perfect, that starts the operation.
        Now we need to be precise.
        You need to turn the ship to the right angle 
        in order for the sensors to be able to generate
        proper coordinates. Look at the touchpad.
        You need to type the right number, although you
        have a leeway of 10-20 degrees.""")
    print()
    print("Type in the angle to calibrate the ship.")
    time.sleep(1)

    return "choice_5b"

#current_situation = choice_5()


def choice_4b():
    print("Type 'Press' to continue.")

    writing = input("> ").lower()

    if writing == "press":
        return "choice_5"
    else:
        print("Please write 'Press' to continue.")
        writing = input("> ").lower()
        return "choice_4b"

def choice_4():
    user_text("""Wojciech... Nowak..? Yeah, I remember.  
    I studied in Warsaw.. I have a wife. And a dog?""")
    time.sleep(1)
    robo_john_text("""
        That's right. You left earth 6 years ago.
        If you get the ship's sensors running again,
        we could try and contact earth.
        Maybe you could even talk with your wife.
        They must be worried. No contact and no data for
        a couple of days. That is not typical for us.""")
    time.sleep(2)
    print()
    user_text("How do I do that?")
    time.sleep(1)
    robo_john_text("""
        You need to recalibrate the sensors.
        In order to do so, press the blue button.""")
    print()
    time.sleep(1)
    print("Type 'Press' to continue.")

    writing = input("> ").lower()

    if writing == "press":
        return "choice_5"
    else:
        print("Please write 'Press' to continue.")
        writing = input("> ").lower()
        return "choice_4b"

#current_situation = choice_4()


def choice_3():
    abc_text("   a. Wormhole? Milky Way? Why am I in space?!")
    abc_text("   b. How long was I out?")
    abc_text("   c. Who are you?")

    first_input = True
    selection = ""
    no_valid_selection = True
    while no_valid_selection:
        if not first_input:
            print("Please choose a, b or c.")
        else:
            first_input = False
        selection = input("> ").lower()
        if selection in ["a", "b", "c"]:
            no_valid_selection = False

    if selection == "a":
        robo_john_text("""
        Damn, quite a chunk of your memory is missing!
        I'm always at awe how delicate you humans can be.
        You are Wojciech Nowak. The first man to conquer space outside of the Milky Way.
        Our mission is to explore what we can.""")
        print()
        return "choice_4"
    elif selection == "b":
        robo_john_text("""
        It's hard to say. My sensors were down for some time.
        But I'd guess 3 to 4ish days?""")
        print()
        return "choice_3"
    elif selection == "c":
        robo_john_text("""
        I am Robo-John! Your companion. Turns out, leave humans
        alone for too long and they'll lose their minds...
        and then their lives.
        So I'm here to keep you sane, buddy! Haha.
        Fragile little things, you humans.""")
        print()
        return "choice_3"

#current_situation = choice_3()


def choice_2():
    abc_text("   a. What happened?")
    abc_text("   b. Who are you?")

    first_input = True
    selection = ""
    no_valid_selection = True
    while no_valid_selection:
        if not first_input:
            print("Please choose a or b.")
        else:
            first_input = False
        selection = input("> ").lower()
        if selection in ["a", "b"]:
            no_valid_selection = False

    if selection == "a":
        robo_john_text("""
        We hit a wormhole. It was hidden in the nebula, we tried to explore.
        It beamed us to the other side of the Milky Way, I think.
        The travel was rather turbulent and we took quite some damage.
        What a Voyager moment, right? 
        Anyway, the gravity feature was down and you hit your head pretty hard.""")
        print()
        return "choice_3"

    elif selection == "b":
        robo_john_text("""
        I am Robo-John! Your companion. Turns out, leave humans
        alone for too long and they'll lose their minds...
        and then their lives.
        So I'm here to keep you sane, buddy! Haha.
        Fragile little things, you humans.""")
        print()
        return "choice_2"

#current_situation = choice_2()


def choice_1():
    print("What do you want to do?")
    time.sleep(1)
    abc_text("   a. Try the joystick")
    abc_text("   b. Press the red blinking button")
    abc_text("   c. Try the touchpad")

    first_input = True
    selection = ""
    no_valid_selection = True
    while no_valid_selection:
        if not first_input:
            print("Please choose a, b or c.")
        else:
            first_input = False
        selection = input("> ").lower()
        if selection in ["a", "b", "c"]:
            no_valid_selection = False

    if selection == "a":
        print("""
        You move the joystick around. It seems to turn the whole thing you are sitting in.
        Suddenly you notice white little dots out the window.
        You turn even further and see a huge swirl of light.""")
        time.sleep(3)
        print()
        user_text("Wait.. Is that... the milky way?!")
        return "choice_1"

    elif selection == "b":
        print("""
        Red lights and an alarm tone appear.""")
        time.sleep(1)
        print("""
        Suddenly some kind of trap door opens above you and you get ejected into... space?""")
        time.sleep(1)
        print("""
        The vacuum hits you immediately. You feel your lungs deflating.""")
        time.sleep(1)
        robo_john_text("""
        This is the end of your adventure, my friend. Farewell.""")
        time.sleep(3)
        print()
        print("Do you want to start over?")
        selection = input("> ").lower()
        if selection == "yes":
            print("\n" * 50)
            return "start"
        else:
            print("It has been short, but enjoyable.")
            return "end"

    elif selection == "c":
        print("You press the touchpad. A melodic robot voice starts taking:")
        time.sleep(1)
        print()
        robo_john_text("""
        Woah dude! I thought you were dead! Are you alright?""")
        time.sleep(1)
        print()
        return "choice_2"

#current_situation = choice_1()


while current_situation != "end":
    if current_situation == "start":
        room_start()
        current_situation = choice_1()
    elif current_situation == "choice_1":
        current_situation = choice_1()
    elif current_situation == "choice_2":
        current_situation = choice_2()
    elif current_situation == "choice_3":
        current_situation = choice_3()
    elif current_situation == "choice_4":
        current_situation = choice_4()
    elif current_situation == "choice_4b":
        current_situation = choice_4b()
    elif current_situation == "choice_5":
        current_situation = choice_5()
    elif current_situation == "choice_5b":
        current_situation = choice_5b()
    elif current_situation == "finale":
        current_situation = finale()

print("Thanks for playing.")





