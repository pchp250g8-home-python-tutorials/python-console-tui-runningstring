# --encoding:utf-8--
import curses
import time

scr = curses.initscr()
curses.curs_set(0)
scr.clear()
scr.nodelay(True)
nCode = curses.ERR
nCounter = 0
strSpaces = " ".center(80)
strLine = "Hello World!!! Running String!!! Press Any Key To Exit!!!"
strLine = strSpaces + strLine + strSpaces
nStrLen = len(strLine) - 80
while nCode == curses.ERR:
    strSpaces = strLine[nCounter : nCounter + 80] 
    scr.addstr(10, 10, strSpaces)
    time.sleep(0.14)
    nCounter += 1
    if(nCounter >= nStrLen):
        nCounter = 0
    nCode = scr.getch()
curses.endwin()