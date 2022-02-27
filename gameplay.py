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
    scr.refresh()

    while True:
        key = scr.getkey()
        if ord(key) == 27:
            break
        if key not in ('0', '1', '2'):
            continue

        comp = randint(0, 2)

        misc.line(scr, 5, 5)
        
        scr.clear()
        scr.addstr(6, 5, options[int(key)][1])
        scr.addstr(6, 20, options[comp][1])
        scr.addstr(16, 5, results[int(key)][comp])
        scr.refresh()
