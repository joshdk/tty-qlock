// Copyright Josh Komoroske. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE.txt file.

package main

import (
	"flag"
	"fmt"
	"strings"

	"github.com/JoelOtter/termloop"
	"github.com/joshdk/tty-qlock/qlock"
)

// version contains the version string, replaced at build-time with ldflags.
var version = "development"

func main() {
	var offColorFlag string
	flag.StringVar(&offColorFlag, "off-color", "black", "color for disabled letters")

	var onColorFlag string
	flag.StringVar(&onColorFlag, "on-color", "blue", "color for enabled letters")

	var versionFlag bool
	flag.BoolVar(&versionFlag, "version", false, "print version and exit")

	flag.Parse()

	// If the -version flag was given, print the version and exit.
	if versionFlag {
		fmt.Println(version)
		return
	}

	game := termloop.NewGame()
	game.Screen().SetFps(5)
	game.Screen().AddEntity(qlock.New(
		color(onColorFlag),
		color(offColorFlag),
	))
	game.Start()
}

func color(spec string) (attr termloop.Attr) {
	if strings.HasSuffix(spec, "+bold") {
		attr = termloop.AttrBold
	}
	spec = strings.TrimSuffix(spec, "+bold")
	colors := map[string]termloop.Attr{
		"black":   termloop.ColorBlack,
		"red":     termloop.ColorRed,
		"green":   termloop.ColorGreen,
		"yellow":  termloop.ColorYellow,
		"blue":    termloop.ColorBlue,
		"magenta": termloop.ColorMagenta,
		"cyan":    termloop.ColorCyan,
		"white":   termloop.ColorWhite,
	}
	return colors[spec] | attr
}
