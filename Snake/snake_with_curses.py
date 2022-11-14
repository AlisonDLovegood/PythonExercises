import random
import curses

# CONFIG DA CURSES
height, width = curses.initscr().getmaxyx()
window = curses.newwin(height, width, 0, 0)

curses.curs_set(False)
window.keypad(True)
window.nodelay(True)


def game():
    # JOGO
    # limites de movimentacao superior e inferior
    for pos in range(0, width-1):
        window.addch(0, pos, '#')
        window.addch(height-1, pos, '#')

    for pos in range(0, height-1):
        window.addch(pos, 0, '#')
        window.addch(pos, width-1, '#')

    #  cobra
    snake = [[2, 4], [2, 3], [2, 2]]
    for pos in range(0, len(snake)):
        window.addch(snake[pos][0], snake[pos][1], '#')
    head_position = [2, 4]

    # environment variables
    apple = [5, 5]
    window.addch(apple[0], apple[1], '#')
    key = -1
    new_key = curses.KEY_RIGHT
    last_position = 'r'
    score = 0
    speed = 100

    while True:
        new_key = window.getch()
        # keep the last key pressed
        key = key if new_key == -1 else new_key

        # impossible go to back
        if key == curses.KEY_DOWN and last_position != 'u':
            last_position = 'd'
        elif key == curses.KEY_UP and last_position != 'd':
            last_position = 'u'
        elif key == curses.KEY_LEFT and last_position != 'r':
            last_position = 'l'
        elif key == curses.KEY_RIGHT and last_position != 'l':
            last_position = 'r'

        # increment or decrement about the head
        if last_position == 'r':
            head_position[1] += 1
        elif last_position == 'l':
            head_position[1] -= 1
        elif last_position == 'u':
            head_position[0] -= 1
        elif last_position == 'd':
            head_position[0] += 1

        # position of the head = apple
        if head_position == apple:
            score += 1
            apple = [random.randint(1, height-2), random.randint(1, width-2)]
            window.addch(apple[0], apple[1], '#')
            speed = speed - 10 if speed - 10 > 5 else speed
        # hit the ends
        elif (head_position[0] == height-1 or head_position[0] == 0 or head_position[1] == width-1 or head_position[1] == 0):
            break
        # remove a position of the tale
        else:
            tale = snake.pop()
            window.addch(tale[0], tale[1], ' ')

        # add in tale
        snake.insert(0, list(head_position))
        window.addch(head_position[0], head_position[1], '#')

        # touch yourself
        if snake[0] in snake[1:]:
            break

        curses.napms(speed)
        window.refresh()

    window.addstr(int(height/2), int(width/2.5), "Your score was: "+str(score))
    window.refresh()
    curses.napms(2000)
    curses.endwin()


game()
