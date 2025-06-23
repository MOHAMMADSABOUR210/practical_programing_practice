import curses
import random 

stdscr = curses.initscr()


curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)

maxl = curses.LINES - 1
maxc = curses.COLS - 1

world = []
player_c = player_l = 0


def init():
    global player_l,player_c
    for i in range(maxl):
        world.append([])
        for j in range(maxc):
            world[i].append(' ' if random.random() > 0.03 else '.')
    player_l = random.randint(0, maxl)
    player_c = random.randint(0, maxc)


def drow():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i,j,world[i][j])
    stdscr.addch(player_l,player_c,'x')
    stdscr.refresh()


def move(c):
    '''get one of the aswd moved toward that direction'''
    global player_l,player_c
    if c == 'w':
        player_l -= 1 
    elif c == 's':
        player_l += 1 
    elif c == 'a':
        player_c -= 1
    else : 
        player_c += 1
    



init()
 
list_c = []
last_c = ''
while True:
    try : 
        c = stdscr.getkey()
        last_c = c
        list_c.append(c)
    except:
        c = last_c;
    if c in 'aswd':
        last_c = c
        move(c)
    elif c == 'q':
        break
    drow()

print(list_c)