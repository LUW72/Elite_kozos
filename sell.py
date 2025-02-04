import random
from screen import Player_Inventory

def selling(credits:int, cargo:int, translator:int):
    return_ = []
    if cargo != 0:
        if translator != 0:
            margin = random.randrange(5, 66)
        else:
            margin = random.randint(-10, 51)
        crcr = cargo + cargo * margin / 100
    else:
        crcr = 0
    credits += int(crcr)
    cargo = 0

    print(f"\n[You made {crcr} credits after selling.]"
          f"\n[Your new balance is {credits} credits.]"
          f"\n\t[You now have {cargo} cargo.]")

    return [credits, cargo]

def buying_cargo(credits:int, cargo:int, container:int):
    buy = int(input(f"\nWould you like to buy cargo?\n"
                    "\t1. Yes\n"
                    "\t2. No\n"))
    how_much = 0
    if buy == 1:
        max_cargo = 5 + container*4
        if cargo == max_cargo:
            print(f"\n\t[You don't have enough space!]")
        else:
            how_much = int(input("\n> How much would you like to buy?: \n"))
            while how_much + cargo > max_cargo or how_much < 0:
                print(f"\n\t[You don't have enough space/Wrong data]\n")
                how_much = int(input(f"\n> How much would you like to buy: \n"))
            while credits < how_much:
                print("\n\t[You don't have enough credits]")
                how_much = int(input("\n> How much would you like to buy: \n"))

    cargo += how_much
    credits -= how_much
    print(f"\nYou now have {cargo} cargo."
          f"\nYour new balance is {credits} credits.")

    return [cargo, credits]

def buying_fuel(credits:int, fuel:int):
    how_much = 0
    if fuel != 2:
        buy = int(input(f"\nWould you like to buy fuel?"
                        "\n\t1. Yes"
                        "\n\t2. No\n"))
        if buy == 1:
            how_much = int(input("\n> How much fuel would you like to buy? (0-2): \n"))
            while how_much > 2 or how_much < 0:
                how_much = int(input(f"\n[Wrong data.]"
                                     f"\n> How much fuel would you like to buy? (0-2): \n"))
            while fuel + how_much > 2:
                how_much = int(input(f"\n[Not enough space.]"
                                     f"\n> How much fuel would you like to buy? (0-2): \n"))
            while credits < how_much:
                print("\n[You don't have enough credits.]")
                how_much = int(input("\n> How much would you like to buy (0-2): \n"))
        fuel += how_much
        credits -= how_much

        print(f"\nYou now have {fuel} fuel."
              f"\nYour new balance is {credits} credits.")

        return [credits, fuel]

def buying_equipment(credits:int, docking_unit:int, translator:int, container:int ):
        equip = []
        buy = int(input(f"\n> Would you like to buy equipment:\n" 
                    "\t1. Yes\n"
                    "\t2. No\n"))
        while buy == 1:
            which = int(input(f"\t1. Docking unit (10 credits)\n"
                              f"\t2. Translator (5 credits)\n"
                              f"\t3. Container (3 credits)\n"
                              f"\n> What would you like to buy?\n"))
            if which == 1:
                if credits < 10:
                    print(f"\n[You don't have enough credits for that.]")

                else:
                    if docking_unit != 1:
                        equip.append("docking unit")
                        docking_unit += 1
                        credits -= 10
                        print("\n[You bought a docking unit.]")
                    else:
                        print("\n[You already have a docking unit.]")

            elif which == 2:
                if credits < 5:
                    print(f"\n[You don't have enough credits for that.]")

                else:
                    if translator != 1:
                        equip.append("translator")
                        translator += 1
                        credits -= 5
                        print("\n[You bought a translator]")
                    else:
                        print("\n[You already have a translator]")

            elif which == 3:
                if credits < 3:
                    print(f"\n[You don't have enough credits for that.]")

                else:
                    container += 1
                    equip.append("container")
                    credits -= 3
                    print("\n[You bought a container]")

            else:
                print("[Wrong data]")

            buy = int(input("\n> Would you like to continue shopping?\n"
                "\n\t1. Yes"
                "\n\t2. No\n"))

        print(f"\n[You bought: {", ".join(map(str, equip))}.]"
              f"\n[Your new balance is {credits} credits.]")

        return [credits, docking_unit, translator, container]