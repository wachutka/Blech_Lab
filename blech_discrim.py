# Set of functions for the Blech Lab to run on the micropython board.
'''
Collection of functions for blech micropython board.  
Here are your options:
calibrate(outport = 'Y2', opentime = 13, repeats = 5)
clear_tastes(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 10000)
passive_water(outport = 'Y2', opentime = 13, trials = 50, iti = 15000)
basic_np(outport = 'Y2', opentime = 13, pokeport = 'X8', trials = 100, iti = [1000, 2000,12000], outtime = [250,250])

'''
import time
import pyb
import os
import math

print('Type \'help(blech_basics)\' to get a list of available functions.')

# Valve calibration procedure

def calibrate(outports = ['Y1', 'Y2', 'Y3', 'Y4'], opentime = 15, repeats = 20):
	iti = 2000	
	for i in range(repeats):
		for j in outports:
			pyb.Pin(j, pyb.Pin.OUT_PP).high()
			pyb.delay(opentime)
			pyb.Pin(j, pyb.Pin.OUT_PP).low()
		pyb.delay(iti)
	print('It\'s all ogre now.')

# Clear out tastant lines.  For filling lines, use setup = 1 to also purge air bubbles from lines.

def clear_tastes(outports = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 5000):
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	light.low()
	repeats = 25
	opentime = 15
	for i in outports:
		pyb.Pin(i, pyb.Pin.OUT_PP).high()
	pyb.delay(duration)
	for i in outports:
		pyb.Pin(i, pyb.Pin.OUT_PP).low()
	print('The purge is complete.  This has been the most sucessful purge yet.')
		
# Water passive habituation
				
def passive_water(outport = 'Y2', opentime = 13, trials = 50, iti = 15000):
	pyb.delay(10000) 
	i = 1	
	while i <= trials:
		pyb.Pin(outport, pyb.Pin.OUT_PP).high()
		pyb.delay(opentime)
		pyb.Pin(outport, pyb.Pin.OUT_PP).low()
		print('Trial '+str(i)+' of '+str(trials)+' completed.')
		i = i+1
		pyb.delay(iti)
	print('Shrek says: It\'s all ogre now.')
	
# Basic nose poke training procedure

def basic_np(outport = 'Y2', opentime = 13, pokeport = 'X8', trials = 100, iti = [3500, 7000, 9000], outtime = [250,250]):
	i = 1			
	ii = 0
	nopoke = 0
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	light.low()
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
			poketime = pyb.millis()		
			curtime = poketime
			rand = pyb.rng()*(1.0/(2**30-1))
			if i <= (trials/2):
				trial_iti = math.floor(rand*(iti[1]-iti[0])+iti[0])
			else:
				trial_iti = math.floor(rand*(iti[2]-iti[0])+iti[0])
			while (curtime-poketime) <= trial_iti:
				if poke.value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			totaltime = time5 - time2
			print('Trial '+str(i)+' of '+str(trials)+' completed. Last poke took '+str(totaltime)+'ms.  The iti was '+str(trial_iti))
			i +=1
			
	print('Shrek says: It\'s all ogre now.')

# Training for discrimination task
	
