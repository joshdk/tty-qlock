#!/usr/bin/env python
# -*- coding: utf-8 -*-
import locale
locale.setlocale(locale.LC_ALL, '')
from time import sleep
from datetime import datetime
import curses
import sys





#{{{ Initialize curses
def curses_init():
	""" Initialize curses
	returns the screen which curses is bound to.
	"""
	curses.initscr()
	if curses.has_colors() == True:
		curses.start_color()
		curses.use_default_colors()
	curses.noecho()
	curses.curs_set(0)

	screen = None
	try:
		screen = curses.initscr()
		screen.nodelay(1)
		screen.keypad(1)
		screen.clear()
	except:
		return None
	return screen
#}}}


#{{{ Finalize curses
def curses_fini(curses, screen=None):
	""" Standard clean-up for when program finishes
	"""
	if screen is not None:
		screen.getch()
		screen.clear()
	curses.endwin()
#}}}


#{{{ Color picker
def curses_colors(curses):
	""" Returns a method for setting colors
	"""
	def color_none(fg=None, bg=None):
		return curses.color_pair(0)

	if curses.has_colors() != True:
		return color_none

	# Iniaialize all possible color pairs
	for i, (fg, bg) in enumerate([(f, b) for b in range(-1, 8) for f in range(-1, 8)]):
		curses.init_pair(i+1, fg, bg)

	def color_full(fg=None, bg=None):
		if bg is None or bg == -1:
			bg = 0
		else:
			bg += 1

		if fg is None or fg == -1:
			fg = 0
		else:
			fg += 1

		if not 0 <= bg <= 8:
			return curses.color_pair(0)

		if not 0 <= fg <= 16:
			return curses.color_pair(0)

		if fg > 8: # bold?
			return curses.color_pair(9 * bg + (fg-8) + 1) | curses.A_BOLD
		else:
			return curses.color_pair(9 * bg + fg + 1)

	return color_full
#}}}




#{{{ A better text drawing routine
def draw_str(screen, y, x, text, attr=None):
	try:
		text = str(text)
		if attr is None:
			screen.addstr(y, x, text)
		else:
			screen.addstr(y, x, text, attr)
	except:
		pass
#}}}


#{{{ A better border drawing routine
def draw_border(screen, chars=[], attr=None, size=None, offset=None):

	(rows, cols) = screen.getmaxyx() if size is None else size
	(top, left)     = (0, 0) if offset is None else offset

	def _draw_str(y, x, text, attr=None):
		draw_str(screen, y+top, x+left, text, attr)

	if len(chars) < 1:
		return
	for y in range(1,rows-1):
		_draw_str(y, 0, chars[0], attr)

	if len(chars) < 2:
		return
	for y in range(1,rows-1):
		_draw_str(y, cols-1, chars[1], attr)

	if len(chars) < 3:
		return
	for x in range(1,cols-1):
		_draw_str(0, x, chars[2], attr)

	if len(chars) < 4:
		return
	for x in range(1,cols-1):
		_draw_str(rows-1, x, chars[3], attr)

	if len(chars) < 5:
		return
	_draw_str(0, 0, chars[4], attr)

	if len(chars) < 6:
		return
	_draw_str(0, cols-1, chars[5], attr)

	if len(chars) < 7:
		return
	_draw_str(rows-1, 0, chars[6], attr)

	if len(chars) < 8:
		return
	_draw_str(rows-1, cols-1, chars[7], attr)
#}}}


#{{{ Draw the clock
def draw_clock(screen, attrs=[], size=None, offset=None):

	(rows, cols) = screen.getmaxyx() if size is None else size
	(top, left)     = (0, 0) if offset is None else offset

	time = datetime.now()
	hour = time.hour
	minute = time.minute

	color_on  = attrs[0] if len(attrs) >= 1 else None
	color_off = attrs[1] if len(attrs) >= 2 else None

	def _draw_str(y, x, text, attr=color_on):
		draw_str(screen, y+top, x+left, text, attr)


#{{{ Draw empty grid
	_draw_str( 0,  0, "I   T   L   I   S   A   S   T   I   M   E", color_off)
	_draw_str( 2,  0, "A   C   Q   U   A   R   T   E   R   D   C", color_off)
	_draw_str( 4,  0, "T   W   E   N   T   Y   F   I   V   E   X", color_off)
	_draw_str( 6,  0, "H   A   L   F   B   T   E   N   F   T   O", color_off)
	_draw_str( 8,  0, "P   A   S   T   E   R   U   N   I   N   E", color_off)
	_draw_str(10,  0, "O   N   E   S   I   X   T   H   R   E   E", color_off)
	_draw_str(12,  0, "F   O   U   R   F   I   V   E   T   W   O", color_off)
	_draw_str(14,  0, "E   I   G   H   T   E   L   E   V   E   N", color_off)
	_draw_str(16,  0, "S   E   V   E   N   T   W   E   L   V   E", color_off)
	_draw_str(18,  0, "T   E   N   S   E   O'  C   L   O   C   K", color_off)
