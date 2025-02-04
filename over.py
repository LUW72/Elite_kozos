import os
from time import sleep

def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux, macOS, and other Unix-based systems
        os.system('clear')

def bad_ending(reason:str):
    clear_screen()
    sleep(1)
    print(f"GAME OVER\n\n")
    print(f"Your game has ended because of: {reason}\n")
    input(f"Press enter to continue...")
    quit()