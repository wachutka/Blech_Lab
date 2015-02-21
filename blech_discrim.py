# Set of functions for the Blech Lab to run on the micropython board.
'''
Collection of functions for blech micropython board.  
Here are your options:
calibrate(outport = 'Y2', opentime = 13, repeats = 5)
clear_tastes(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 10000)
passive_water(outport = 'Y2', opentime = 13, trials = 50, iti = 15000)
basic_rand(outport = 'Y2', opentime = 13, pokeport = 'X8', trials = 100, iti = [1000, 2000,12000], outtime = [250,250])

'''
import time
import pyb
import os

print('Type \'help(blech_basics)\' to get a list of available functions.')

# Valve calibration procedure

def calibrate(outport = 'Y2', opentime = 13, repeats = 5):
	iti = 2000	# time between valve openings
	out = pyb.Pin(outport, pyb.Pin.OUT_PP)	# set pin mode
	for i in range(repeats)
		out.high()
		pyb.delay(opentime)
		out.low()
		pyb.delay(iti)
	print('It\'s all ogre now.')

# Clear out tastants

def clear_tastes(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 10000):
	for i in tastes:
		pyb.Pin(i, pyb.Pin.OUT_PP).high()
	pyb.delay(duration)
	for i in tastes:
		pyb.Pin(i, pyb.Pin.OUT_PP).low()
	print('The purge is complete.  This has been the most sucessful purge yet.')
	
# Water passive habituation
				
def passive_water(outport = 'Y2', opentime = 13, trials = 50, iti = 15000):
	out = pyb.Pin(outport, pyb.Pin.OUT_PP)	# set pin mode
	for i in range(trials):
		out.high()
		pyb.delay(opentime)
		out.low()
		pyb.delay(iti)
		print('Trial '+str(i+1)+' of '+str(trials)+' completed.')
	print('Shrek says: It\'s all ogre now.')
	
# Basic nose poke training procedure

def basic_rand(outport = 'Y2', opentime = 13, pokeport = 'X8', trials = 100, iti = [1000, 2000,12000], outtime = [250,250]):
	i = 1			# trial counter
	ii = 0
	nopoke = 0
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	water = pyb.Pin(outport, pyb.Pin.OUT_PP)
	poke = pyb.Pin(pokeport, pyb.Pin.IN, pyb.Pin.PULL_UP)
	pyb.delay(10000)
	while i <= trials:
		time1 = pyb.millis()
		if i - ii >= 1.0:
			ii = i
			time2 = pyb.millis()
			light.high()
			pyb.delay(5)
		if poke.value() == 0:
			time3 = pyb.millis()
			time4 = pyb.millis()
			time5 = pyb.millis()
			while (time4 - time3) < outtime[0]:
				if poke.value() == 0:
					time3 = pyb.millis()
				time4 = pyb.millis()
			water.high()
			pyb.delay(opentime)
			water.low()
			light.low()
			poketime = pyb.millis()		# get current time
			curtime = poketime
			rand = pyb.rng()*(1.0/(2**30-1))
			trial_iti = math.floor(rand*(iti[2]-iti[1])+iti[1])
			while (curtime-poketime) <= trial_iti:
				if poke.value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			totaltime = time5 - time2
			print('Trial '+str(i)+' of '+str(trials)+' completed. Last poke took '+str(totaltime)+'ms.  The iti was '+str(trial_iti))
			i +=1
			
	print('Shrek says: It\'s all ogre now.')
