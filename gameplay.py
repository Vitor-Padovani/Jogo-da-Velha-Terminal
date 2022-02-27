import misc
from random import randint

options = [
['Pedra', '(º_)'],
['Papel',  '[ ]'],
['Tesoura',  '8<']
 ]

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

    while True:
        key = scr.getkey()
        if ord(key) == 27:
            break
        if key not in ('0', '1', '2'):
            continue

        scr.clear()
        misc.title(scr, txt='Gameplay')
        scr.addstr('''
    0 - pedra | 1 - papel | 2 - tesoura | ESC - sair
        ''')

        comp = randint(0, 2)

        misc.line(scr, 4, 5)
        
        scr.addstr(6, 23, options[int(key)][1])
        scr.addstr(7, 22, options[int(key)][0])

        scr.addstr(6, 29, 'X')

        scr.addstr(6, 33, options[comp][1])
        scr.addstr(7, 32, options[comp][0])

        scr.addstr(9, 20, f'Você jogou: {options[int(key)][0]}')
        scr.addstr(10, 15, f'Computador jogou: {options[comp][0]}')
        scr.addstr(11, 16, f'O resultado foi: {results[int(key)][comp]}')

        scr.refresh()
