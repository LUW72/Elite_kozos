from time import sleep
import os

def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux, macOS, and other Unix-based systems
        os.system('clear')

class Player_Inventory:
    def __init__(self, cargo, fuel, credits, docking_unit, translator, container, location):
        # Initialize the resource values
        self.resources = {
            "cargo": cargo,
            "fuel": fuel,
            "credits": credits,
            "docking_unit": docking_unit,
            "translator": translator,
            "container": container,
            "location":location
        }

    def increase(self, resource, amount=1):
        """Mennyiség növelése"""
        self.resources[resource] += amount
        return self.resources[resource]

    def decrease(self, resource, amount=1):
        """Mennyiség csökkentése."""
        self.resources[resource] -= amount
        return self.resources[resource]

    def setvalue(self, resource, value=1):
        """Mennyiség csökkentése."""
        self.resources[resource] = value
        return self.resources[resource]

    def get_value(self, resource):
        """ Kiiras """
        return self.resources[resource]


def fuel_drawer(fuel: int) -> str:
    if fuel == 2:
        return "||||||||||||"
    elif fuel == 1:
        return "|||||||     "
    else:
        return "  NO FUEL   "

def print_corrector(unit):
    if unit < 10:
        return f"0{unit}"
    return unit

def infopanel_1(cargo, credits, fuel):
    sleep(1)
    print(f"""
╔══════════════╦═══════════════╗                What would you like to do here?
║ Fuel         ║ {fuel_drawer(fuel)}  ║                1. Inventory
╠══════════════╬═══════════════╣                2. Trading, Buying Fuel
║ Cargo        ║ {print_corrector(cargo)}            ║                3. Travel to somewhere
╠══════════════╬═══════════════╣                4. Other
║ Credits      ║ {print_corrector(credits)}            ║
╚══════════════╩═══════════════╝
""")
    
    """
    print("-----------------------------------------------------------")
    print("Cargo: ", cargo)
    print("idk: ")
    print("----------------------------------------------------------")
    """
def infopanel_2(cargo, credits, docking_unit, translator, container):

    print(f"""
╔══════════════╦═══════════════╗ 
┌──────────────┬───────────────┐
│ cargo        │           {print_corrector(cargo)}  │
│ credits      │           {print_corrector(credits)}  │
│ docking_unit │           {print_corrector(docking_unit)}  │
│ translator   │           {print_corrector(translator)}  │
│ container    │           {print_corrector(container)}  │
└──────────────┴───────────────┘          
""")


def wait():
    sleep(1)
    input("> Type something to continue")

