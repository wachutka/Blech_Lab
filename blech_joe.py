# Set of basic commands for the Blech Lab to run on the micropython board.
# pyb.rng()*(1.0/(2**30-1))
'''
Collection of functions for blech micropython board.
Here are your options:
calibrate(outport = 'Y1', opentime = 10)
clear_tastes(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 10000)
passive_water(outport_1 = 'Y1', opentime_1 = 100, trials = 5, iti = 2000)
passive_random(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], opentimes = [10, 1000, 10, 1000], repeats = 5, iti = 5000)
basic_np(outport_1 = 'Y1', outport_2 = 'Y2', opentime_1 = 10, opentime_2 = 10, trials = 5, iti = 3000)
alt_np(tastes = ['Y2','Y2'], opentimes = [10, 10], trials = 100, iti = 15000)
alt_np_pun(tastes = ['Y2','Y4'], opentimes = [10, 10], trials = 100, iti = 15000)
disco(repeats = 20, duration = 75)
'''


import time
import pyb
import os

print('Type \'help(blech_basics)\' to get a list of available functions.')

# Valve calibration procedure

def calibrate(outport = 'Y1', opentime = 10):

	i = 1		# trial counter
	repeats = 5	# number of times to open valve
	iti = 1000	# time between valve openings
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

		
# Basic nose poke task with 2 pokes

def basic_np(outport_1 = 'Y2', outport_2 = 'Y2', opentime_1 = 10, opentime_2 = 10, trials = 120, iti = [14000, 16000], file = 'JW05_110614'):

	inport_1 = 'X7'		# port connected to nose poke 1
	inport_2 = 'X8'		# port connected to nose poke 2
	i = 0			# trial counter
	ii = -1
	log = open('/sd/'+file+'.out', 'w')	# open log file on upython SD card

	while i <= trials:
		if i <= (trials/2):
			if i - ii >= 1.0:
				pyb.Pin('Y8', pyb.Pin.OUT_PP).high()			# play tone cue
				pyb.delay(300)
				pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
			if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
				pyb.Pin(outport_1, pyb.Pin.OUT_PP).high()
				pyb.delay(opentime_1)
				pyb.Pin(outport_1, pyb.Pin.OUT_PP).low()
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[0]:
					if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = curtime - starttime
				log.write(str(totaltime)+'\n')
				i +=1
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[0]))

		else:
			if i - ii >= 1.0:
				pyb.Pin('Y8', pyb.Pin.OUT_PP).high()			# play tone cue
				pyb.delay(300)
				pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
			if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
				pyb.Pin(outport_1, pyb.Pin.OUT_PP).high()
				pyb.delay(opentime_1)
				pyb.Pin(outport_1, pyb.Pin.OUT_PP).low()
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[1]:
					if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = curtime - starttime
				log.write(str(totaltime)+'\n')
				i +=1
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[1]))
	
	log.close()		
	print('It\'s all ogre now.')

# Random cued nose poke

