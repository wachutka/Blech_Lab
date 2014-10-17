# Clear tastes script for micropython board

import pyb

valves = ['Y1','Y2','Y3','Y4']		# I/O port where valve is connected
opentime = 10000		# valve open time in ms



for i in valves:
	v = pyb.Pin(valves[i], pyb.Pin.OUT_PP)
	v.high()

pyb.delay(opentime)

for i in valves:
	v = pyb.Pin(valves[i], pyb.Pin.OUT_PP)
	v.low()
	

