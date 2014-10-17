# Tastant calibration for micropython board

import pyb

valve = 'Y1'		# I/O port where valve is connected
trials = 5		# number of repeats
opentime = 10		# valve open time in ms
iti = 1000		# iti in ms

v = pyb.Pin(valve, pyb.Pin.OUT_PP)

for i in range(trials):
	v.high()
	pyb.delay(opentime)
	v.low()
	pyb.delay(iti)

