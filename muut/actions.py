#!/usr/bsin/env python

import functions

def move(direction):
    functions.move_player(direction)
    functions.guard_patrol()
    #look()

def use(item, item2=''):
    print("use " + item + item2)

def take(item):
    print("take " + item)

def examine(item):
    functions.examine_item(item)

def hide():
    print("hide")
    functions.guard_patrol()

def look():
    functions.get_room_desc()
    print("\n")

def items():
    print("items")

