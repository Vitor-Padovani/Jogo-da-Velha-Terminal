import curses
import screens

def main(scr): # scr = screen

    screens.start_screen(scr)

curses.wrapper(main) # Allow Curses to control the terminal window
