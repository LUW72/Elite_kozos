import screen
import art
import sell
import os

from screen import Player_Inventory
from time import sleep


player_inventory = Player_Inventory(cargo=0, fuel=1, credits=10, docking_unit=0, translator=0, container=0, location=0)


def base():


    screen.clear_screen()
    art.header(art.location_calc(player_inventory.get_value("location")))
    art.kepernyo_calc(player_inventory.get_value("location"))
    screen.infopanel_1(player_inventory.get_value("cargo"), player_inventory.get_value("credits"), player_inventory.get_value("fuel") )

    type = int(input("> What do you choose? (pick a number)"))

    while type < 1 or type > 4:
        type = int(input("> INVALID! What do you choose? (pick a number)"))

    if type == 1:
        screen.clear_screen()
        screen.infopanel_2(player_inventory.get_value("cargo"), player_inventory.get_value("credits"), player_inventory.get_value("docking_unit"), player_inventory.get_value("translator"), player_inventory.get_value("container"))
        sleep(1)
        input("> Type something to continue")
        base()
    if type == 2:
        info()
    if type == 3:
        travel()

def info():
    screen.clear_screen()
    place = player_inventory.get_value("location")
    print(f"Information about planet: {art.location_calc(place)}")
    input("\n> Type something to continue")
    base()

def travel():
    screen.clear_screen()
    print("\nWhere would you like to travel?")
    print("1. Thorodin")
    print("2. Ydalir")
    print("3. Vidar")
    print(f"4. Folkvang\n")

    type2 = int(input("> What do you choose? (pick a number)"))
    while type2 < 1 or type2 > 4:
        type2 = int(input("> INVALID! What do you choose? (pick a number)"))
    if type2 == 1:
        player_inventory.value("location", 1)
        sell.selling(player_inventory.get_value("credits"), player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        base()
    if type2 == 2:
        player_inventory.value("location", 2)
    if type2 == 3:
        player_inventory.value("location", 3)
    if type2 == 4:
        player_inventory.value("location", 4)




base()