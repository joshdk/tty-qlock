// Copyright Josh Komoroske. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE.txt file.

package qlock

import (
	"time"

	"github.com/JoelOtter/termloop"
)

type clock struct {
	colorOn  termloop.Attr
	colorOff termloop.Attr
}

func New(colorOn, colorOff termloop.Attr) termloop.Drawable {
	return &clock{
		colorOn:  colorOn,
		colorOff: colorOff,
	}
}

func (*clock) Tick(termloop.Event) {}

func (c *clock) Draw(s *termloop.Screen) {
	// Get the current hour and minute.
	now := time.Now()
	hour, minute := now.Hour(), now.Minute()

	// Get the current screen size.
	screenWidth, screenHeight := s.Size()

	// Get the X "origin" for drawing all components relative to this offset.
	originX := (screenWidth - width) / 2
	if originX < 0 {
		originX = 0
	}

	// Get the Y "origin" for drawing all components relative to this offset.
	originY := (screenHeight - height) / 2
	if originY < 0 {
		originY = 0
	}

	// Get all the components that should be enabled.
	enabled := entries(hour, minute)

	// Loop over the list of all components...
	for entry := range all {
		if _, found := enabled[entry]; found {
			// If the component was one of the enabled ones, draw it with the
			// "on" color.
			t := termloop.NewText(originX+entry.x, originY+entry.y, entry.text, c.colorOn, termloop.ColorDefault)
			t.Draw(s)
		} else {
			// If the component was not one of the enabled ones, draw it with
			// the "off" color.
			t := termloop.NewText(originX+entry.x, originY+entry.y, entry.text, c.colorOff, termloop.ColorDefault)
			t.Draw(s)
		}
	}
}
