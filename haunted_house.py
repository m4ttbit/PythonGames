import time
import options
import front_room

#welcome intro to start the game
def welcome():
    print()
    print('"Ha! Ha! Ha! Thank you for coming to my haunted house.')
    print("I've been expecting you, {!s}.".format(name))
    print('Go ahead.\nOpen the front door to start looking for the treasure."')
    print()
    ent = input("PRESS ENTER TO GO INSIDE THE HAUNTED HOUSE\n>")
    ent = ent.upper()
    if ent == "Q":
        options.game_over()
    elif ent == "H":
        options.aid()
        aid = input("PRESS ENTER TO RESUME THE GAME\n>")
        aid = aid.upper()
        if aid == "Q":
            options.game_over()
        else:
            enter()
    else:
        enter()

#entering the house and front room
def enter():
    print("\n" * 100)
    print("Creeeeeeaaaaak...")
    print("You walk inside the spooky house. Cobwebs are everywhere!\nIt's so dark inside. There's a storm outside and sometimes you can see\nlightning through the curtains over the windows.")
    lights()

#turning the lights on in the front room
def lights():
    print()
    print("How are you going to search for a hidden treasure in this dark house?")
    print()
    print("A: Try the light switch.")
    print("B: Turn on your flashlight.")
    print("C: Light a match.")
    print()
    light = str(input("Which letter?\n>"))
    light = light.upper()
    if light == "A":
        print("\n" * 100)
        print("Click. Click. Oh no! Click. Click. You flick the light\nswitch up and down, but nothing happens! It looks like\nthe light switches don't work. Try another item.")
        print("\n" * 2)
        lights()
    elif light == "B":
        print("\n" * 100)
        print('Click! Your flashlight turns on and shines a bright beam\nacross the dark room. You see a shadow on the wall! You\nshout, "Hey! Stop right there!" But the shadow turns and\ndisappears. You shine your flashlight all around the room,')
        print("but there's no sign of the strange shadow.")
        find_key()
    elif light == "C":
        print("\n" * 100)
        print("Uh-oh. Your pockets are empty. You didn't bring any matches.\nYou know matches aren't safe for kids to use.\nTry another item from the list.")
        print("\n" * 2)
        lights()
    elif light == "Q":
        options.game_over()
    elif light == "H":
        options.aid()
        lights()
    else:
        print("\n" * 100)
        print("You didn't choose a letter between A and C. Try again.")
        print("\n" * 2)
        lights()

#find key for the first time in front room
def find_key():
    print()
    print("Wow! The room is filled with old and dusty furniture. You can hear\nrain beating down on the house's wooden shingles.\nEvery now and then, you see lightning flash across the walls of the room.")
    print()
    print("You shine your flashlight around the dark room and find something\nshiny on the floor in front of a large, dusty couch.\nYou walk over the shiny object to get a closer look. It's a key!")
    print()
    print("But a key for what?")
    print()
    print("Just as you pick up the key and put it in your pocket...")
    print()
    cont = input("PRESS ENTER TO CONTINUE\n>")
    cont = cont.upper()
    if cont == "Q":
        options.game_over()
    elif cont == "H":
        options.aid()
        find_key()
    else:
        print("\n" * 2)
        print("...you hear a loud laugh!")
        print()
        print("\"Ah! Ha! Ha! Ha! You'll never find the treasure, {!s}! Ha! Ha! Ha!\"".format(name))
        print()
        print("You quickly drop the key in your pocket and turn around with your flashlight,\nbut there's on one there.")
        print()
        fro = input("PRESS ENTER TO CONTINUE\n>")
        fro = fro.upper()
        if fro =="Q":
            game_over()
        elif fro == "H":
            options.aid()
            print("Now you look around the front room some more.")
            front_room.doors()
        else:
            front_room.doors()

#title and name input
print("\n" * 100)
print(" _____  _")
print("|_   _|| |")
print("  | |  | |__    ___")
print("  | |  | '_ \  / _ \ ")
print("  | |  | | | ||  __/")
print("  \_/  |_| |_| \___|")
print()
print(" _   _                       _              _")
print("| | | |                     | |            | |")
print("| |_| |  __ _  _   _  _ __  | |_   ___   __| |")
print("|  _  | / _` || | | || '_ \ | __| / _ \ / _` |")
print("| | | || (_| || |_| || | | || |_ |  __/| (_| |")
print("\_| |_/ \__,_| \__,_||_| |_| \__| \___| \__,_|")
print()
print(" _   _")
print("| | | |")
print("| |_| |  ___   _   _  ___   ___")
print("|  _  | / _ \ | | | |/ __| / _ \ ")
print("| | | || (_) || |_| |\__ \|  __/")
print("\_| |_/ \___/  \__,_||___/ \___|")
print('\n' * 2)
time.sleep(.5)
print("by Matt Arnold")
print("\n" * 2)
time.sleep(.5)
name = input('"Who are you?"\n>')
if name == "Q" or name == "q":
    options.game_over()
elif name == "H" or name =="h":
    options.aid()
    name = input('"Who are you?"\n>')
    welcome()
else:
    welcome()
