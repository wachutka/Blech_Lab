# Discrimination task for Blech Lab

import time
from math import floor
import random
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

# Clear tastant lines
def clearout(outports = [31, 33, 35, 37], dur = 5):

	GPIO.setmode(GPIO.BOARD)
	for i in outports:
		GPIO.setup(i, GPIO.OUT)

	for i in outports:
		GPIO.output(i, 1)
	time.sleep(dur)
	for i in outports:
		GPIO.output(i, 0)

	print('Tastant line clearing complete.')

# Calibrate tastant lines
def calibrate(outports = [31, 33, 35, 37], opentime = 0.015, repeats = 5):

	GPIO.setmode(GPIO.BOARD)
	for i in outports:
		GPIO.setup(i, GPIO.OUT)

	for rep in range(repeats):
		for i in outports:
			GPIO.output(i, 1)
		time.sleep(opentime)
		for i in outports:
			GPIO.output(i, 0)
		time.sleep(2)

	print('Calibration procedure complete.')

# Passive H2O deliveries
def passive(outport = 31, opentime = 0.015, iti = 15, trials = 100):

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(outport, GPIO.OUT)

	time.sleep(10)
	
	for trial in range(trials):
		GPIO.output(outport, 1)
		time.sleep(opentime)
		GPIO.output(outport, 0)
		print('Trial '+str(trial+1)+' of '+str(trials)+' completed.')
		time.sleep(iti)

	print('Passive deliveries completed')

# Basic nose poking procedure for H2O rewards
def basic_np(outport = 31, opentime = 0.011, iti = [0.4, 1, 1.5], trials = 120, outtime = 0.15):

	GPIO.setmode(GPIO.BOARD)
	trial = 1
	inport = 13
	pokelight = 38
	houselight = 18
	lights = 0
	GPIO.setup(pokelight, GPIO.OUT)
	GPIO.setup(houselight, GPIO.OUT)
	GPIO.setup(inport, GPIO.IN)
	GPIO.setup(outport, GPIO.OUT)
	
	time.sleep(5)

	while trial <= trials:
		if lights == 0:
			GPIO.output(pokelight, 1)
			GPIO.output(houselight, 1)
			lights = 1

# Check for pokes
		if GPIO.input(inport) == 0:
			poketime = time.time()
			curtime = poketime

# Make rat remove nose from nose poke to receive reward
			while (curtime - poketime) <= outtime:
				if GPIO.input(inport) == 0:
					poketime = time.time()
				curtime = time.time()

# Passive delivery
			GPIO.output(outport, 1)
			time.sleep(opentime)
			GPIO.output(outport, 0)
			GPIO.output(pokelight, 0)
			GPIO.output(houselight, 0)
			print('Trial '+str(trial)+' of '+str(trials)+' completed.')
			trial += 1
			lights = 0

# Calculate and execute ITI delay.  Pokes during ITI reset ITI timer.
			if trial <= trials/2:
				delay = floor((random.random()*(iti[1]-iti[0]))*100)/100+iti[0]
			else:
				delay = floor((random.random()*(iti[2]-iti[0]))*100)/100+iti[0]
			poketime = time.time()
			curtime = poketime

			while (curtime - poketime) <= delay:
				if GPIO.input(inport) == 0:
					poketime = time.time()
				curtime = time.time()

		
	print('Basic nose poking has been completed.')

# Discrimination task training procedure
def disc_train(outports = [31, 33, 35], opentimes = [0.0105, 0.0125, 0.0105], iti = [10, 12, 14], trials = 120, blocksize = 20, plswitch = 120):

	GPIO.setmode(GPIO.BOARD)
	blocked = 0			# blocked = 1 for blocked, 0 for random
	outtime = 0.25
	trial = 0
	bothpl = 0			# bothpl = 1 for both lights, 0 for cue light only
	blcounter = 1
	lights = 0
	trialdur = 10			# trial duration (rat must respond within this time or trial is counted as no-poke)
	tarray = []

	cacorrect = 0
	naclcorrect = 0
	catrials = 0
	nacltrials = 0
	nopoke = 0
	poke = 0
	

	inports = [11, 13, 15]
	pokelights = [36, 38, 40]
	houselight = 18
	
	for i in outports:
		GPIO.setup(i, GPIO.OUT)
	for i in inports:
		GPIO.setup(i, GPIO.IN, GPIO.PUD_UP)
	for i in pokelights:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, 0)
	GPIO.setup(houselight, GPIO.OUT)
	GPIO.output(houselight, 0)

	time.sleep(10)

	if blocked == 1:
		for i in range(trials):
			if i % blocksize == 0:
				blcounter += 1
			if blcounter % 2 == 0:
				tarray.append(0)
			else:
				tarray.append(1)		
	else:
		for i in range(trials):
			if i % 2 == 0:
				tarray.append(0)
			else:
				tarray.append(1)
		random.shuffle(tarray)

	print(tarray)
	time.sleep(10)

	while trial < trials:
		if lights == 0:
			GPIO.output(houselight, 1)
			GPIO.output(pokelights[1], 1)
			if trial > plswitch:
				bothpl = 1
			if tarray[trial] == 0:
				print('This trial will be CA(R)')
			else:
				print('This trial will be NaCl(L)')
			lights = 1	

