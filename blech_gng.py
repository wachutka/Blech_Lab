# Set of basic commands for the Blech Lab to run on the micropython board.
# pyb.rng()*(1.0/(2**30-1))
'''
Collection of functions for blech micropython board.
Here are your options:
calibrate(outport = 'Y1', opentime = 10, repeats = 5)
clear_tastes(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 10000)
passive_water(outport = 'Y2', opentime = 11, trials = 40, iti = 15000)
basic_np(outport = 'Y2', opentime = 13, pokeport = 'X8', trials = 100, iti = [500, 2000,4000], outtime = [250,250])
basic_rand(outport = 'Y2', opentime = 13, pokeport = 'X8', trials = 100, iti = [1000, 2000,12000], outtime = [250,250])
gng_train(outports = ['Y1', 'Y2', 'Y3', 'Y4'], opentimes = [13, 13, 13, 13], pokeport = 'X8', trials = 100, iti = [13000, 16000], outtime = [500,500], trialdur = 30000, training = 'go')

'''

import time
import pyb
import os
import math

print('Type \'help(blech_basics)\' to get a list of available functions.')

# Valve calibration procedure

def calibrate(outport = 'Y1', opentime = 10, repeats = 5):

	i = 1		# trial counter
	iti = 2000	# time between valve openings
	out = pyb.Pin(outport, pyb.Pin.OUT_PP)	# set pin mode

	while i <= repeats:
		out.high()
		pyb.delay(opentime)
		out.low()
		pyb.delay(iti)
		i = i+1
	print('It\'s all ogre now.')

# Clear out tastant lines.  For filling lines, use setup = 1 to also purge air bubbles from lines.

def clear_tastes(outports = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 5000):
	repeats = 25
	opentime = 15
	for i in outports:
		pyb.Pin(i, pyb.Pin.OUT_PP).high()
	pyb.delay(duration)
	for i in outports:
		pyb.Pin(i, pyb.Pin.OUT_PP).low()
	print('The purge is complete.  This has been the most sucessful purge yet.')

# Water passive habituation
				
def passive_water(outport = 'Y2', opentime = 11, trials = 40, iti = 15000):
	pyb.delay(10000)  # start delay
	i = 1	# trial counter
	while i <= trials:
		pyb.Pin(outport, pyb.Pin.OUT_PP).high()
		pyb.delay(opentime)
		pyb.Pin(outport, pyb.Pin.OUT_PP).low()
		print('Trial '+str(i)+' of '+str(trials)+' completed.')
		i = i+1
		pyb.delay(iti)
	print('Shrek says: It\'s all ogre now.')

# Basic nose poke task with 1 pokes

def basic_np(outport = 'Y2', opentime = 13, pokeport = 'X8', trials = 100, iti = [500, 2000,4000], outtime = [250,250]):
	i = 1			# trial counter
	ii = 0
	nopoke = 0
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	water = pyb.Pin(outport, pyb.Pin.OUT_PP)
	poke = pyb.Pin(pokeport, pyb.Pin.IN, pyb.Pin.PULL_UP)
	pyb.delay(10000)
	while i <= trials:
		if i <= 5:
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
				while (curtime-poketime) <= iti[0]:
					if poke.value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = time5 - time2
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[0]))
				i +=1
				
		elif i <= (trials/2):
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
				while (curtime-poketime) <= iti[1]:
					if poke.value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = time5 - time2
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[1]))
				i +=1
			
		else:
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
				while (time4 - time3) < outtime[1]:
					if poke.value() == 0:
						time3 = pyb.millis()
					time4 = pyb.millis()
				water.high()
				pyb.delay(opentime)
				water.low()
				light.low()
				poketime = pyb.millis()		# get current time
				curtime = poketime
				while (curtime-poketime) <= iti[2]:
					if poke.value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = time5 - time2
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[2]))
				i +=1
			
	print('Shrek says: It\'s all ogre now.')

# Basic nose poke random time with 1 pokes

def basic_rand(outport = 'Y2', opentime = 13, pokeport = 'X8', trials = 100, iti = [1000, 2000,12000], outtime = [250,250]):
	i = 1			# trial counter
	ii = 0
	nopoke = 0
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	light.low()
	water = pyb.Pin(outport, pyb.Pin.OUT_PP)
	poke = pyb.Pin(pokeport, pyb.Pin.IN, pyb.Pin.PULL_UP)
	pyb.delay(10000)
	while i <= trials:
		if i <= 5:
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
				while (curtime-poketime) <= iti[0]:
					if poke.value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = time5 - time2
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[0]))
				i +=1
				
		elif i <= (trials):
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
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(trial_iti))
				i +=1
			
	print('Shrek says: It\'s all ogre now.')
	
