PORT=/dev/ttyUSB0

install:
	ampy -p $(PORT) put config.json
	ampy -p $(PORT) put boot.py
	ampy -p $(PORT) put main.py
shell:
	picocom $(PORT) -b115200
