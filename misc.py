def title(scr, y=0, txt=''):
    title_width = 60

    scr.addstr(y, 0, '-'*(title_width+4) )
    scr.addstr(y+1, 0, f'{( ( title_width-len(txt) ) // 2 )*"="}< {txt} >{( ( title_width-len(txt) ) // 2 )*"="}')
    scr.addstr(y+2, 0, '-'*(title_width+4) )