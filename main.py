import screen
import art
import sell
import opening

from screen import Player_Inventory
from time import sleep

player_inventory = Player_Inventory(cargo=0, fuel=1,
                                    credits=20, docking_unit=0,
                                    translator=0, container=3,
                                    location=0)


opening.op_scr()


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
        screen.wait()
        base()
    if type == 2:
        info()
    if type == 3:
        travel()

def info():
    screen.clear_screen()
    place = player_inventory.get_value("location")
    print(f"Yout current planet: {art.location_calc(place)}\n")
    cargo = sell.buying_cargo(player_inventory.get_value("credits"), player_inventory.get_value("cargo"), player_inventory.get_value("container"))
    player_inventory.setvalue("cargo", cargo[0])
    player_inventory.setvalue("credits", cargo[1])
    screen.wait()
    print("")
    fuel = sell.buying_fuel(player_inventory.get_value("credits"), player_inventory.get_value("fuel"))
    player_inventory.setvalue("credits", fuel[0])
    player_inventory.setvalue("fuel", fuel[1])
    screen.wait()
    print("")
    eq = sell.buying_equipment(player_inventory.get_value("credits"), player_inventory.get_value("docking_unit"), player_inventory.get_value("translator"), player_inventory.get_value("container"))
    player_inventory.setvalue("credits", eq[0])
    player_inventory.setvalue("docking_unit", eq[1])
    player_inventory.setvalue("translator", eq[2])
    player_inventory.setvalue("container", eq[3])
    screen.wait()
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
        player_inventory.setvalue("location", 1)
        # sell.selling(3, 2, 1)
        #sell.selling(player_inventory.get_value("credits"), player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        selling = sell.selling(player_inventory.get_value("credits"),player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        player_inventory.setvalue("credits", selling[0])
        player_inventory.setvalue("cargo", selling[1])
        screen.wait()
        base()
    if type2 == 2:
        player_inventory.setvalue("location", 2)
        selling = sell.selling(player_inventory.get_value("credits"),player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        player_inventory.setvalue("credits", selling[0])
        player_inventory.setvalue("cargo", selling[1])
        screen.wait()
        base()
    if type2 == 3:
        player_inventory.setvalue("location", 3)
        selling = sell.selling(player_inventory.get_value("credits"),player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        player_inventory.setvalue("credits", selling[0])
        player_inventory.setvalue("cargo", selling[1])
        screen.wait()
        base()
    if type2 == 4:
        player_inventory.setvalue("location", 4)
        selling = sell.selling(player_inventory.get_value("credits"),player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        player_inventory.setvalue("credits", selling[0])
        player_inventory.setvalue("cargo", selling[1])
        screen.wait()
        base()



base()