#!/usr/bin/env python

import os
import actions
import functions

SAVE_FILE = "game-save.save"


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def exit():
    if input("Are you sure you want to quit? (y/n): ") in ("y", "Y"):
        if input("Save the game? (y/n): ") in ("y", "Y"):
            save()
        clear()
        print("Goodbye\n")
        return True

def save():
    dumpcmd = "mysqldump -u " + DB_USER + " -h" + DB_HOST + " -p" + DB_PASSWORD + " " + DB_NAME + " > " + SAVE_FILE
    os.system(dumpcmd)

def load():
    loadcmd = "mysql -u " + DB_USER + " -h" + DB_HOST + " -p" + DB_PASSWORD + " " + DB_NAME + " < " + SAVE_FILE
    os.system(loadcmd)

def help():
    print("GAME HELP\n" +
          "\n" +
          "Movement:\n" +
          "Move around to any cardinal or intermediate directions, by entering\n" +
          "the direction or it's abbrevation, e.g. \"northeast\" or \"ne\".\n" +
          "\n" +
          "Gameplay commands:\n" +
          "look, l ............. Look around\n" +
          "hide, h ............. Hide yourself\n" +
          "take, t <item> ...... Take item\n" +
          "use, u <item> ....... Use item\n" +
          "examine, x <item> ... Examine item\n" +
          "items, i ............ List items\n" +
          "\n" +
          "Other commands:\n" +
          "help, ? ............. Print this help\n" +
          "exit, quit, q ....... Exit the game\n\n")
          
# first clear the screen
clear()

#TODO create initial game database with sql script????s

# load saved game if exists,
if os.path.isfile(SAVE_FILE):
    if input("Load saved game state? (y/n): ") in ("y", "Y"):
        load()

# start the game
print("You find yourself in a room tjsp alotustekstii?\n")

# main game loop
while True:
    functions.get_room_desc()

    cmd = input("Command: ").split()

    clear()

    try:
        if cmd[0] in ("north", "n", "N"):
            actions.move("N")
        elif cmd[0] in ("northeast", "ne", "NE"):
            actions.move("NE")
        elif cmd[0] in ("east", "e", "E"):
            actions.move("E")
        elif cmd[0] in ("southeast", "se", "SE"):
            actions.move("SE")
        elif cmd[0] in ("south", "s", "S"):
            actions.move("S")
        elif cmd[0] in ("southwest", "sw", "SW"):
            actions.move("SW")
        elif cmd[0] in ("west", "w", "W"):
            actions.move("W")
        elif cmd[0] in ("northwest", "nw", "NW"):
            actions.move("NW")

        elif cmd[0] in ("use", "u"):
            try:
                item = cmd[1]
            except IndexError:
                print("You must define the item you wish to use.")
                continue

            try:
                if cmd[2] in ("on", "with"):
                    try:
                        item2 = cmd[3]
                    except IndexError:
                        print("You must define the item you wish to use with "+item+".")
                        continue
                else:
                    item2 = cmd[2]
            except IndexError:
                #item2 = None
                item2 = ''

            actions.use(item, item2)

        elif cmd[0] in ("take", "t"):
            try:
                actions.take(cmd[1])
            except IndexError:
                print("You must define the item you wish to take.")
        elif cmd[0] in ("examine", "x"):
            try:
                actions.examine(cmd[1])
            except IndexError:
                print("You must define the item you wish to examine.")

        elif cmd[0] in ("hide", "h"):
            actions.hide()
        elif cmd[0] in ("look", "l"):
            actions.look()
        elif cmd[0] in ("items", "i"):
            actions.items()

        elif cmd[0] in ("help", "?"):
            help()
        elif cmd[0] in ("exit", "quit", "q"):
            if exit():
                break

        else:
            print("Invalid command.")
            continue

    except IndexError:
        print("Enter command you dummy.")