# Check for pokes
		if GPIO.input(inports[1]) == 0:
			poketime = time.time()
			curtime = poketime

# Make rat remove nose from nose poke to receive reward
			while (curtime - poketime) <= outtime:
				if GPIO.input(inports[1]) == 0:
					poketime = time.time()
				curtime = time.time()
			
# Deliver cue taste and manipulate cue lights (depends on setting for bothpl)
			if tarray[trial] == 0:
				catrials += 1
				GPIO.output(outports[0], 1)
				time.sleep(opentimes[0])
				GPIO.output(outports[0], 0)
				GPIO.output(pokelights[1], 0)
				GPIO.output(houselight, 0)
				if bothpl == 0:
					GPIO.output(pokelights[0], 1)
				else:
					GPIO.output(pokelights[0], 1)
					GPIO.output(pokelights[2], 1)
# Wait for response poke and provide reward or timeout punishment
				timestart = time.time()
				curtime = timestart
				while (curtime - timestart) <= trialdur:
					if GPIO.input(inports[0]) == 0:
						GPIO.output(outports[1], 1)
						time.sleep(opentimes[1])
						GPIO.output(outports[1], 0)
						GPIO.output(pokelights[0], 0)
						GPIO.output(pokelights[2], 0)
						poke = 1
						cacorrect += 1
						break
					elif GPIO.input(inports[2]) == 0:
						poke = 1
						GPIO.output(pokelights[0], 0)
						GPIO.output(pokelights[2], 0)
						break
					curtime = time.time()
# Deliver cue taste and manipulate cue lights (depends on setting for bothpl)	
			else:
				nacltrials += 1
				GPIO.output(outports[2], 1)
				time.sleep(opentimes[2])
				GPIO.output(outports[2], 0)
				GPIO.output(pokelights[1], 0)
				GPIO.output(houselight, 0)
				if bothpl == 0:
					GPIO.output(pokelights[2], 1)
				else:
					GPIO.output(pokelights[0], 1)
					GPIO.output(pokelights[2], 1)
# Wait for response poke and provide reward or timeout punishment
				timestart = time.time()
				curtime = timestart
				while (curtime - timestart) <= trialdur:
					if GPIO.input(inports[2]) == 0:
						GPIO.output(outports[1], 1)
						time.sleep(opentimes[1])
						GPIO.output(outports[1], 0)
						GPIO.output(pokelights[0], 0)
						GPIO.output(pokelights[2], 0)
						poke = 1
						naclcorrect += 1
						break
					elif GPIO.input(inports[0]) == 0:
						poke = 1
						GPIO.output(pokelights[0], 0)
						GPIO.output(pokelights[2], 0)
						break
					curtime = time.time()
			totalcorrect = cacorrect + naclcorrect
			trial += 1
			if poke == 0:
				nopoke += 1
				GPIO.output(pokelights[0], 0)
				GPIO.output(pokelights[2], 0)
				print('Last trial had no poke. '+str(trial)+' of '+str(trials)+' completed. '+str(totalcorrect)+' correct trials thus far.')
				time.sleep(5)
			else:
				print(str(trial)+' of '+str(trials)+' completed. '+str(totalcorrect)+' correct trials thus far.')
			
			poke = 0
			lights = 0

# Calculate and execute ITI delay.  Pokes during ITI reset ITI timer.
			if trial <= trials/2:
				delay = floor((random.random()*(iti[1]-iti[0]))*100)/100+iti[0]
			else:
				delay = floor((random.random()*(iti[2]-iti[0]))*100)/100+iti[0]
			poketime = time.time()
			curtime = poketime
			while (curtime - poketime) <= delay:
				if GPIO.input(inports[1]) == 0:
					poketime = time.time()
				curtime = time.time()

	print('Discrimination task is complete! Stats: '+str(cacorrect)+'/'+str(catrials)+' CA trials correct, '+str(naclcorrect)+'/'+str(nacltrials)+' NaCl trials correct, and '+str(nopoke)+' no poke trials.')

