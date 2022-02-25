import curses

def title(scr, y=0, txt=''):
    title_width = 60

    scr.addstr(y, 0, '-'*(title_width+3) )
    scr.addstr(y+1, 0, f'{( ( title_width-len(txt) ) // 2 )*"="}< {txt} >{( ( title_width-len(txt) ) // 2 )*"="}')
    scr.addstr(y+2, 0, '-'*(title_width+3) )

def start_screen(scr):

    while True:
        scr.clear()

        title(scr, txt='Jokenpô')

        scr.addstr('''
        J - jogar | I - instruções | ESC - sair
        ''')

        scr.refresh()

        key = scr.getkey()
        if ord(key) == 27:
            break
        elif ord(key) == 106:
            pass
            # jogar
        elif ord(key) == 105:
            instructions_screen(scr)

def instructions_screen(scr):
    scr.clear()

    title(scr, txt='Instruções')
    
    scr.addstr('''
    ESC - sair
    ''')
    scr.addstr('''
    O jogo consiste em escolher uma das 3 opções de ataque,
    tanto o jogador, quanto o computador. Após isso,
    o resultado é mostrado, e as pontuações registradas.
    Mas claro que o melhor jeito de aprender é jogando!
    ''')

    scr.refresh()

    while True:
        key = scr.getkey()
        if ord(key) == 27:
            break

def main(scr): # scr = screen

    start_screen(scr)

curses.wrapper(main) # Allow Curses to control the terminal window
