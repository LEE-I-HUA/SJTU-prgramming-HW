# click.py
from graphics import *

def main():
    # call a graphic window name "click me"
    win = GraphWin("Click Me!!")
    # click the window for ten times the shell will return the values of the points u clicked. 
    for i in range ( 10 ):
        p = win.getMouse()
        print("You clicked at: ", p.getX(), p.getY())

main()
