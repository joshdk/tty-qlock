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
	curses.curs_set(0)
	curses.noecho()
	if curses.has_colors() == True:
		curses.start_color()
		curses.use_default_colors()

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
def draw_border(screen, chars=[], attr=None):
	rows, cols = screen.getmaxyx()

	screen.border(0)

	if len(chars) < 1:
		return
	for y in range(1,rows-1):
		draw_str(screen, y, 0, chars[0], attr)

	if len(chars) < 2:
		return
	for y in range(1,rows-1):
		draw_str(screen, y, cols-1, chars[1], attr)

	if len(chars) < 3:
		return
	for x in range(1,cols-1):
		draw_str(screen, 0, x, chars[2], attr)

	if len(chars) < 4:
		return
	for x in range(1,cols-1):
		draw_str(screen, rows-1, x, chars[3], attr)

	if len(chars) < 5:
		return
	draw_str(screen, 0, 0, chars[4], attr)

	if len(chars) < 6:
		return
	draw_str(screen, 0, cols-1, chars[5], attr)

	if len(chars) < 7:
		return
	draw_str(screen, rows-1, 0, chars[6], attr)

	if len(chars) < 8:
		return
	draw_str(screen, rows-1, cols-1, chars[7], attr)
#}}}


#{{{ Draw the clock
def draw_clock(screen, attrs=[]):

	time = datetime.now()
	hour = time.hour
	minute = time.minute

	color_on  = attrs[0] if len(attrs) >= 1 else None
	color_off = attrs[1] if len(attrs) >= 2 else None

#{{{ Draw empty grid
	draw_str(screen,  0,  0, "I   T   L   I   S   A   S   T   I   M   E", color_off)
	draw_str(screen,  2,  0, "A   C   Q   U   A   R   T   E   R   D   C", color_off)
	draw_str(screen,  4,  0, "T   W   E   N   T   Y   F   I   V   E   X", color_off)
	draw_str(screen,  6,  0, "H   A   L   F   B   T   E   N   F   T   O", color_off)
	draw_str(screen,  8,  0, "P   A   S   T   E   R   U   N   I   N   E", color_off)
	draw_str(screen, 10,  0, "O   N   E   S   I   X   T   H   R   E   E", color_off)
	draw_str(screen, 12,  0, "F   O   U   R   F   I   V   E   T   W   O", color_off)
	draw_str(screen, 14,  0, "E   I   G   H   T   E   L   E   V   E   N", color_off)
	draw_str(screen, 16,  0, "S   E   V   E   N   T   W   E   L   V   E", color_off)
	draw_str(screen, 18,  0, "T   E   N   S   E   O'  C   L   O   C   K", color_off)
#}}}

#{{{ All
	draw_str(screen,  0,  0, "I   T", color_on)
	draw_str(screen,  0, 12, "I   S", color_on)
#}}}

#{{{
	if minute >= 35:
		draw_str(screen,  6, 36, "T   O", color_on)
	elif minute >= 5:
		draw_str(screen,  8,  0, "P   A   S   T", color_on)
#}}}

#{{{ Minutes
	if minute >= 55:
		draw_str(screen,  4, 24, "F   I   V   E", color_on)

	elif minute >= 50:
		draw_str(screen,  6, 20, "T   E   N", color_on)

	elif minute >= 45:
		draw_str(screen,  2,  0, "A", color_on)
		draw_str(screen,  2,  8, "Q   U   A   R   T   E   R", color_on)

	elif minute >= 40:
		draw_str(screen,  4,  0, "T   W   E   N   T   Y", color_on)

	elif minute >= 35:
		draw_str(screen,  4,  0, "T   W   E   N   T   Y", color_on)
		draw_str(screen,  4, 24, "F   I   V   E", color_on)

	elif minute >= 30:
		draw_str(screen,  6,  0, "H   A   L   F", color_on)

	elif minute >= 25:
		draw_str(screen,  4,  0, "T   W   E   N   T   Y", color_on)
		draw_str(screen,  4, 24, "F   I   V   E", color_on)

	elif minute >= 20:
		draw_str(screen,  4,  0, "T   W   E   N   T   Y", color_on)

	elif minute >= 15:
		draw_str(screen,  2,  0, "A", color_on)
		draw_str(screen,  2,  8, "Q   U   A   R   T   E   R", color_on)

	elif minute >= 10:
		draw_str(screen,  6, 20, "T   E   N", color_on)

	elif minute >= 5:
		draw_str(screen,  4, 24, "F   I   V   E", color_on)

	else:
		draw_str(screen, 18, 20, "O'  C   L   O   C   K", color_on)
