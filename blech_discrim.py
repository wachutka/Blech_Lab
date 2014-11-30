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

# Water passive habituation
				
def passive_water(outport = 'Y2', opentime = 13, trials = 50, iti = 15000):

	i = 1	# trial counter
	out = pyb.Pin(outport, pyb.Pin.OUT_PP)	# set pin mode

	while i <= trials:
		pyb.Pin('Y8', pyb.Pin.OUT_PP).high()			# play tone cue
		pyb.delay(500)
		pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
		out.high()
		pyb.delay(opentime)
		out.low()
		i = i+1
		pyb.delay(iti)
	print('Shrek says: It\'s all ogre now.')
		
# Basic nose poke task with 2 pokes

def basic_np(outport = 'Y2', opentime = 13, trials = 100, iti = [8000, 12000], resptime = [14000, 11000], file = 'JW07_113014'):

	inport_1 = 'X7'		# port connected to nose poke 1
	inport_2 = 'X8'		# port connected to nose poke 2
	i = 1			# trial counter
	ii = 0
	nopoke = 0
	log = open('/sd/'+file+'.out', 'w')	# open log file on upython SD card

	pyb.delay(5000)
	while i <= trials:
		if i <= (trials/2):
			time1 = pyb.millis()
			if i - ii >= 1.0:
				ii = i
				time2 = pyb.millis()
				pyb.Pin('Y6', pyb.Pin.OUT_PP).high()
				pyb.Pin('Y7', pyb.Pin.OUT_PP).high()
			if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
				pyb.Pin(outport, pyb.Pin.OUT_PP).high()
				pyb.delay(opentime)
				pyb.Pin(outport, pyb.Pin.OUT_PP).low()
				pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
				pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[0]:
					if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = curtime - starttime
				log.write(str(totaltime)+'\n')
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[0]))
				i +=1
			if (time1-time2) >= resptime[0]:
				pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
				pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
				pyb.delay(10000)
				nopoke +=1
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[0]:
					if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial had no poke.  There have been '+str(nopoke)+' no-poke trials thus far.')
				i +=1
				
		else:
			time1 = pyb.millis()
			if i - ii >= 1.0:
				ii = i
				time2 = pyb.millis()
				pyb.Pin('Y6', pyb.Pin.OUT_PP).high()
				pyb.Pin('Y7', pyb.Pin.OUT_PP).high()
			if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
				pyb.Pin(outport, pyb.Pin.OUT_PP).high()
				pyb.delay(opentime)
				pyb.Pin(outport, pyb.Pin.OUT_PP).low()
				pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
				pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[1]:
					if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = curtime - starttime
				log.write(str(totaltime)+'\n')
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[1]))
				i +=1
			if (time1-time2) >= resptime[1]:
				pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
				pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
				pyb.delay(10000)
				nopoke +=1
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[1]:
					if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial had no poke.  There have been '+str(nopoke)+' no-poke trials thus far.')
				i +=1
	
	log.close()		
	print('Shrek says: It\'s all ogre now.')

# Blocked cue exposure

def cued_np(tastes = ['Y1','Y2','Y3'], opentimes = [12, 13, 10], trials = 100, iti = 13000, resptime = 15000):
	inport_1 = 'X7'		# port connected to nose poke 1
	inport_2 = 'X8'		# port connected to nose poke 2
	i = 0			# trial counter
	ii = -1			# trial start counter
	pyb.delay(10000)	# delay start of experiment

	while i <= (trials-1):
		time1 = pyb.millis()
		if i - ii >= 1.0:
			pyb.Pin('Y8', pyb.Pin.OUT_PP).high()			# play tone cue
			pyb.delay(500)
			pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
			if i < (trials/2):					# give passive taste cue	
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[0])
				pyb.Pin(tastes[0], pyb.Pin.OUT_PP).low()
			else:
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).high()
				pyb.delay(opentimes[2])
				pyb.Pin(tastes[2], pyb.Pin.OUT_PP).low()
			pyb.delay(3000)
			pyb.Pin('Y6', pyb.Pin.OUT_PP).high()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).high()
			ii = i
			time2 = pyb.millis()

		elif i < (trials/2) and pyb.Pin(inport_1, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			poketime = pyb.millis()		# get current time
			curtime = poketime
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. Errors last trial = '+str(errors))

		elif i >= (trials/2) and pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			poketime = pyb.millis()		# get current time
			curtime = poketime
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. Errors last trial = '+str(errors))

		elif (time1-time2) >= resptime:
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			pyb.delay(10000)
			nopoke +=1
			poketime = pyb.millis()		# get current time
			starttime = poketime
			curtime = poketime
			while (curtime-poketime) <= iti[0]:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial had no poke.  There have been '+str(nopoke)+' no-poke trials thus far.')
			i +=1

	print('Shrek says: It\'s all ogre now.')

# Random cued nose poke with punishment and reward tastes

def rand_np_pun(tastes = ['Y1','Y2','Y3','Y4'], opentimes = [13, 23, 10, 10], trials = 100, iti = 13000, file = 'JW05_111814'):
	inport_1 = 'X7'		# port connected to nose poke 1
	inport_2 = 'X8'		# port connected to nose poke 2
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
		
	print(trialarray)

	i = 0			# trial counter
	ii = -1			# trial start counter
	pyb.delay(10000)	# delay first trial
	
	while i <= (trials-1):
		if i - ii >= 1.0:
			pyb.Pin('Y8', pyb.Pin.OUT_PP).high()			# play tone cue
			pyb.delay(500)
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
			correct +=1
			correct1 = 1
			poketime = pyb.millis()		# get current time
			curtime = poketime
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			log.write(str(correct1)+'\n')
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correct)+' correct.')

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
			log.write(str(correct1)+'\n')
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correct)+' correct.')


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
			log.write(str(correct1)+'\n')
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correct)+' correct.')


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
			log.write(str(correct1)+'\n')
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correct)+' correct.')

	log.close()
	print('It\'s all ogre now.')

