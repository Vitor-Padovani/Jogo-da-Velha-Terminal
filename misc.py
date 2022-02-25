line_width = 60

def title(scr, y=0, txt=''):
    scr.addstr(y, 0, '-'*(line_width+4) )
    scr.addstr(y+1, 0, f'{( ( line_width-len(txt) ) // 2 )*"="}< {txt} >{( ( line_width-len(txt) ) // 2 )*"="}')
    scr.addstr(y+2, 0, '-'*(line_width+4) )

def line(scr):
    scr.addstr('-'*(line_width+4) )
