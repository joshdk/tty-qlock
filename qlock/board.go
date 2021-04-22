// Copyright Josh Komoroske. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE.txt file.

package qlock

const (
	it     = "IT"
	is     = "IS"
	a      = "A"
	to     = "TO"
	past   = "PAST"
	oClock = "O'CLOCK"

	quarter = "QUARTER"
	twenty  = "TWENTY"
	half    = "HALF"
	am      = "AM"
	pm      = "PM"

	one    = "ONE"
	two    = "TWO"
	three  = "THREE"
	four   = "FOUR"
	five   = "FIVE"
	six    = "SIX"
	seven  = "SEVEN"
	eight  = "EIGHT"
	nine   = "NINE"
	ten    = "TEN"
	eleven = "ELEVEN"
	twelve = "TWELVE"

	dot = "●"
	f1  = "L"
	f2  = "AS"
	f3  = "C"
	f4  = "DC"
	f5  = "X"
	f6  = "S"
	f7  = "F"
	f8  = "ERU"
	f9  = "SE"

	width         = 40
	height        = 20
	compactWidth  = 20
	compactHeight = 11
)

var (
	hours = []string{
		twelve,
		one,
		two,
		three,
		four,
		five,
		six,
		seven,
		eight,
		nine,
		ten,
		eleven,
	}
)
