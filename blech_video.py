'''
This code is for shaping behavior using manual input prior to video recording of oro-facial behaviors.
'''

import pyb
import os

# Valve calibration procedure

def calibrate(outport = 'Y2', opentime = 10):

	i = 1		# trial counter
	repeats = 5	# number of times to open valve
	iti = 2000	# time between valve openings

	while i <= repeats:
		pyb.Pin(outport, pyb.Pin.OUT_PP).high()
		pyb.delay(opentime)
		pyb.Pin(outport, pyb.Pin.OUT_PP).low()
		pyb.delay(iti)
		i = i+1
	print('It\'s all ogre now.')

# Clear out tastants

def clear_tastes(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 10000):
	for i in tastes:
		pyb.Pin(i, pyb.Pin.OUT_PP).high()
	pyb.delay(duration)
	for i in tastes:
		pyb.Pin(i, pyb.Pin.OUT_PP).low()
	print('The purge is complete.  This has been the most sucessful purge yet.')

# This is for manual shaping of behavior.

def shape(maxtrials = 100, outport = 'Y2', opentime = 12)
	i = 0
	inport = 'X6'
	while i < maxtrials:
		if pyb.Pin(inport, pyb.Pin.IN).value() == 0:
			pyb.Pin(outport, pyb.Pin.OUT_PP).high()
			pyb.delay(opentime)
			pyb.Pin(outport, pyb.Pin.OUT_PP).low()
			pyb.delay(500)
			i += 1
			print(str(i)+' rewards given.')

# Water passive habituation
				
def passive_water(outport = 'Y2', opentime = 12, trials = 50, iti = 15000):
	i = 1	# trial counter
	while i <= trials:
		pyb.Pin(outport, pyb.Pin.OUT_PP).high()
		pyb.delay(opentime)
		pyb.Pin(outport, pyb.Pin.OUT_PP).low()
		i = i+1
		pyb.delay(iti)
	print('Shrek says: It\'s all ogre now.')

