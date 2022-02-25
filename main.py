import curses

def main(scr): # scr = screen
    
    scr.clear() # cleans all screen content

    scr.addstr('Olá, Mundo!')

    scr.refresh() # relaods the screen content

    scr.getkey() # waits for the user to type

curses.wrapper(main) # Allow Curses to control the terminal window
