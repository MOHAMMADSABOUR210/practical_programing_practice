import curses
stdscr = curses.initscr()

maxl = curses.LINES - 1
maxc = curses.COLS - 1

# print(maxl, maxc)
world = []

def init():
    for i in range(maxl):
        temp = []
        world.append(temp)
        for j in range(maxc):
            world[i].append('.')


curses.noecho()
curses.cbreak()
stdscr.keypad(True)

stdscr.addch(20,21,'0')
stdscr.addch(0,1,'1')
stdscr.addch(1,0,'2')
stdscr.addch(10,12,'f')

stdscr.refresh()
stdscr.getkey()