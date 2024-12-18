import random
import main

def selling(credits:int, cargo:int, translator:int):
    if cargo != 0:
        if translator != 0:
            margin = random.randrange(5, 66)
        else:
            margin = random.randint(-10, 51)
        crcr = cargo + cargo * margin / 100
    else:
        crcr = 0
    credits += cargo
    cargo = 0

    main.player_inventory.value("cargo", cargo)
    main.player_inventory.value("credits", credits)

    print(f"You made {crcr} credits after selling.\n"
          f"Your new balance is {credits} credits.\n"
          f"You now have {cargo} cargo.")





def buying_cargo(credits:int, cargo:int, container:int):
    buy = int(input("Would you like to buy cargo?: "))
    how_much = 0
    if buy:
        max_cargo = 5 + container*4
        if cargo == max_cargo:
            print("You don't have enough space.")
        else:
            how_much = int(input("How much would you like to buy?: "))
            while how_much + cargo > max_cargo or how_much < 0:
                print("You don't have enough space/Wrong data.")
                how_much = int(input("How much would you like to buy?: "))
            while credits < how_much:
                print("You don't have enough credits.")
                how_much = int(input("How much would you like to buy?: "))

    cargo += how_much
    credits -= how_much
    print(f"You now have {cargo} cargo.\n"
          f"Your new balance is {credits} credits.")


def buying_fuel(credits:int, fuel:int):
    how_much = 0
    if fuel != 2:
        buy = int(input("Would you like to buy fuel?: "))
        if buy:
            how_much = int(input("How much fuel would you like to buy?(0-2): "))
            while how_much > 2 or how_much < 0:
                how_much = int(input(f"Wrong data."
                                     f"How much fuel would you like to buy?(0-2): "))
            while fuel + how_much > 2:
                how_much = int(input(f"Not enough space."
                                     f"How much fuel would you like to buy?(0-2): "))
            while credits < how_much:
                print("You don't have enough credits.")
                how_much = int(input("How much would you like to buy?: "))
        fuel += how_much
        credits -= how_much

        print(f"You now have {fuel} fuel.\n"
              f"Your new balance is {credits} credits.")

def buying_equipment(credits:int, docking_unit:int, translator:int, container:int ):
        equip = []
        buy = int(input("Would you like to buy equipment?: "))
        while buy == 1:
            which = int(input(f"Docking unit (10 credits): 1\n"
                              f"Translator (5 credits): 2\n"
                              f"Container (3 credits): 3\n"
                              f"What would you like to buy?: "))
            if which == 1:
                if credits < 10:
                    print(f"You don't have enough credits for that.")


                else:
                    if docking_unit != 1:
                        equip.append("docking unit")
                        docking_unit += 1
                        credits -= 10
                        print("You bought a docking unit.")
                    else:
                        print("You already have a docking unit.")

            elif which == 2:
                if credits < 5:
                    print(f"You don't have enough credits for that.")

                else:
                    if translator != 1:
                        equip.append("transator")
                        translator += 1
                        credits -= 5
                        print("You bought a translator.")
                    else:
                        print("You already have a translator.")


            elif which == 3:
                if credits < 3:
                    print(f"You don't have enough credits for that.")

                else:
                    container += 1
                    equip.append("container")
                    credits -= 3
                    print("You bought a container.")

            else:
                print("Wrong data.")




            buy = int(input("Would you like to continue shopping~?: "))

        print(f"You bought: {equip}.\n"
              f"Your new balance is {credits} credits.")


























