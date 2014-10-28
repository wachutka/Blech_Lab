# Set of basic commands for the Blech Lab to run on the micropython board.
# pyb.rng()*(1.0/(2**30-1))

import pyb

print('Type options() to get a list of available functions.')

# Print available functions

def options():
	print('Here are your options; choose wisely.')
	pyb.delay(500)
	print('calibrate(outport = \'Y1\', opentime = 10)')
	print('clear_tastes(outport_1 = \'Y1\', outport_2 = \'Y2\', outport_3 = \'Y3\', outport_4 = \'Y4\', duration = 10000)')
	print('basic_np(outport_1 = \'Y1\', outport_2 = \'Y2\', opentime_1 = 10, opentime_2 = 10, trials = 10, iti = 3000)')
	print('passive_water(tasteport_1 = \'Y1\', opentime_1 = 100, trials = 5, iti = 2000)')
	print('Or, for a sweet disco party, disco(repeats = 20, duration = 75)')
	
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

def basic_np(outport_1 = 'Y1', outport_2 = 'Y2', opentime_1 = 10, opentime_2 = 10, trials = 5, iti = 3000):

	inport_1 = 'Y9'		# port connected to nose poke 1
	inport_2 = 'Y10'	# port connected to nose poke 2
	i = 1			# trial counter

	while i <= trials:
		if pyb.Pin(inport_1, pyb.Pin.IN).value() == 0:
			pyb.Pin(outport_1, pyb.Pin.OUT_PP).high()
			pyb.delay(opentime_1)
			pyb.Pin(outport_1, pyb.Pin.OUT_PP).low()
			print('Trial ' i ' of ' trials ' completed.')
			i = i+1
			pyb.delay(iti)
		if pyb.Pin(inport_2, pyb.Pin.IN).value() == 0:
			pyb.Pin(outport_2, pyb.Pin.OUT_PP).high()
			pyb.delay(opentime_2)
			pyb.Pin(outport_2, pyb.Pin.OUT_PP).low()
			print('Trial ' i ' of ' trials ' completed.')
			i = i+1
			pyb.delay(iti)
	print('It\'s all ogre now.')

# Water passive habituation
				
def passive_water(outport_1 = 'Y1', opentime_1 = 100, trials = 5, iti = 2000):

	i = 1	# trial counter
	out_1 = pyb.Pin(outport_1, pyb.Pin.OUT_PP)	# set pin mode

	while i <= trials:
		out_1.high()
		pyb.delay(opentime_1)
		out_1.low()
		i = i+1
		pyb.delay(iti)
	print('It\'s all ogre now.')

def passive_random(tastes = ['Y1', 'Y2', 'Y3', 'Y4'], opentimes = [10, 1000, 10, 1000], repeats = 5, iti = 5000):

	total = len(tastes)*repeats	# total number of trials

	trials = []

	# create array of trials
	for i in range(total):	
		trials.append(i%len(tastes))	

	# randomize trials array
	for i in range(total-1):	# total-1 so that the last position does not get randomized
		rand = pyb.rng()*(1.0/(2**30-1))	
		if rand > (1.0/len(tastes)):
			rand_switch = pyb.rng()*(1.0/(2**30-1))
			rand_switch = int(rand_switch*(total-i-2))+1	# random number between 1 remaining trials 
			trials[i], trials[i+rand_switch] = trials[i+rand_switch], trials[i]	# swap values

	print(trials)

	counter = 1
	for i in trials:
		pyb.Pin(tastes[i], pyb.Pin.OUT_PP).high()
		pyb.delay(opentimes[i])
		pyb.Pin(tastes[i], pyb.Pin.OUT_PP).low()
		pyb.delay(iti)
		print(str(counter)+' trials of '+str(total)+' completed.')
		counter += 1


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
