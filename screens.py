import gameplay
import misc

def start_screen(scr):

    while True:
        scr.clear()

        misc.title(scr, txt='Jokenpô')

        scr.addstr('''
        J - jogar | I - instruções | ESC - sair
        ''')

        scr.refresh()

        key = scr.getkey()
        if ord(key) == 27:
            break

        elif ord(key) == 106:
            gameplay.game(scr)

        elif ord(key) == 105:
            instructions_screen(scr)

def instructions_screen(scr):
    scr.clear()

    misc.title(scr, txt='Instruções')
    
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