#}}}

#{{{ Hours
	if minute >= 35:
		hour += 1
	hour %= 12

	if hour == 1:
		draw_str(screen, 10,  0, "O   N   E", color_on)

	elif hour == 2:
		draw_str(screen, 12, 32, "T   W   O", color_on)

	elif hour == 3:
		draw_str(screen, 10, 24, "T   H   R   E   E", color_on)

	elif hour == 4:
		draw_str(screen, 12,  0, "F   O   U   R", color_on)

	elif hour == 5:
		draw_str(screen, 12, 16, "F   I   V   E", color_on)

	elif hour == 6:
		draw_str(screen, 10, 12, "S   I   X", color_on)

	elif hour == 7:
		draw_str(screen, 16,  0, "S   E   V   E   N", color_on)

	elif hour == 8:
		draw_str(screen, 14,  0, "E   I   G   H   T", color_on)

	elif hour == 9:
		draw_str(screen,  8, 28, "N   I   N   E", color_on)

	elif hour == 10:
		draw_str(screen, 18,  0, "T   E   N", color_on)

	elif hour == 11:
		draw_str(screen, 14, 20, "E   L   E   V   E   N", color_on)

	elif hour == 0:
		draw_str(screen, 16, 20, "T   W   E   L   V   E", color_on)

#}}}

#}}}


#{{{ Curses class
class Curses:

	def __init__(self, screen=None):
		self.screen = curses_init() if screen is None else screen
		self.colors = curses_colors(curses)
		self.container = None
		self.clock = None
		self.frame = 0


	def invalidate(self):
		if self.container is not None or self.clock is not None:
			self.screen.erase()
		self.container = None
		self.clock = None


	def update(self):
		if self.container is None or self.clock is None:
			(maxy, maxx) = self.screen.getmaxyx()
			if maxy < 23 or maxx < 49:
				self.invalidate()
			top  = int(maxy/2 - 23/2)
			left = int(maxx/2 - 49/2)
			self.container = self.screen.derwin(23, 49, top, left)
			self.clock = self.container.derwin(19, 41, 2, 4)


	def redraw(self):
		(maxy, maxx) = self.screen.getmaxyx()
		if maxy < 23 or maxx < 49:
			self.invalidate()
			return
		if self.container is None or self.clock is None:
			self.update()
		self.frame += 1
		self.screen.touchwin()
		draw_border(self.container, ['┃','┃','━','━','┏','┓','┗','┛'], self.colors(0))
		draw_clock(self.clock, [self.colors(2), self.colors(0)])
		# draw_str(self.screen, 0, 0, "frame: "+str(self.frame))
		self.screen.refresh()
#}}}




#{{{ Run
def run(screen=None):
	screen = curses_init()

	widget = Curses(screen)

#{{{ Main event loop
	while True:

		widget.redraw()
		sleep(0.1)

		event = screen.getch()
		curses.flushinp()

		if event == curses.ERR:
			continue
		elif event == ord('q'):
			break
		elif event == ord('r'):
			widget.invalidate()
		elif event == curses.KEY_RESIZE:
			widget.invalidate()
			continue
#}}}

	curses_fini(curses, screen)

	return 0
#}}}



#{{{ Main
def main(argv=None):
	if argv is None:
		argv = sys.argv
	argc = len(argv)

	curses.wrapper(run)

	return 0


if __name__ == '__main__':
	sys.exit(main())
#}}}
