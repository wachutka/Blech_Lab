# Set of basic commands for the Blech Lab to run on the micropython board.
# pyb.rng()*(1.0/(2**30-1))
'''
Collection of functions for blech micropython board.
Here are your options:
calibrate(outport = 'Y1', opentime = 10)
clear_tastes(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 10000)

'''

import time
import pyb
import os

print('Type \'help(blech_basics)\' to get a list of available functions.')

# Valve calibration procedure

def calibrate(outport = 'Y1', opentime = 10):

	i = 1		# trial counter
	repeats = 5	# number of times to open valve
	iti = 2000	# time between valve openings
	out = pyb.Pin(outport, pyb.Pin.OUT_PP)	# set pin mode

	while i <= repeats:
		out.high()
		pyb.delay(opentime)
		out.low()
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

# Basic nose poke task with 1 poke

def basic_np(outport = 'Y2', opentime = 11, trials = 100, iti = [5000, 10000], resptime = [20000, 15000]):

	inport = 'X7'		# port connected to nose poke 1
	i = 1			# trial counter
	ii = 0		# lights makes sure that the lights turn on at the start of the first trial.
	nopoke = 0
	
	pyb.delay(5000)
	while i <= trials:
		if i <= (trials/2): # use diff times for the first half of the experiment
			time1 = pyb.millis()
			if i - ii >= 1.0:
				ii = i
				time2 = pyb.millis()
				pyb.Pin('X9', pyb.Pin.OUT_PP).high()
			if pyb.Pin(inport, pyb.Pin.IN).value() == 0: #or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
				pyb.Pin(outport, pyb.Pin.OUT_PP).high()
				pyb.delay(opentime)
				pyb.Pin(outport, pyb.Pin.OUT_PP).low()
				pyb.Pin('X9', pyb.Pin.OUT_PP).low()
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[0]:
					if pyb.Pin(inport, pyb.Pin.IN).value() == 0: # or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = curtime - starttime
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[0]))
				i +=1
			if (time1-time2) >= resptime[0]:
				#pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
				#pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
				pyb.Pin('X9', pyb.Pin.OUT_PP).low()
				pyb.delay(10000)
				nopoke +=1
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[0]:
					if pyb.Pin(inport, pyb.Pin.IN).value() == 0: # or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial had no poke.  There have been '+str(nopoke)+' no-poke trials thus far.')
				i +=1
				
		else:
			time1 = pyb.millis()
			if i - ii >= 1.0:
				ii = i
				time2 = pyb.millis()
				pyb.Pin('X9', pyb.Pin.OUT_PP).high()
			if pyb.Pin(inport, pyb.Pin.IN).value() == 0: #or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
				pyb.Pin(outport, pyb.Pin.OUT_PP).high()
				pyb.delay(opentime)
				pyb.Pin(outport, pyb.Pin.OUT_PP).low()
				pyb.Pin('X9', pyb.Pin.OUT_PP).low()
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[1]:
					if pyb.Pin(inport, pyb.Pin.IN).value() == 0: #or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = curtime - starttime
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[1]))
				i +=1
			if (time1-time2) >= resptime[1]:
				pyb.Pin('X9', pyb.Pin.OUT_PP).low()
				pyb.delay(10000)
				nopoke +=1
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[1]:
					if pyb.Pin(inport, pyb.Pin.IN).value() == 0: #or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial had no poke.  There have been '+str(nopoke)+' no-poke trials thus far.')
				i +=1

	print('Shrek says: It\'s all ogre now.')


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
			print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(trial_iti))
			i +=1
			
	print('Shrek says: It\'s all ogre now.')
	
