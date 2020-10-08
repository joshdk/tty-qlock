// Copyright Josh Komoroske. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE.md file.

package qlock

type entry struct {
	x    int
	y    int
	text string
}

var (
	width  = 44
	height = 20

	it     = entry{2, 1, "I   T"}
	is     = entry{14, 1, "I   S"}
	a      = entry{2, 3, "A"}
	to     = entry{38, 7, "T   O"}
	past   = entry{2, 9, "P   A   S   T"}
	oclock = entry{22, 19, "O'  C   L   O   C   K"}

	fiveOff = entry{26, 5, "F   I   V   E"}
	tenOff  = entry{22, 7, "T   E   N"}
	quarter = entry{10, 3, "Q   U   A   R   T   E   R"}
	twenty  = entry{2, 5, "T   W   E   N   T   Y"}
	half    = entry{2, 7, "H   A   L   F"}

	one        = entry{2, 11, "O   N   E"}
	two        = entry{34, 13, "T   W   O"}
	three      = entry{26, 11, "T   H   R   E   E"}
	four       = entry{2, 13, "F   O   U   R"}
	fiveSecond = entry{18, 13, "F   I   V   E"}
	six        = entry{14, 11, "S   I   X"}
	seven      = entry{2, 17, "S   E   V   E   N"}
	eight      = entry{2, 15, "E   I   G   H   T"}
	nine       = entry{30, 9, "N   I   N   E"}
	tenSecond  = entry{2, 19, "T   E   N"}
	eleven     = entry{22, 15, "E   L   E   V   E   N"}
	twelve     = entry{22, 17, "T   W   E   L   V   E"}

	dotOne   = entry{0, 0, "●"}
	dotTwo   = entry{44, 0, "●"}
	dotThree = entry{44, 20, "●"}
	dotFour  = entry{0, 20, "●"}

	all = map[entry]struct{}{
		it:         {},
		is:         {},
		a:          {},
		to:         {},
		quarter:    {},
		half:       {},
		oclock:     {},
		past:       {},
		one:        {},
		two:        {},
		three:      {},
		four:       {},
		fiveOff:    {},
		fiveSecond: {},
		six:        {},
		seven:      {},
		eight:      {},
		nine:       {},
		tenOff:     {},
		tenSecond:  {},
		eleven:     {},
		twelve:     {},
		twenty:     {},

		dotOne:   {},
		dotTwo:   {},
		dotThree: {},
		dotFour:  {},

		{10, 1, "L"}:                     {},
		{22, 1, "A   S   A   M   P   M"}: {},
		{6, 3, "C"}:                      {},
		{38, 3, "D   C"}:                 {},
		{42, 5, "X"}:                     {},
		{18, 7, "S"}:                     {},
		{34, 7, "F"}:                     {},
		{18, 9, "E   R   U"}:             {},
		{14, 19, "S   E"}:                {},
	}

	hours = []entry{
		twelve,
		one,
		two,
		three,
		four,
		fiveSecond,
		six,
		seven,
		eight,
		nine,
		tenSecond,
		eleven,
	}
)