# Training for go-no-go tasks
	
def gng_train(outports = ['Y1', 'Y2', 'Y3', 'Y4'], opentimes = [14, 14, 13, 12], pokeport = 'X8', trials = 120, iti = [14000, 16000], outtime = [500,500], trialdur = [5000, 5000], training = 'gonogo', blocksize = 10, firstblock = 0):
    # training can be 'go', 'nogo', or 'gonogo'
	trial = 0
	dur = trialdur[0]			
	nopoke = 0
    	pokecheck = 0
    	correct = 0
	lit = 0
	blockcount = firstblock-1
	trialarray = []
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	light.low()
	t1 = pyb.Pin(outports[0], pyb.Pin.OUT_PP)
    	t2 = pyb.Pin(outports[1], pyb.Pin.OUT_PP)
    	t3 = pyb.Pin(outports[2], pyb.Pin.OUT_PP)
    	t4 = pyb.Pin(outports[3], pyb.Pin.OUT_PP)
	poke = pyb.Pin(pokeport, pyb.Pin.IN, pyb.Pin.PULL_UP)
	pokelight = pyb.Pin('Y6', pyb.Pin.OUT_PP)

	if training == 'go':
		for i in range(trials):
			trialarray.append(0)

	elif training == 'nogo':
		for i in range(trials):
			trialarray.append(1)

	if training == 'gonogo':
		for i in range(trials):
			if i % blocksize == 0:
				blockcount += 1
			if blockcount % 2 == 0:
				trialarray.append(0)
			else:
				trialarray.append(1)

	print(trialarray)

	pyb.delay(10000)
    
        while trial < trials:
        	time1 = pyb.millis()
		if trial >= (trials/2):
			dur = trialdur[1]
		if lit == 0:
			lit = 1
			time2 = pyb.millis()
			light.high()
			pyb.delay(5)
            	if poke.value() == 0:
    			time3 = pyb.millis()
    			time4 = pyb.millis()
    			while (time4 - time3) < outtime[0]:
    				if poke.value() == 0:
    					time3 = pyb.millis()
    				time4 = pyb.millis()
			if trialarray[trial] == 0:
    				t3.high()
    				pyb.delay(opentimes[2])
    				t3.low()
				light.low()
    				time6 = pyb.millis()
    				time7 = pyb.millis()
				pokelight.high()
               			while (time6 - time7) < dur:
                    			if poke.value() == 0:
                        			t2.high()
                        			pyb.delay(opentimes[1])
                        			t2.low()
						time5 = pyb.millis()
                        			correct += 1
                        			break
        				time6 = pyb.millis()
			elif trialarray[trial] == 1:
    				t1.high()
    				pyb.delay(opentimes[0])
    				t1.low()
				light.low()
    				time6 = pyb.millis()
    				time7 = pyb.millis()
				#pokelight.high()
               			while (time6 - time7) < dur:
                    			if poke.value() == 0:
                        			pokecheck = 1
						t4.high()
						pyb.delay(opentimes[3])
						t4.low()
						time5 = pyb.millis()
						break
        				time6 = pyb.millis()
               			if pokecheck == 0:
                    			t2.high()
                    			pyb.delay(opentimes[1])
                    			t2.low()
                    			correct += 1
					time5 = time7
			pokelight.low()
			lit = 0
			pokecheck = 0
    			poketime = pyb.millis()
    			curtime = poketime
    			rand = pyb.rng()*(1.0/(2**30-1))
    			trial_iti = math.floor(rand*(iti[1]-iti[0])+iti[0])
    			while (curtime-poketime) <= trial_iti:
    				if poke.value() == 0:
    					poketime = pyb.millis()
    				curtime = pyb.millis()
    			totaltime = time5 - time7
			totaltime = max(0, totaltime)
			trial +=1
    			print('Trial '+str(trial)+' of '+str(trials)+' completed. Last poke took '+str(totaltime)+'ms.  There have been '+str(correct)+' correct trials thus far.')		
    
	print('Shrek says: It\'s all ogre now.')

