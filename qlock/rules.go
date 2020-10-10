// Copyright Josh Komoroske. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE.md file.

package qlock

func entries(hour int, minute int) map[entry]struct{} {
	items := []entry{
		it, is,
	}

	switch minute - minute%5 {
	case 55:
		items = append(items, fiveOff, to)
	case 50:
		items = append(items, tenOff, to)
	case 45:
		items = append(items, a, quarter, to)
	case 40:
		items = append(items, twenty, to)
	case 35:
		items = append(items, twenty, fiveOff, to)
	case 30:
		items = append(items, half, past)
	case 25:
		items = append(items, twenty, fiveOff, past)
	case 20:
		items = append(items, twenty, past)
	case 15:
		items = append(items, a, quarter, past)
	case 10:
		items = append(items, tenOff, past)
	case 5:
		items = append(items, fiveOff, past)
	case 0:
		items = append(items, oclock)
	}

	switch minute % 5 {
	case 1:
		items = append(items, dotOne)
	case 2:
		items = append(items, dotOne, dotTwo)
	case 3:
		items = append(items, dotOne, dotTwo, dotThree)
	case 4:
		items = append(items, dotOne, dotTwo, dotThree, dotFour)
	}

	if minute >= 35 {
		items = append(items, hours[(hour+1)%12])
	} else {
		items = append(items, hours[hour%12])
	}

	set := make(map[entry]struct{}, len(items))
	for _, item := range items {
		set[item] = struct{}{}
	}
	return set
}
