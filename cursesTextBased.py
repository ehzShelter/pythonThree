import curses
from curses.textpad import Textbox, rectangle

def main(stdscr):
    stdscr.addstr(0, 0, "hit")

    editwin = curses.newwin(5, 30, 2, 1)
    rectangle(stdscr, 1, 0, 1 + 5 + 1, 1+ 30 + 1)
    stdscr.refresh()

    box = Textbox(editwin)

    box.edit()

    message = box.gather()

    print(message)
