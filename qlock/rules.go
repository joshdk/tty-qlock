// Copyright Josh Komoroske. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE.txt file.

package qlock

type entry struct {
	Text   string
	Active bool
}

func e(text string, active bool) entry {
	return entry{Text: text, Active: active}
}

func activate(board [][]entry, row, index int) {
	board[row][index].Active = true
}

func quickAbs(value int) int {
	return value * ((value*2 + 1) % 2)
}

func entries(hour int, minute int, ampm bool) [][]entry {
	board := [][]entry{
		{e(it, true), e(f1, false), e(is, true), e(f2, false), e(am, false), e(pm, false)},
		{e(a, false), e(f3, false), e(quarter, false), e(f4, false)},
		{e(twenty, false), e(five, false), e(f5, false)},
		{e(half, false), e(f6, false), e(ten, false), e(f7, false), e(to, false)},
		{e(past, false), e(f8, false), e(nine, false)},
		{e(one, false), e(six, false), e(three, false)},
		{e(four, false), e(five, false), e(two, false)},
		{e(eight, false), e(eleven, false)},
		{e(seven, false), e(twelve, false)},
		{e(ten, false), e(f9, false), e(oClock, false)},
	}

	minSection := minute - minute%5

	if ampm {
		if hour < 12 {
			activate(board, 0, 4)
		} else {
			activate(board, 0, 5)
		}
	}

	if minSection > 30 {
		// Set: to.
		activate(board, 3, 4)
	} else if minSection == 0 {
		activate(board, 9, 2)
	} else {
		// Set: past.
		activate(board, 4, 0)
	}

	switch quickAbs(minSection - 30) {
	case 25:
		activate(board, 2, 1)
	case 20:
		activate(board, 3, 2)
	case 15:
		activate(board, 1, 0)
		activate(board, 1, 2)
	case 10:
		activate(board, 2, 0)
	case 5:
		activate(board, 2, 0)
		activate(board, 2, 1)
	case 0:
		if minSection == 30 {
			activate(board, 3, 0)
		}
	}

	var target string

	if minute >= 35 {
		target = hours[(hour+1)%12]
	} else {
		target = hours[hour%12]
	}

outer:
	for idx := 5; idx < len(board); idx++ {
		for jdx := 0; jdx < len(board[idx]); jdx++ {
			if board[idx][jdx].Text == target {
				board[idx][jdx].Active = true

				break outer
			}
		}
	}

	_ = target

	return board
}