def discrim_train(outports = ['Y1', 'Y2', 'Y3', 'Y4'], opentimes = [13, 14, 13, 11], pokeports = ['X7', 'X8', 'X3'], trials = 120, iti = [14000, 16000], outtime = [250,250], trialdur = 10000, blocksize = 1, firstblock = 0, training = 'random', plswitch = 90):
# training can be 'blocked', 'both', or 'random'
# bothpl sets both pokelights on.  f set to 0 only the cued pokelight will light.
	trial = 0			
	nopoke = 0
    	pokecheck = 0
	bothpl = 0
    	correct = 0
    	pokelight = ['Y6', 'Y7']
	lit = 0
	blockcount = firstblock - 1
	trialarray = []
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	light.low()
	t1 = pyb.Pin(outports[0], pyb.Pin.OUT_PP)
    	t2 = pyb.Pin(outports[1], pyb.Pin.OUT_PP)
    	t3 = pyb.Pin(outports[2], pyb.Pin.OUT_PP)
    	t4 = pyb.Pin(outports[3], pyb.Pin.OUT_PP)
	poke1 = pyb.Pin(pokeports[0], pyb.Pin.IN, pyb.Pin.PULL_UP)
	poke2 = pyb.Pin(pokeports[1], pyb.Pin.IN, pyb.Pin.PULL_UP)
	poke3 = pyb.Pin(pokeports[2], pyb.Pin.IN, pyb.Pin.PULL_UP)
	pokelight1 = pyb.Pin(pokelight[0], pyb.Pin.OUT_PP)
	pokelight3 = pyb.Pin(pokelight[1], pyb.Pin.OUT_PP)
	
	if training == 'blocked':
		for i in range(trials):
			if i % blocksize == 0:
				blockcount += 1
			if blockcount % 2 == 0:
				trialarray.append(0)
			else:
				trialarray.append(1)
	elif training == 'both':
		for i in range(trials):
			trialarray.append(2)
	elif training == 'random':
		blocksize = 1
		for i in range(trials):
			if i % 2 == 0:
				trialarray.append(0)
			else:
				trialarray.append(1)
			# randomize trials array
		for i in range(trials-1):	# total-1 so that the last position does not get randomized
			rand = pyb.rng()*(1.0/(2**30-1))	
			if rand >= (0.5):
				rand_switch = pyb.rng()*(1.0/(2**30-1))
				rand_switch = int(rand_switch*(trials-i-2))+1		 
				trialarray[i], trialarray[i+rand_switch] = trialarray[i+rand_switch], trialarray[i]	

	print(trialarray)

	pyb.delay(10000)
    
        while trial < trials:
		if trialarray[trial] == 0 and lit < 1:
			print('This trial will be NaCl (L)')
    		elif lit < 1:
			print('This trial will be CA (R)')
		if trial >= plswitch:
			bothpl = 1
        	time1 = pyb.millis()
		if lit < 1:
			lit = 1
			light.high()
			pyb.delay(5)
            	elif poke2.value() == 0:
    			time3 = pyb.millis()
    			time4 = pyb.millis()
    			while (time4 - time3) < outtime[0]:
    				if poke2.value() == 0:
    					time3 = pyb.millis()
    				time4 = pyb.millis()
			light.low()
			if trialarray[trial] == 0:
    				t3.high()
    				pyb.delay(opentimes[2])
    				t3.low()
    				time6 = pyb.millis()
    				time7 = pyb.millis()

				if bothpl == 0:
					pokelight1.high()
				else:
					pokelight1.high()
					pokelight3.high()
               			while (time6 - time7) < trialdur:
                    			if poke1.value() == 0:
                        			t2.high()
                        			pyb.delay(opentimes[1])
                        			t2.low()
						time5 = pyb.millis()
                        			correct += 1
						pokecheck = 1
                        			break
					elif poke3.value() == 0:
						time5 - pyb.millis()
						break
					else:
						time5 = time7
					time6 = pyb.millis()
			elif trialarray[trial] == 1:
    				t1.high()
    				pyb.delay(opentimes[0])
    				t1.low()
    				time6 = pyb.millis()
    				time7 = pyb.millis()

				if bothpl == 0:
					pokelight3.high()
				else:
					pokelight1.high()
					pokelight3.high()
               			while (time6 - time7) < trialdur:
                    			if poke3.value() == 0:
                        			t2.high()
                        			pyb.delay(opentimes[1])
                        			t2.low()
						time5 = pyb.millis()
                        			correct += 1
						pokecheck = 1
                        			break
					elif poke1.value() == 0:
						time5 = pyb.millis()
						break
					else:
						time5 = time7
        				time6 = pyb.millis()
			elif trialarray[trial] == 2:
    				t2.high()
    				pyb.delay(opentimes[1])
    				t2.low()
    				time6 = pyb.millis()
    				time7 = pyb.millis()
				pokelight1.high()
				pokelight3.high()
               			while (time6 - time7) < trialdur:
                    			if poke1.value() == 0 or poke3.value() == 0:
                        			t2.high()
                        			pyb.delay(opentimes[1])
                        			t2.low()
						time5 = pyb.millis()
                        			correct += 1
						pokecheck = 1
                        			break
        				time6 = pyb.millis()
			pokelight1.low()
			pokelight3.low()
			lit = 0
			if pokecheck == 0:
				pyb.delay(10000)
			pokecheck = 0
			totaltime = time5 - time7
			totaltime = max(0, totaltime)
			trial +=1

    			print('Trial '+str(trial)+' of '+str(trials)+' completed. Last decision took '+str(totaltime)+'ms.  There have been '+str(correct)+' correct trials thus far.')

			poketime = pyb.millis()
    			curtime = poketime
    			rand = pyb.rng()*(1.0/(2**30-1))
			trial_iti = math.floor(rand*(iti[1]-iti[0])+iti[0])
    			while (curtime-poketime) <= trial_iti:
    				if poke1.value() == 0 or poke2.value() == 0 or poke3.value() == 0:
    					poketime = pyb.millis()
    				curtime = pyb.millis()
			
	print('Shrek says: It\'s all ogre now.')


