import unicurses as curses
from tools import *

name = 'Tuntematon manageri'

# Pääohjelma
def main():
	stdscr = curses.initscr()
	curses.keypad(stdscr, True)
	curses.curs_set(False)
	curses.noecho()
	curses.start_color()

	select = mainmenu()
	curses.erase()
	if (select == 3):
		pass

	elif (select == 2):
		curses.mvaddstr(1,1, "Lataa peli")

	elif (select == 1):
		newgame()
		create_game()
		game_main_loop()	

	curses.endwin()

# Päävalikko
def mainmenu():
	menu_x = 15
	menu_y = 5
	cursor_location = menu_y

	key = 0
	while (key != 10):
		curses.mvaddstr(menu_y, menu_x, "1. Uusi peli")
		curses.mvaddstr(menu_y + 2, menu_x, "2. Lataa peli")
		curses.mvaddstr(menu_y + 4, menu_x, "3. Poistu")
		curses.mvaddstr(cursor_location, menu_x - 4, "->")

		key = curses.getch()
		if (key == 258 and cursor_location < menu_y + 4):
			curses.mvaddstr(cursor_location, menu_x - 4, "  ")
			cursor_location += 2

		elif (key == 259 and cursor_location > menu_y):
			curses.mvaddstr(cursor_location, menu_x - 4, "  ")
			cursor_location -= 2

	if (cursor_location == 5):
		return 1
	elif (cursor_location == 7):
		return 2
	elif (cursor_location == 9):
		return 3

# Uusi peli
def newgame():
	global name
	curses.erase()
	curses.mvaddstr(1, 1, "UUSI PELI")
	curses.mvaddstr(3, 1, "Kirjoita nimesi:")
	curses.echo()
	curses.move(4, 1)
	name = curses.getstr().decode(encoding="utf-8")
	curses.noecho()
	
	curses.mvaddstr(12, 1, name)
	curses.mvaddstr(10, 1, "Onko tiedot oikein? (K/E)")
	while 1:
		key = curses.getch()
		if (check_key(key, "k") or key == 27):
			break
		elif(key == ord('e') or key == ord('E')):
			newgame()

# Luo tietokannat ja muut asetukset
def create_game():
	pass

# Pelin päälooppi
def game_main_loop():
	running = 1
	week = 1
	while (week < 10):
		curses.erase()
		curses.mvaddstr(1, 1, "Tervetuloa Manageri: ")
		curses.addstr(name)
		curses.mvaddstr(2, 1, "VIIKKO ")
		curses.addstr(week)
		curses.addstr("/50")
		week += 1

		curses.getch()

# Suorita
if (__name__ == "__main__"):
	main()


# 260 Vasen
# 261 Oikea
# 259 Ylös
# 258 Alas