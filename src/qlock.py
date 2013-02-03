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


#{{{ Create clock mask
def _build_mask(time):
	mask = set()

	#  0: I   T   L   I   S   A   S   T   I   M   E
	#
	# 11: A   C   Q   U   A   R   T   E   R   D   C
	#
	# 22: T   W   E   N   T   Y   F   I   V   E   X
	#
	# 33: H   A   L   F   B   T   E   N   F   T   O
	#
	# 44: P   A   S   T   E   R   U   N   I   N   E
	#
	# 55: O   N   E   S   I   X   T   H   R   E   E
	#
	# 66: F   O   U   R   F   I   V   E   T   W   O
	#
	# 77: E   I   G   H   T   E   L   E   V   E   N
	#
	# 88: S   E   V   E   N   T   W   E   L   V   E
	#
	# 99: T   E   N   S   E   O'  C   L   O   C   K

	mask.update([0,1,3,4]) # IT IS

	hour = time.hour
	minute = time.minute


#{{{ Minute masks
	if minute >= 55:
		mask.update([28, 29, 30, 31]) # FIVE
		mask.update([42, 43]) # TO
		hour += 1

	elif minute >= 50:
		mask.update([38, 39, 40]) # TEN
		mask.update([42, 43]) # TO
		hour += 1

	elif minute >= 45:
		mask.update([11]) # A
		mask.update([13, 14, 15, 16, 17, 18, 19]) # QUARTER
		mask.update([42, 43]) # TO
		hour += 1

	elif minute >= 40:
		mask.update([22, 23, 24, 25, 26, 27]) # TWENTY
		mask.update([42, 43]) # TO
		hour += 1

	elif minute >= 35:
		mask.update([22, 23, 24, 25, 26, 27]) # TWENTY
		mask.update([28, 29, 30, 31]) # FIVE
		mask.update([42, 43]) # TO
		hour += 1

	elif minute >= 30:
		mask.update([33, 34, 35, 36]) # HALF
		mask.update([44, 45, 46, 47]) # PAST

	elif minute >= 25:
		mask.update([22, 23, 24, 25, 26, 27]) # TWENTY
		mask.update([28, 29, 30, 31]) # FIVE
		mask.update([44, 45, 46, 47]) # PAST

	elif minute >= 20:
		mask.update([22, 23, 24, 25, 26, 27]) # TWENTY
		mask.update([44, 45, 46, 47]) # PAST

	elif minute >= 15:
		mask.update([11]) # A
		mask.update([13, 14, 15, 16, 17, 18, 19]) # QUARTER
		mask.update([44, 45, 46, 47]) # PAST

	elif minute >= 10:
		mask.update([38, 39, 40]) # TEN
		mask.update([44, 45, 46, 47]) # PAST

	elif minute >= 5:
		mask.update([28, 29, 30, 31]) # FIVE
		mask.update([44, 45, 46, 47]) # PAST

	elif minute >= 0:
		mask.update([104, 105, 106, 107, 108, 109, 110]) # O'CLOCK
#}}}

	hour = hour % 12

#{{{ Hour masks
	if hour == 1:
		mask.update([55, 56, 57]) # ONE

	elif hour == 2:
		mask.update([74, 75, 76]) # TWO

	elif hour == 3:
		mask.update([61, 62, 63, 64, 65]) # THREE

	elif hour == 4:
		mask.update([66, 67, 68, 69]) # FOUR

	elif hour == 5:
		mask.update([70, 71, 72, 73]) # FIVE

	elif hour == 6:
		mask.update([58, 59, 60]) # SIX

	elif hour == 7:
		mask.update([88, 89, 90, 91, 92]) # SEVEN

	elif hour == 8:
		mask.update([77, 78, 79, 80, 81]) # EIGHT

	elif hour == 9:
		mask.update([51, 52, 53, 54]) # NINE

	elif hour in (10, 12+10):
		mask.update([99, 100, 101]) # TEN

	elif hour in (11, 12+11):
		mask.update([82, 83, 84, 85, 86, 87]) # ELEVEN

	elif hour == 0:
		mask.update([93, 94, 95, 96, 97, 98]) # TWELVE
#}}}

	return mask
#}}}


#{{{ Draw the clock
def draw_clock(screen, attrs=[]):

	time = datetime.now()

	color_on  = attrs[0] if len(attrs) >= 1 else color(2)
	color_off = attrs[1] if len(attrs) >= 2 else color(0)

	data = 'ITLISASTIMEACQUARTERDCTWENTYFIVEXHALFBTENFTOPASTERUNINEONESIXTHREEFOURFIVETWOEIGHTELEVENSEVENTWELVETENSEO\'CLOCK'

	mask = _build_mask(time)

	for i, letter in enumerate(data):
		if i in mask:
			color = color_on
		else:
			color = color_off

		x, y = (None, None)

		if i <= 104:
			x = i % 11 * 4
			y = i // 11 * 2
		elif i == 105:
			x = 21
			y = 18
		elif i > 105:
			x = (i - 106) * 4 + 24
			y = 18

		draw_str(screen, y, x, letter, color)
#}}}


#{{{ Draw everything
def draw(screen, attrs):
	rows, cols = screen.getmaxyx()

	if rows < 23 or cols < 47:
		screen.clear()
		return

	y = int(rows/2 - 23/2)
	x = int(cols/2 - 47/2)

	border = screen.derwin(23, 47, y, x)
	clock = border.derwin(19, 41, 2, 3)

	draw_clock(clock, attrs[0])
	draw_border(border, ['┃','┃','━','━','┏','┓','┗','┛'], attrs[1])

	border.noutrefresh()
	clock.noutrefresh()
	screen.refresh()
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


		event = screen.getch()

		if event == curses.ERR:
			pass
		elif event == ord('q'):
			break
		elif event == ord('r'):
			screen.clear()
		elif event == curses.KEY_RESIZE:
			screen.clear()

		redraw()
		sleep(0.25)

			# redraw()
			# render(screen, colors, now)

		# time = datetime.now()
		# screen.addstr(0, 0, str(time))

		# sleep(0.25)
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
