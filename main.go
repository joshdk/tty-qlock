// Copyright Josh Komoroske. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE.txt file.

package main

import (
	"github.com/JoelOtter/termloop"
	"github.com/joshdk/tty-qlock/qlock"
)

func main() {
	game := termloop.NewGame()
	game.Screen().SetFps(5)
	game.Screen().AddEntity(qlock.New(termloop.ColorBlue, termloop.ColorBlack))
	game.Start()
}
