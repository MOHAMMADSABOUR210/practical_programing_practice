import curses
import random 
import time

stdscr = curses.initscr()


testing = False

curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)
curses.curs_set(False)


maxl = curses.LINES - 1
maxc = curses.COLS - 1


score = 0
world = []
player_c = player_l = 0
enemy = []
food = []

def random_place():
    a = random.randint(0,maxl)
    b = random.randint(0,maxc)
    while world[a][b] != ' ':
        a = random.randint(0,maxl)
        b = random.randint(0,maxc)
    return a , b             

def init():
    global player_l,player_c
    for i in range(-1 , maxl + 1):
        world.append([])
        for j in range(-1 , maxc + 1):
            world[i].append(' ' if random.random() > 0.03 else '.')
    
    for i in range(10):
        fl , fc = random_place()
        fa = random.randint(100,1000)
        food.append((fl,fc,fa))

    for i in range(3):
            el , ec = random_place()
            enemy.append((el,ec))


    player_l , player_c = random_place()


def drow():
    global score
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i,j,world[i][j])
    stdscr.addstr(1,1,f"score {score}")

    for f in food:
        fl , fc, fa = f 
        stdscr.addch(fl,fc,'*')
    
    for e in enemy:
        el , ec = e
        stdscr.addch(el,ec,'E')


    stdscr.addch(player_l,player_c,'x')
    stdscr.refresh()


def in_range(num,max_chek):
    if num > max_chek - 1 :
        return 0
    elif num < 0 :
        return max_chek - 1
    else :
        return num
    
def check_Obstacle(num_i,num_j):
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
    if c == 'w' and check_Obstacle(player_l-1,player_c):
        player_l -= 1 
    elif c == 's'and check_Obstacle(player_l+1,player_c):
        player_l += 1 
    elif c == 'a'and check_Obstacle(player_l,player_c-1):
        player_c -= 1
    elif c == 'd'and check_Obstacle(player_l,player_c+1): 
        player_c += 1

    player_c = in_range(player_c,maxc)
    player_l = in_range(player_l,maxl)


def check_food():
    global score
    for i in range(len(food)) : 
        fl, fc, fa = food[i]
        fa -= 1 
        if fl == player_l and fc == player_c:
            score += 10 
            nfl , nfc = random_place()
            nfa = random.randint(100,1000)
            food[i] = (nfl, nfc, nfa)
        elif fa <= 0:
            nfl , nfc = random_place()
            nfa = random.randint(100,1000)
            food[i] = (nfl, nfc, nfa)
        else :
            food[i] = (fl, fc, fa)


def move_enemy():
    for i in range(len(enemy)):
        el , ec = enemy[i]
        if el == player_l and ec == player_c and not testing:
            stdscr.addstr(maxl//2,maxc//2,"YOU DIED!!!")
            stdscr.refresh()
            time.sleep(3)
            return True
        if random.random() > 0.9 :
            if el > player_l: 
                el -= 1
            el = in_range(el , maxl)
            ec = in_range(ec , maxc)
            enemy[i] = (el,ec)

        if random.random() > 0.9 :
            if ec > player_c:
                ec -= 1
            el = in_range(el , maxl)
            ec = in_range(ec , maxc)
            enemy[i] = (el,ec)

        if random.random() > 0.9 :
            if el < player_l:
                el += 1            
            el = in_range(el , maxl)
            ec = in_range(ec , maxc)
            enemy[i] = (el,ec)

        if random.random() > 0.9 :
            if ec < player_c:
                ec += 1 
            el = in_range(el , maxl)
            ec = in_range(ec , maxc)
            enemy[i] = (el,ec)

init()
 
list_c = []
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
    check_food()
    if move_enemy():
        break
    time.sleep(0.01)

    drow()


stdscr.addstr(maxl//2,maxc//2,"Game Over!!")
stdscr.refresh()
time.sleep(2)
