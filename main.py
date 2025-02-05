import screen
import art
import sell
import opening

from screen import Player_Inventory, Player_Values
from time import sleep

from travel_logic import Planet_travel

player_inventory = Player_Inventory(cargo=0, fuel=1,
                                    credits=20, docking_unit=0,
                                    translator=0, container=3,
                                    location=0)

player_values = Player_Values(num_of_trip=0, chance_of_success=70)

opening.op_scr()


def base():

    screen.clear_screen()
    art.header(art.location_calc(player_inventory.get_value("location")))
    art.kepernyo_calc(player_inventory.get_value("location"))
    screen.infopanel_1(player_inventory.get_value("cargo"), player_inventory.get_value("credits"), player_inventory.get_value("fuel") )

    print(f"Fuel num: {player_inventory.get_value("fuel")}")
    # print(f"Expl ch: {trav.get_chance_of_success()}")

    type = int(input("> What do you choose? (pick a number)"))

    while type < 1 or type > 4:
        type = int(input("> INVALID! What do you choose? (pick a number)"))

    if type == 1:
        screen.clear_screen()
        screen.infopanel_2(player_inventory.get_value("cargo"), player_inventory.get_value("credits"),player_inventory.get_value("fuel"), player_inventory.get_value("docking_unit"), player_inventory.get_value("translator"), player_inventory.get_value("container"))
        screen.wait()
        base()
    if type == 2:
        info()
    if type == 3:
        travel()

def info():
    screen.clear_screen()
    place = player_inventory.get_value("location")
    screen.infopanel_2(player_inventory.get_value("cargo"), player_inventory.get_value("credits"),
                       player_inventory.get_value("fuel"), player_inventory.get_value("docking_unit"),
                       player_inventory.get_value("translator"), player_inventory.get_value("container"))
    print(f"Your current planet: {art.location_calc(place)}\n")
    if place == 0:
        print("You cannot trade in space. Please travel to a planet first.")
    else:
        buy = int(input(f"> What would you like to buy?\n\t"
                        f"1. Cargo\n\t"
                        f"2. Fuel\n\t"
                        f"3. Equipment\n\t"
                        f"4. Go back\n"))
        while not 0 < buy < 5:
            buy = int(input("> INVALID! What do you choose? (pick a number)"))
        while buy != 4:
            if buy == 1:
                cargo = sell.buying_cargo(player_inventory.get_value("credits"), player_inventory.get_value("cargo"), player_inventory.get_value("container"))
                player_inventory.setvalue("cargo", cargo[0])
                player_inventory.setvalue("credits", cargo[1])
                screen.wait()
                screen.infopanel_2(player_inventory.get_value("cargo"), player_inventory.get_value("credits"),
                               player_inventory.get_value("fuel"), player_inventory.get_value("docking_unit"),
                               player_inventory.get_value("translator"), player_inventory.get_value("container"))
            if buy == 2:
                print("")
                fuel = sell.buying_fuel(player_inventory.get_value("credits"), player_inventory.get_value("fuel"))
                player_inventory.setvalue("credits", fuel[0])
                player_inventory.setvalue("fuel", fuel[1])
                screen.wait()
                screen.infopanel_2(player_inventory.get_value("cargo"), player_inventory.get_value("credits"),
                                   player_inventory.get_value("fuel"), player_inventory.get_value("docking_unit"),
                                   player_inventory.get_value("translator"), player_inventory.get_value("container"))
            if buy == 3:
                print("")
                eq = sell.buying_equipment(player_inventory.get_value("credits"), player_inventory.get_value("docking_unit"), player_inventory.get_value("translator"), player_inventory.get_value("container"))
                player_inventory.setvalue("credits", eq[0])
                player_inventory.setvalue("docking_unit", eq[1])
                player_inventory.setvalue("translator", eq[2])
                player_inventory.setvalue("container", eq[3])
                screen.infopanel_2(player_inventory.get_value("cargo"), player_inventory.get_value("credits"),
                                   player_inventory.get_value("fuel"), player_inventory.get_value("docking_unit"),
                                   player_inventory.get_value("translator"), player_inventory.get_value("container"))
            buy = int(input(f"> What would you like to buy?\n\t"
                            f"1. Cargo\n\t"
                            f"2. Fuel\n\t"
                            f"3. Equipment\n\t"
                            f"4. Go back \n"))
    screen.wait()
    base()

