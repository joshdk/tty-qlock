// Copyright Josh Komoroske. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE.txt file.

package qlock

import (
	"strings"
	"time"

	"github.com/JoelOtter/termloop"
)

type clock struct {
	colorOn  termloop.Attr
	colorOff termloop.Attr
	compact  bool
	showAMPM bool
}

func New(colorOn, colorOff termloop.Attr, compact, ampm bool) termloop.Drawable {
	return &clock{
		colorOn:  colorOn,
		colorOff: colorOff,
		compact:  compact,
		showAMPM: ampm,
	}
}

func (c *clock) width() int {
	if c.compact {
		return compactWidth
	}

	return width
}

func (c *clock) height() int {
	if c.compact {
		return compactHeight
	}

	return height
}

func (*clock) Tick(termloop.Event) {}

func (c *clock) Draw(s *termloop.Screen) {
	// Get the current hour and minute.
	now := time.Now()
	hour, minute := now.Hour(), now.Minute()

	// Get the current screen size.
	screenWidth, screenHeight := s.Size()

	// Get the X "origin" for drawing all components relative to this offset.
	originX := (screenWidth - c.width()) / 2
	if originX < 0 {
		originX = 0
	}

	// Get the Y "origin" for drawing all components relative to this offset.
	originY := (screenHeight - c.height()) / 2
	if originY < 0 {
		originY = 0
	}

	board := entries(hour, minute, c.showAMPM)

	minuteMarker := minute % 5

	for idx := 1; idx < 5; idx++ {
		state := c.colorOff
		if idx <= minuteMarker {
			state = c.colorOn
		}
		termloop.NewText(
			originX+idx*(4*c.offsetMultiplier()),
			originY,
			dot,
			state,
			termloop.ColorDefault,
		).Draw(s)
	}

	for idx, row := range board {
		x := 0
		for _, item := range row {
			state := c.colorOff
			if item.Active {
				state = c.colorOn
			}

			text := c.text(item.Text)

			termloop.NewText(
				originX+x,
				originY+(idx*c.offsetMultiplier()) + 1,
				text,
				state,
				termloop.ColorDefault,
			).Draw(s)

			x += len(text) + c.offsetX()
		}
	}
}

func (c *clock) offsetX() int {
	if c.compact {
		return 1
	}

	return 3
}

func (c *clock) offsetMultiplier() int {
	if c.compact {
		return 1
	}

	return 2
}

func (c *clock) text(str string) string {
	if c.compact {
		str = strings.Join(strings.Split(str, ""), " ")
		str = strings.Replace(str, " ' ", "'", 1)
	} else {
		str = strings.Join(strings.Split(str, ""), "   ")
		str = strings.Replace(str, "   '   ", "'  ", 1)
	}

	return str
}
