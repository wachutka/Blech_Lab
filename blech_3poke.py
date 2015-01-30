# Set of basic commands for the Blech Lab to run on the micropython board.
# pyb.rng()*(1.0/(2**30-1))
'''
Collection of functions for blech micropython board.
Here are your options:
calibrate(outport = 'Y1', opentime = 10)
clear_tastes(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], duration = 10000)
basic_np(outport = 'Y2', opentime = 11, trials = 100, iti = [500, 1000], resptime = [25000, 20000])
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
				
def passive_water(outport = 'Y2', opentime = 11, trials = 40, iti = 15000):
	i = 1	# trial counter
	while i <= trials:
		pyb.Pin(outport, pyb.Pin.OUT_PP).high()
		pyb.delay(opentime)
		pyb.Pin(outport, pyb.Pin.OUT_PP).low()
		i = i+1
		pyb.delay(iti)
	print('Shrek says: It\'s all ogre now.')


# Basic nose poke task with 1 pokes

def basic_np(outport = 'Y2', opentime = 11, pokeport = 'X8', trials = 100, iti = [2000, 4000], resptime = [25000, 20000], outtime = [150,200]):
	i = 1			# trial counter
	ii = 0
	nopoke = 0
	light = pyb.Pin('X9', pyb.Pin.OUT_PP)
	water = pyb.Pin(outport, pyb.Pin.OUT_PP)
	poke = pyb.Pin(pokeport, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
	pyb.delay(5000)
	while i <= trials:
		if i <= (trials/2):
			time1 = pyb.millis()
			if i - ii >= 1.0:
				ii = i
				time2 = pyb.millis()
				light.high()
			if poke.value() == 0:
				time3 = pyb.millis()
				time4 = pyb.millis()
				while (time4 - time3) < outtime[0]:
					if poke.value() == 0:
						time3 = pyb.millis()
					time4 = pyb.millis()
				water.high()
				pyb.delay(opentime)
				water.low()
				light.low()
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[0]:
					if poke.value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = curtime - starttime
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[0]))
				i +=1
			if (time1-time2) >= resptime[0]:
				light.low()
				pyb.delay(5000)
				nopoke +=1
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[0]:
					if poke.value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial had no poke.  There have been '+str(nopoke)+' no-poke trials thus far.')
				i +=1
				
		else:
			time1 = pyb.millis()
			if i - ii >= 1.0:
				ii = i
				time2 = pyb.millis()
				light.high()
			if poke.value() == 0:
				time3 = pyb.millis()
				time4 = pyb.millis()
				while (time4 - time3) < outtime[1]:
					if poke.value() == 0:
						time3 = pyb.millis()
					time4 = pyb.millis()
				water.high()
				pyb.delay(opentime)
				water.low()
				light.low()
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[1]:
					if poke.value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				totaltime = curtime - starttime
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial duration was '+str(totaltime)+'ms.  The iti was '+str(iti[1]))
				i +=1
			if (time1-time2) >= resptime[1]:
				light.low()
				pyb.delay(5000)
				nopoke +=1
				poketime = pyb.millis()		# get current time
				starttime = poketime
				curtime = poketime
				while (curtime-poketime) <= iti[1]:
					if poke.value() == 0:
						poketime = pyb.millis()
					curtime = pyb.millis()
				print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial had no poke.  There have been '+str(nopoke)+' no-poke trials thus far.')
				i +=1		
	print('Shrek says: It\'s all ogre now.')

# Blocked cue exposure

def cued_np(tastes = ['Y1','Y2','Y3', 'Y4'], pokes = ['X7', 'X8'], opentimes = [11, 11, 10, 10], trials = 100, iti = 13000, resptime = 14000):
	i = 0			# trial counter
	ii = -1			# trial start counter
	nopoke = 0		# counter for trials without pokes
	curtime = 0
	poketime = 0
	time1 = 0
	time2 = 0
	pyb.delay(10000)	# delay start of experiment

	while i <= (trials-1):
		time1 = pyb.millis()
		if i - ii >= 1.0:
			pyb.Pin('Y8', pyb.Pin.OUT_PP).high()			# play tone cue
			pyb.delay(500)
			pyb.Pin('Y8', pyb.Pin.OUT_PP).low()
			#if i < 50:
			#if i < 25 or (i >=50 and i < 75):
			if i < 10 or (i >=20 and i < 30) or (i >=40 and i < 50) or (i >=60 and i < 70) or (i >=80 and i < 90):	
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
			pyb.Pin('X9', pyb.Pin.OUT_PP).high()
			ii = i
			time2 = pyb.millis()
		#elif (i < 50) and pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0:
		elif (i < 25 or (i >=50 and i < 75)) and pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0:
		#elif (i < 10 or (i >=20 and i < 30) or (i >=40 and i < 50) or (i >=60 and i < 70) or (i >=80 and i < 90)) and pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			poketime = pyb.millis()		# get current time
			curtime = poketime
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			while (curtime-poketime) <= iti:
				if pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0 or pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			trialdur = poketime-time2
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. Latency to poke was '+str(trialdur)+'ms.')
		#elif (i < 50) and pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
		#elif (i < 25 or (i >=50 and i < 75)) and pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
		#elif (i < 10 or (i >=20 and i < 30) or (i >=40 and i < 50) or (i >=60 and i < 70) or (i >=80 and i < 90)) and pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
			#pyb.Pin(tastes[3], pyb.Pin.OUT_PP).high()
			#pyb.delay(opentimes[3])
			#pyb.Pin(tastes[3], pyb.Pin.OUT_PP).low()
			#poketime = pyb.millis()		# get current time
			#curtime = poketime
			#pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			#pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			#pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			#while (curtime-poketime) <= iti:
				#if pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0 or pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
					#poketime = pyb.millis()
				#curtime = pyb.millis()
			#trialdur = poketime-time2
			#i +=1
			#print('Trial '+str(i)+' of '+str(trials)+' completed. Latency to poke was '+str(trialdur)+'ms.')

		#elif (i >= 50) and pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
		elif ((i >= 25 and i < 50) or i >= 75) and pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
		#elif ((i >=10 and i < 20) or (i >=30 and i < 40) or (i >=50 and i < 60) or (i >=70 and i < 80) or i >= 90) and pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			poketime = pyb.millis()		# get current time
			curtime = poketime
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			while (curtime-poketime) <= iti:
				if pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0 or pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			trialdur = poketime-time2
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. Latency to poke was '+str(trialdur)+'ms.')
		#elif (i >= 50) and pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0:
		#elif ((i >= 25 and i < 50) or i >= 75) and pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0:
		#elif ((i >=10 and i < 20) or (i >=30 and i < 40) or (i >=50 and i < 60) or (i >=70 and i < 80) or i >= 90) and pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0:
			#pyb.Pin(tastes[3], pyb.Pin.OUT_PP).high()
			#pyb.delay(opentimes[3])
			#pyb.Pin(tastes[3], pyb.Pin.OUT_PP).low()
			#poketime = pyb.millis()		# get current time
			#curtime = poketime
			#pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			#pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			#pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			#while (curtime-poketime) <= iti:
				#if pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0 or pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
					#poketime = pyb.millis()
				#curtime = pyb.millis()
			#trialdur = poketime-time2
			#i +=1
			#print('Trial '+str(i)+' of '+str(trials)+' completed. Latency to poke was '+str(trialdur)+'ms.')

		elif (time1-time2) >= resptime:
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			pyb.delay(10000)
			nopoke += 1
			poketime = pyb.millis()		# get current time
			while (curtime-poketime) <= iti:
				if pyb.Pin(pokes[0], pyb.Pin.IN).value() == 0 or pyb.Pin(pokes[1], pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial had no poke. There have been '+str(nopoke)+' no-poke trials thus far.')

	print('Shrek says: It\'s all ogre now.')

# Random cued nose poke with punishment and reward tastes

def rand_np_pun(tastes = ['Y1','Y2','Y3','Y4'], opentimes = [11, 11, 10, 10], trials = 100, iti = 15000, resptime = 13000, file = 'JW06_122014'):
	inport_1 = 'X7'		# port connected to nose poke 1
	inport_2 = 'X8'		# port connected to nose poke 2
	correct1 = 0
	correctA = 0		# correct pokes counter
	correctB = 0		# correct pokes counter
	trialsA = 0
	trialsB = 0
	nopoke = 0
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
		time1 = pyb.millis()
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
			pyb.delay(3000)
			if trialarray[i] == 0:	
				pyb.Pin('Y6', pyb.Pin.OUT_PP).high()
			elif trialarray[i] == 1:
				pyb.Pin('Y7', pyb.Pin.OUT_PP).high()
			pyb.Pin('X9', pyb.Pin.OUT_PP).high()
			ii = i
			time2 = pyb.millis()

		elif trialarray[i] == 0 and pyb.Pin(inport_1, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			correct1 = 1
			correctA += 1
			trialsA += 1
			poketime = pyb.millis()		# get current time
			curtime = poketime
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correctA)+' of '+str(trialsA)+' CA trials correct.')
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			log.write(str(correct1)+'\n')
			

		elif trialarray[i] == 1 and pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[1])
			pyb.Pin(tastes[1], pyb.Pin.OUT_PP).low()
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			correct1 = 1
			correctB += 1
			trialsB += 1
			poketime = pyb.millis()		# get current time
			curtime = poketime
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correctB)+' of '+str(trialsB)+' NaCl trials correct.')
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			log.write(str(correct1)+'\n')

		elif trialarray[i] == 0 and pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[3], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[3])
			pyb.Pin(tastes[3], pyb.Pin.OUT_PP).low()
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			correct1 = 0
			trialsA += 1
			poketime = pyb.millis()		# get current time
			curtime = poketime
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correctA)+' of '+str(trialsA)+' CA trials correct.')
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			log.write(str(correct1)+'\n')
			
		elif trialarray[i] == 1 and pyb.Pin(inport_1, pyb.Pin.IN).value() == 0:
			pyb.Pin(tastes[3], pyb.Pin.OUT_PP).high()
			pyb.delay(opentimes[3])
			pyb.Pin(tastes[3], pyb.Pin.OUT_PP).low()
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			correct1 = 0
			trialsB += 1
			poketime = pyb.millis()		# get current time
			curtime = poketime
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. '+str(correctB)+' of '+str(trialsB)+' NaCl trials correct.')
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
			log.write(str(correct1)+'\n')

		elif (time1-time2) >= resptime:
			pyb.Pin('Y6', pyb.Pin.OUT_PP).low()
			pyb.Pin('Y7', pyb.Pin.OUT_PP).low()
			pyb.Pin('X9', pyb.Pin.OUT_PP).low()
			pyb.delay(10000)
			nopoke += 1
			poketime = pyb.millis()
			curtime = poketime		
			i +=1
			print('Trial '+str(i)+' of '+str(trials)+' completed. Last trial had no poke. There have been '+str(nopoke)+' no-poke trials thus far.')
			while (curtime-poketime) <= iti:
				if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0 or pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
					poketime = pyb.millis()
				curtime = pyb.millis()
	log.close()
	print('It\'s all ogre now.')

