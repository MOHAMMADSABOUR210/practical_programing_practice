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
    for i in range(-1 , maxl + 1):
        world.append([])
        for j in range(-1 , maxc + 1):
            world[i].append(' ' if random.random() > 0.03 else '.')
    player_l = random.randint(0, maxl)
    player_c = random.randint(0, maxc)


def drow():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i,j,world[i][j])
    stdscr.addch(player_l,player_c,'x')
    stdscr.refresh()


def in_range(num,max_chek):
    if num > max_chek - 1 :
        return 0
    elif num < 0 :
        return max_chek - 1
    else :
        return num
    
def chek_Obstacle(num_i,num_j):
    if num_i < 0 or num_i > maxl:
        return True
    if num_j < 0 or num_j > maxc:
        return True
    if world[num_i][num_j] != '.' :
        return True
    return False



def move(c):
    '''get one of the aswd moved toward that direction'''
    global player_l,player_c
    if c == 'w' and chek_Obstacle(player_l-1,player_c):
        player_l -= 1 
    elif c == 's'and chek_Obstacle(player_l+1,player_c):
        player_l += 1 
    elif c == 'a'and chek_Obstacle(player_l,player_c-1):
        player_c -= 1
    elif c == 'd'and chek_Obstacle(player_l,player_c+1): 
        player_c += 1

    player_c = in_range(player_c,maxc)
    player_l = in_range(player_l,maxl)



init()
 
list_c = []
# last_c = ''
while True:
    try : 
        c = stdscr.getkey()
        # last_c = c
        list_c.append(c)
    except:
        c = '';
    if c in 'aswd':
        last_c = c
        move(c)
    elif c == 'q':
        break
    drow()

print(list_c)