def travel():
    screen.clear_screen()
    print("\nWhere would you like to travel?\n\t1. Thorodin\n\t2. Ydalir\n\t3. Vidar\n\t4. Folkvang\n\n5. Go back\n")

    if player_inventory.get_value("fuel") <= 0:
        print(f"[You have no fuel left, so you cannot travel anymore]")
        sleep(2)
        base()

    type2 = int(input("> What do you choose? (pick a number)"))
    while type2 < 1 or type2 > 5:
        type2 = int(input("> INVALID! What do you choose? (pick a number)"))
    while player_inventory.get_value("location") == type2:
        type2 = int(input("> You are already here! (pick a different number)"))

    if type2 == 1:
        """
        curr_fuel = 
        curr_loc = 
        docking_unit = 

        chance_of_success = 
        num_of_trip = 
        """
        trav = Planet_travel(player_inventory.get_value("location"), "Thorodin",  player_inventory.get_value("fuel"), player_inventory.get_value("docking_unit"), player_values.get_value("chance_of_success"), player_values.get_value("num_of_trip"))
        # trav = Planet_travel(curr_loc, "Thorodin",  curr_fuel, docking_unit, chance_of_success, num_of_trip)

        results = trav.travel()
        """
        rem_fuel = results[0]
        rem_suc_chance = results[1]
        trips = results[2]
        """

        if (results[0]) <= 0:
            sleep(2)
            travel()

        player_values.setvalue("num_of_trip", results[2])
        player_values.setvalue("chance_of_success", results[1])

        player_inventory.setvalue("location", 1)
        
        player_inventory.setvalue("fuel", results[0])

        # sell.selling(3, 2, 1)
        #sell.selling(player_inventory.get_value("credits"), player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        selling = sell.selling(player_inventory.get_value("credits"),player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        player_inventory.setvalue("credits", selling[0])
        player_inventory.setvalue("cargo", selling[1])
        screen.wait()
        base()
    if type2 == 2:

        trav = Planet_travel(player_inventory.get_value("location"), "Ydalir", player_inventory.get_value("fuel"),
                             player_inventory.get_value("docking_unit"), player_values.get_value("chance_of_success"),
                             player_values.get_value("num_of_trip"))
        results = trav.travel()

        if (results[0]) <= 0:
            sleep(2)
            travel()

        player_values.setvalue("num_of_trip", results[2])
        player_values.setvalue("chance_of_success", results[1])
        player_inventory.setvalue("location", 2)
        player_inventory.setvalue("fuel", results[0])

        selling = sell.selling(player_inventory.get_value("credits"),player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        player_inventory.setvalue("credits", selling[0])
        player_inventory.setvalue("cargo", selling[1])
        screen.wait()
        base()
    if type2 == 3:

        trav = Planet_travel(player_inventory.get_value("location"), "Vidar", player_inventory.get_value("fuel"),
                             player_inventory.get_value("docking_unit"), player_values.get_value("chance_of_success"),
                             player_values.get_value("num_of_trip"))
        results = trav.travel()
        if (results[0]) <= 0:
            sleep(2)
            travel()
        player_values.setvalue("num_of_trip", results[2])
        player_values.setvalue("chance_of_success", results[1])
        player_inventory.setvalue("location", 3)
        player_inventory.setvalue("fuel", results[0])

        selling = sell.selling(player_inventory.get_value("credits"),player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        player_inventory.setvalue("credits", selling[0])
        player_inventory.setvalue("cargo", selling[1])
        screen.wait()
        base()
    if type2 == 4:

        trav = Planet_travel(player_inventory.get_value("location"), "Folkvang", player_inventory.get_value("fuel"),
                             player_inventory.get_value("docking_unit"), player_values.get_value("chance_of_success"),
                             player_values.get_value("num_of_trip"))
        results = trav.travel()

        if (results[0]) <= 0:
            sleep(2)
            travel()

        player_values.setvalue("num_of_trip", results[2])
        player_values.setvalue("chance_of_success", results[1])
        player_inventory.setvalue("location", 4)
        player_inventory.setvalue("fuel", results[0])

        selling = sell.selling(player_inventory.get_value("credits"),player_inventory.get_value("cargo"), player_inventory.get_value("translator"))
        player_inventory.setvalue("credits", selling[0])
        player_inventory.setvalue("cargo", selling[1])
        screen.wait()
        base()
    if type2 == 5:
        base()


base()
