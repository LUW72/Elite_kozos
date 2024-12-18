import curses

def navigation_system(stdscr):
    # Disable cursor and enable keypad input
    curses.curs_set(0)
    stdscr.keypad(True)

    # Menu options
    options = ["Option 1", "Option 2", "Option 3"]
    current_option = 0  # Track the currently selected option

    while True:
        # Clear the screen
        stdscr.clear()

        # Display the options
        for i, option in enumerate(options):
            if i == current_option:
                # Highlight the selected option
                stdscr.addstr(i, 0, option, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, option)

        # Refresh the screen
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        # Handle arrow key input
        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1  # Move up
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1  # Move down
        elif key == 10:  # Enter key
            # Return the selected option
            return current_option + 1

def main():
    # Start the curses application
    selected_option = curses.wrapper(navigation_system)
    print(f"You selected Option {selected_option}")

if __name__ == "__main__":
    main()