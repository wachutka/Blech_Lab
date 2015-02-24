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
	
# Basic nose poke training procedure

def basic_np(outport = 'Y2', opentime = 13, pokeport = 'X8', trials = 100, iti = [1000, 2000,12000], outtime = [250,250]):
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

# Training for discrimination task
	
def discrim_train(outports = ['Y1', 'Y2', 'Y3', 'Y4'], opentimes = [13, 13, 13, 13], pokeports = ['X7', 'X8', 'X9'], trials = 100, iti = [13000, 16000], outtime = [500,500], trialdur = 30000, blocksize = 50, firstblock = 0):
    # training can be 'go', 'nogo', or 'gonogo'
	trial = 0			# trial counter
	nopoke = 0
    	pokecheck = 0
    	correct = 0
	lit = 0
	blockcount = firstblock - 1
	trialarray = []
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	t1 = pyb.Pin(outports[0], pyb.Pin.OUT_PP)
    	t2 = pyb.Pin(outports[1], pyb.Pin.OUT_PP)
    	t3 = pyb.Pin(outports[2], pyb.Pin.OUT_PP)
    	t4 = pyb.Pin(outports[3], pyb.Pin.OUT_PP)
	poke1 = pyb.Pin(pokeports[0], pyb.Pin.IN, pyb.Pin.PULL_UP)
	poke2 = pyb.Pin(pokeports[1], pyb.Pin.IN, pyb.Pin.PULL_UP)
	poke3 = pyb.Pin(pokeports[2], pyb.Pin.IN, pyb.Pin.PULL_UP)
	pokelight1 = pyb.Pin(LIGHTPORT, pyb.Pin.OUT_PP)
	pokelight2 = pyb.Pin(LIGHTPORT, pyb.Pin.OUT_PP)

	for i in range(trials):
		if i % blocksize == 0:
			blockcount += 1
		if blockcount % 2 == 0:
			trialarray.append(0)
		else:
			trialarray.append(1)

	print(trialarray)

	pyb.delay(10000)
    
        while trial <= trials:
        	time1 = pyb.millis()
		if lit == 0:
			lit = 1
			time2 = pyb.millis()
			light.high()
			pyb.delay(5)
            	if poke2.value() == 0:
    			time3 = pyb.millis()
    			time4 = pyb.millis()
			light.low()
    			while (time4 - time3) < outtime[0]:
    				if poke.value() == 0:
    					time3 = pyb.millis()
    				time4 = pyb.millis()
			pokelight1.high()
			pokelight2.high()
			if trialarray[trial] == 0:
    				t3.high()
    				pyb.delay(opentimes[2])
    				t3.low()
    				time6 = pyb.millis()
    				time7 = pyb.millis()
               			while (time6 - time7) < trialdur:
                    			if poke1.value() == 0:
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
    				time6 = pyb.millis()
    				time7 = pyb.millis()
               			while (time6 - time7) < trialdur:
                    			if poke3.value() == 0:
                        			t2.high()
                        			pyb.delay(opentimes[1])
                        			t2.low()
						time5 = pyb.millis()
                        			correct += 1
                        			break
        				time6 = pyb.millis()
			pokelight1.low()
			pokelight2.low()
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
			trial +=1
    			print('Trial '+str(trial)+' of '+str(trials)+' completed. Last decision took '+str(totaltime)+'ms.  There have been '+str(correct)+' correct trials thus far.')		
    
	print('Shrek says: It\'s all ogre now.')


