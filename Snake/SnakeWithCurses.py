import random
import curses

# CONFIG DA CURSES
height, width = curses.initscr().getmaxyx()
window = curses.newwin(height, width, 0, 0)

curses.curs_set(False)
window.keypad(True)
window.nodelay(True)

# JOGO
# limites de movimentacao superior e inferior
for pos in range(0, width-1):
    window.addch(0, pos, '#')
    window.addch(height-1, pos, '#')

for pos in range(0, height-1):
    window.addch(pos, 0, '#')
    window.addch(pos, width-1, '#')

#  cobra
