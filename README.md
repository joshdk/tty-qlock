[![Actions][github-actions-badge]][github-actions-link]
[![License][license-badge]][license-link]
[![Go Report Card][go-report-badge]][go-report-link]
[![Releases][github-release-badge]][github-release-link]

# Qlock

A minimal, curses-based clock, for your terminal. Inspired by the [QlockTwo by Biegert&Funk](https://qlocktwo.com/us/ "QlockTwo by Biegert&Funk").

![qlock screenshot](images/screenshot.jpg "qlock screenshot")

## Installing

### Release binary

Prebuilt binaries can be found on the [releases page][github-release-link]. Download the archive for your computer's architecture, extract the binary, and put it inside your `$PATH`.

```bash
$ wget -q https://github.com/joshdk/tty-qlock/releases/download/v1.0.0/qlock-linux-amd64.tar.gz
$ tar -xf qlock-linux-amd64.tar.gz
$ sudo install qlock /usr/bin/qlock
```

You can then launch qlock by running:

```
$ qlock -help
```

### From source

Alternatively, you can build it yourself by cloning the repo, and then running:

```bash
$ make build
```

You can then launch qlock by running:

```
$ ./dist/qlock -help
```

## Usage

### Help!

You can pass the `-help` flag to display the help text:

```
$ qlock -help
Usage of qlock:
  -off-color string
        color for disabled letters (default "black")
  -on-color string
        color for enabled letters (default "blue")
  -version
        print version and exit
```

### Colors

You can pass the `-on-color` and `-off-color` flags to control the color of the enabled and disabled UI elements respectively.

Both flags can take any of the 8 standard color names (`black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, or `white`).

Additionally, a `+bold` suffix can be added to use the bold color variant (like `-color-on green+bold`).

## Bug Reporting

If you encounter an issue, [please report it](https://github.com/joshdk/tty-qlock/issues/new)!

When reporting, please include:

- A screenshot of your terminal (drag an image into the issue description box to attach it).
- Any interaction workflow details (resizing/dragging/clicking/etc).
- Your system's architecture (like `linux`/`amd64`).

Thank you!

## License

This code is distributed under the [BSD 3-Clause License][license-link], see [LICENSE.txt][license-file] for more information.

[github-actions-badge]:  https://github.com/joshdk/tty-qlock/workflows/Build/badge.svg
[github-actions-link]:   https://github.com/joshdk/tty-qlock/actions
[github-release-badge]:  https://img.shields.io/github/release/joshdk/tty-qlock/all.svg
[github-release-link]:   https://github.com/joshdk/tty-qlock/releases
[go-report-badge]:  https://goreportcard.com/badge/github.com/joshdk/tty-qlock
[go-report-link]:   https://goreportcard.com/report/github.com/joshdk/tty-qlock
[license-badge]:    https://img.shields.io/badge/license-BSD-green.svg
[license-file]:     https://github.com/joshdk/tty-qlock/blob/master/LICENSE.txt
[license-link]:     https://opensource.org/licenses/BSD-3-Clause