def gng_train(outports = ['Y1', 'Y2', 'Y3', 'Y4'], opentimes = [13, 13, 13, 13], pokeport = 'X8', trials = 100, iti = [13000, 16000], outtime = [500,500], trialdur = 30000, training = 'go'):
    # training can be 'go', 'nogo', or 'gonogo'
	i = 1			# trial counter
	ii = 0
	nopoke = 0
    poke = 0
    correct = 0
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	t1 = pyb.Pin(outports[0], pyb.Pin.OUT_PP)
    t2 = pyb.Pin(outports[1], pyb.Pin.OUT_PP)
    t3 = pyb.Pin(outports[2], pyb.Pin.OUT_PP)
    t4 = pyb.Pin(outports[3], pyb.Pin.OUT_PP)
	poke = pyb.Pin(pokeport, pyb.Pin.IN, pyb.Pin.PULL_UP)
	pyb.delay(10000)
    
    if training == 'go':
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
    			t3.high()
    			pyb.delay(opentime[2])
    			t3.low()
    			time6 = pyb.millis()
    			time7 = pyb.millis()
                while (time6 - time7) < trialdur:
                    if poke.value() == 0:
                        t2.high()
                        pyb.delay(opentime[1])
                        t2.low()
                        correct += 1
                        break
        			time6 = pyb.millis()
                light.low()
    			poketime = pyb.millis()
    			curtime = poketime
    			rand = pyb.rng()*(1.0/(2**30-1))
    			trial_iti = math.floor(rand*(iti[2]-iti[1])+iti[1])
    			while (curtime-poketime) <= trial_iti:
    				if poke.value() == 0:
    					poketime = pyb.millis()
    				curtime = pyb.millis()
    			totaltime = time5 - time2
    			print('Trial '+str(i)+' of '+str(trials)+' completed. Last poke took '+str(totaltime)+'ms.  There have been '+str(correct)+' correct trials thus far.')
    			i +=1
                
    elif training == 'nogo':
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
    			t1.high()
    			pyb.delay(opentime[0])
    			t1.low()
    			time6 = pyb.millis()
    			time7 = pyb.millis()
                while (time6 - time7) < trialdur:
                    if poke.value() == 0:
                        poke = 1
                        light.low()
                        break
        			time6 = pyb.millis()
                if poke == 0:
                    t2.high()
                    pyb.delay(opentime[1])
                    t2.low()
                    correct += 1
                light.low()
    			poketime = pyb.millis()
    			curtime = poketime
    			rand = pyb.rng()*(1.0/(2**30-1))
    			trial_iti = math.floor(rand*(iti[2]-iti[1])+iti[1])
    			while (curtime-poketime) <= trial_iti:
    				if poke.value() == 0:
    					poketime = pyb.millis()
    				curtime = pyb.millis()
    			totaltime = time5 - time2
    			print('Trial '+str(i)+' of '+str(trials)+' completed. Last poke took '+str(totaltime)+'ms.  There have been '+str(correct)+' correct trials thus far.')
    			i +=1
                
    elif training == 'gonogo':
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
    			t1.high()
    			pyb.delay(opentime[0])
    			t1.low()
    			time6 = pyb.millis()
    			time7 = pyb.millis()
                while (time6 - time7) < trialdur:
                    if poke.value() == 0:
                        poke = 1
                        light.low()
                        break
        			time6 = pyb.millis()
                if poke == 0:
                    t2.high()
                    pyb.delay(opentime[1])
                    t2.low()
                    correct += 1
                light.low()
    			poketime = pyb.millis()
    			curtime = poketime
    			rand = pyb.rng()*(1.0/(2**30-1))
    			trial_iti = math.floor(rand*(iti[2]-iti[1])+iti[1])
    			while (curtime-poketime) <= trial_iti:
    				if poke.value() == 0:
    					poketime = pyb.millis()
    				curtime = pyb.millis()
    			totaltime = time5 - time2
    			print('Trial '+str(i)+' of '+str(trials)+' completed. Last poke took '+str(totaltime)+'ms.  There have been '+str(correct)+' correct trials thus far.')
    			i +=1
	print('Shrek says: It\'s all ogre now.')