#}}}

#{{{ All
	_draw_str( 0,  0, "I   T")
	_draw_str( 0, 12, "I   S")
#}}}

#{{{
	if minute >= 35:
		_draw_str( 6, 36, "T   O")
	elif minute >= 5:
		_draw_str( 8,  0, "P   A   S   T")
#}}}

#{{{ Minutes
	if minute >= 55:
		_draw_str( 4, 24, "F   I   V   E")

	elif minute >= 50:
		_draw_str( 6, 20, "T   E   N")

	elif minute >= 45:
		_draw_str( 2,  0, "A")
		_draw_str( 2,  8, "Q   U   A   R   T   E   R")

	elif minute >= 40:
		_draw_str( 4,  0, "T   W   E   N   T   Y")

	elif minute >= 35:
		_draw_str( 4,  0, "T   W   E   N   T   Y")
		_draw_str( 4, 24, "F   I   V   E")

	elif minute >= 30:
		_draw_str( 6,  0, "H   A   L   F")

	elif minute >= 25:
		_draw_str( 4,  0, "T   W   E   N   T   Y")
		_draw_str( 4, 24, "F   I   V   E")

	elif minute >= 20:
		_draw_str( 4,  0, "T   W   E   N   T   Y")

	elif minute >= 15:
		_draw_str( 2,  0, "A")
		_draw_str( 2,  8, "Q   U   A   R   T   E   R")

	elif minute >= 10:
		_draw_str( 6, 20, "T   E   N")

	elif minute >= 5:
		_draw_str( 4, 24, "F   I   V   E")

	else:
		_draw_str(18, 20, "O'  C   L   O   C   K")
#}}}

#{{{ Hours
	if minute >= 35:
		hour += 1
	hour %= 12

	if hour == 1:
		_draw_str(10,  0, "O   N   E")

	elif hour == 2:
		_draw_str(12, 32, "T   W   O")

	elif hour == 3:
		_draw_str(10, 24, "T   H   R   E   E")

	elif hour == 4:
		_draw_str(12,  0, "F   O   U   R")

	elif hour == 5:
		_draw_str(12, 16, "F   I   V   E")

	elif hour == 6:
		_draw_str(10, 12, "S   I   X")

	elif hour == 7:
		_draw_str(16,  0, "S   E   V   E   N")

	elif hour == 8:
		_draw_str(14,  0, "E   I   G   H   T")

	elif hour == 9:
		_draw_str( 8, 28, "N   I   N   E")

	elif hour == 10:
		_draw_str(18,  0, "T   E   N")

	elif hour == 11:
		_draw_str(14, 20, "E   L   E   V   E   N")

	elif hour == 0:
		_draw_str(16, 20, "T   W   E   L   V   E")

#}}}

#}}}


#{{{ Draw everything
def draw(screen, attrs):
	(height, width) = screen.getmaxyx()

	(rows, cols) = (23, 49)

	if height < rows+2 or width < cols+2:
		screen.clear()
		screen.refresh()
		return

	top  = int(height/2 - rows/2)
	left = int( width/2 - cols/2)

	draw_clock(screen, attrs[0], offset=(top+2, left+4))
	draw_border(screen, ['┃','┃','━','━','┏','┓','┗','┛'], attrs[1], size=(rows, cols), offset=(top, left))
#}}}




#{{{ Run
def run():
	screen = curses_init()
	if screen is None:
		return 1

	colors = curses_colors(curses)

	redraw = lambda: draw(screen, [[colors(2), colors(0)], colors(0)])

	redraw()

#{{{ Main event loop
	while True:

		redraw()
		sleep(0.25)

		event = screen.getch()
		curses.flushinp()

		if event == curses.ERR:
			continue
		elif event == ord('q'):
			break
		elif event == ord('r'):
			screen.clear()
		elif event == curses.KEY_RESIZE:
			screen.clear()
#}}}

	curses_fini(curses, screen)

	return 0
#}}}


#{{{ Main
def main(argv=None):
	if argv is None:
		argv = sys.argv
	argc = len(argv)

	run()

	return 0


if __name__ == '__main__':
	sys.exit(main())
#}}}
