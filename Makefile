SOURCE="./src/qlock.py"
TARGET="/usr/bin/tty-qlock"


all: install

install:
	install -m 755 $(SOURCE) $(TARGET)

uninstall:
	rm $(TARGET)
