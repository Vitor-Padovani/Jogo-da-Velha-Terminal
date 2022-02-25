import misc

def gameplay(scr):
    
    scr.clear()
    misc.title(scr, txt='Gameplay')
    scr.addstr('''
    0 - pedra | 1 - papel | 2 - tesoura | ESC - sair
    ''')
    scr.refresh()

    while True:
        key = scr.getkey()
        if ord(key) == 27:
            break
