import misc
from random import randint

options = ['Pedra', 'Papel', 'Tesoura']

results = [
    ['Empate', 'Derrota', 'Vitória'], 
    ['Vitória', 'Empate', 'Derrota'], 
    ['Derrota', 'Vitória', 'Empate']
]

def game(scr):
    
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
        if key not in ('0', '1', '2'):
            continue

        comp = randint(0, 2)

        misc.line(scr)

        scr.addstr(f'''
        Você jogou {options[int(key)]}
        ''')
        scr.addstr(f'''
        Computador jogou {options[comp]}
        ''')
        scr.addstr(f'''
        O resultado foi {results[int(key)][comp]}
        ''')
        scr.refresh()