def rand_np(tastes = ['Y1','Y2','Y3','Y4'], opentimes = [11, 10, 10, 9], trials = 120, iti = 15000, file = 'JW05_110614'):
	inport_1 = 'X7'		# port connected to nose poke 1
	inport_2 = 'X8'		# port connected to nose poke 2
	log = open('/sd/'+file+'.out', 'w')	# open log file on upython SD card
	trialarray = []
	for i in range(trials):
		trialarray.append(i%2)

	# randomize trials array
	for i in range(trials-1):	# total-1 so that the last position does not get randomized
		rand = pyb.rng()*(1.0/(2**30-1))	
		if rand >= (0.5):
			rand_switch = pyb.rng()*(1.0/(2**30-1))
			rand_switch = int(rand_switch*(trials-i-2))+1		# random number between 1 remaining trials 
			trialarray[i], trialarray[i+rand_switch] = trialarray[i+rand_switch], trialarray[i]	# swap values
		
	print(trialarray)
	i = 0			# trial counter
	ii = -1			# trial start counter
	errors = 0		# error tracker
	pyb.delay(10000)	# delay start of experiment

	while i <= (trials-1):
		if i - ii >= 1.0:
			pyb.Pin('Y8', pyb.Pin.OUT_PP).high()			# play tone cue
			pyb.delay(300)
			pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
			if trialarray[i] == 0:					# give passive taste cue	
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[0])
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).low()
			elif trialarray[i] == 1:
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[2])
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).low()
			ii = i

		elif trialarray[i] == 0 and pyb.Pin(inport_1, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			poketime = pyb.millis()		# get current time
			curtime = poketime
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			log.write(str(errors)+'\n')
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. Errors last trial = '+str(errors))
			errors = 0

		elif trialarray[i] == 1 and pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			poketime = pyb.millis()		# get current time
			curtime = poketime
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			log.write(str(errors)+'\n')
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. Errors last trial = '+str(errors))
			errors = 0

		elif trialarray[i] == 0 and pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
			errors +=1
			pyb.delay(500)

		elif trialarray[i] == 1 and pyb.Pin(inport_1, pyb.Pin.IN).value() == 0:
			errors +=1
			pyb.delay(500)

	log.close()
	print('It\'s all ogre now.')

# Random cued nose poke with punishment and reward tastes

def rand_np_pun(tastes = ['Y1','Y2','Y3','Y4'], opentimes = [11, 10, 10, 9], trials = 100, iti = 15000, file = 'JW05_110414'):
	inport_1 = 'X7'		# port connected to nose poke 1
	inport_2 = 'X8'		# port connected to nose poke 2
	i = 1			# trial counter
	correct = 0		# correct pokes counter
	log = open('/sd/'+file+'.out', 'w')	# open log file on upython SD card
	trialarray = []
	for i in range(trials):
		trialarray.append(i%2)
		
	# randomize trials array
	for i in range(trials-1):	# total-1 so that the last position does not get randomized
		rand = pyb.rng()*(1.0/(2**30-1))	
		if rand >= (0.5):
			rand_switch = pyb.rng()*(1.0/(2**30-1))
			rand_switch = int(rand_switch*(trials-i-2))+1		# random number between 1 remaining trials 
			trialarray[i], trialarray[i+rand_switch] = trialarray[i+rand_switch], trialarray[i]	# swap values

	while i <= trials:

		if trialarray[i] == 0 and pyb.Pin(inport_1, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			correct +=1
			correct1 = 1
			poketime = pyb.millis()		# get current time
			curtime = poketime
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			pyb.Pin('Y8', pyb.Pin.OUT_PP).high()
			pyb.delay(300)
			pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
			if trialarray[i+1] == 0:
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[0])
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).low()
			elif trialarray[i+1] == 1:
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[2])
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).low()
			log.write(str(correct1)+'\n')
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correct)+' correct.')
			i +=1

		elif trialarray[i] == 1 and pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			correct +=1
			correct1 = 1
			poketime = pyb.millis()		# get current time
			curtime = poketime
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			pyb.Pin('Y8', pyb.Pin.OUT_PP).high()
			pyb.delay(300)
			pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
			if trialarray[i+1] == 0:
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[0])
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).low()
			elif trialarray[i+1] == 1:
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[2])
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).low()
			log.write(str(correct1)+'\n')
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correct)+' correct.')
			i +=1

		elif trialarray[i] == 0 and pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[3], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[3])
			pyb.Pin(tastes[3], pyb.Pin.OUT_PP).low()
			correct1 = 0
			poketime = pyb.millis()		# get current time
			curtime = poketime
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			pyb.Pin('Y8', pyb.Pin.OUT_PP).high()
			pyb.delay(300)
			pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
			if trialarray[i+1] == 0:
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[0])
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).low()
			elif trialarray[i+1] == 1:
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[2])
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).low()
			log.write(str(correct1)+'\n')
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correct)+' correct.')
			i +=1

		elif trialarray[i] == 1 and pyb.Pin(inport_1, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[3], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[3])
			pyb.Pin(tastes[3], pyb.Pin.OUT_PP).low()
			correct1 = 0
			poketime = pyb.millis()		# get current time
			curtime = poketime
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			pyb.Pin('Y8', pyb.Pin.OUT_PP).high()
			pyb.delay(300)
			pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
			if trialarray[i+1] == 0:
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[0])
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).low()
			elif trialarray[i+1] == 1:
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[2])
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).low()
			log.write(str(correct1)+'\n')
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correct)+' correct.')
			i +=1

	log.close()
	print('It\'s all ogre now.')

# Disco party time

def disco(repeats = 20, duration = 75):
	i = 1
	while i <= repeats:
		pyb.LED(1).on()
		pyb.delay(duration)
		pyb.LED(1).off()
		pyb.LED(2).on()
		pyb.delay(duration)
		pyb.LED(2).off()
		pyb.LED(3).on()
		pyb.delay(duration)
		pyb.LED(3).off()
		pyb.LED(4).on()
		pyb.delay(duration)
		pyb.LED(4).off()
		i = i+1
