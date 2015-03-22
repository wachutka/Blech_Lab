# Discrimination task for Blech Lab

import time
from math import floor
from random import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Clear tastant lines
def clearout(outports = [31, 33, 35, 37], dur = 5):
	for i in outports:
		GPIO.setup(i, GPIO.OUT)

	for i in outports:
		GPIO.output(i, 1)
	time.sleep(dur)
	for i in outports:
		GPIO.output(i, 0)

	GPIO.cleanup()
	print('Tastant line clearing complete.')

# Calibrate tastant lines
def calibrate(outports = [31, 33, 35, 37], opentime = 0.015, repeats = 5):
	for i in outports:
		GPIO.setup(i, GPIO.OUT)

	for rep in range(repeats):
		for i in outports:
			GPIO.output(i, 1)
		time.sleep(opentime)
		for i in outports:
			GPIO.output(i, 0)

	GPIO.cleanup()
	print('Calibration procedure complete.')

# Passive H2O deliveries
def passive_water(outport = 31, opentime = 0.015, iti = 15, trials = 100):
	GPIO.setup(outport, GPIO.OUT)
	
	for trial in range(trials):
		GPIO.output(outport, 1)
		time.sleep(opentime)
		GPIO.output(outport, 0)
		print('Trial '+str(trial+1)+' of '+str(trials)+' completed.')
		time.sleep(iti)

	GPIO.cleanup()
	print('Passive H2O deliveries completed')

# Basic nose poking procedure for H2O rewards
def basic_np(outport = 31, opentime = 0.015, iti = [0.5, 1, 1.5], trials = 120):

	trial = 1
	inport = 13
	pokelight = 38
	houselight = 18
	lights = 0
	GPIO.setup(pokelight, GPIO.OUT)
	GPIO.setup(houselight, GPIO.OUT)
	GPIO.setup(inport, GPIO.IN, GPIO.PUD_UP)
	for i in outports:
		GPIO.setup(i, GPIO.OUT)

	while trial <= trials:
		if lights == 0:
			GPIO.output(pokelight, 1)
			GPIO.output(houselight, 1)
			lights = 1
		if GPIO.input(inport) == 0:
			GPIO.output(outport, 1)
			time.sleep(opentime)
			GPIO.output(outport, 0)
			GPIO.output(pokelight, 0)
			GPIO.output(houselight, 0)
			print('Trial '+str(trial)+' of '+str(trials)+' completed.')
			trial += 1
			lights = 0
			if trial <= trials/2:
				delay = floor((random()*(iti[1]-iti[0]))*100)/100+iti[0]
			else:
				delay = floor((random()*(iti[2]-iti[0]))*100)/100+iti[0]
			poketime == time.time()
			while time.time() - poketime < delay:
				if GPIO.input(inport) == 0:
					poketime == time.time()
		

	GPIO.cleanup()
	print('Basic nose poking has been completed. '+str(correct)+' of '+str(trials)+' were correct.')

# Discrimination task training procedure
def disc_train(outports = [31, 33, 35, 37], opentimes = [0.015, 0.015, 0.015, 0.015], iti = [10000, 12000, 14000], trials = 120, blocksize = 10):

	blocked = 1
	trial = 1
	bothpl = 0
	plswitch = 120
	blcounter = 1
	lit = 0
	tarray = []

	inports = [11, 13, 15]
	pokelights = [36, 38, 40]
	houselight = 18
	
	for i in outports:
		GPIO.setup(i, GPIO.OUT)
	for i in inports:
		GPIO.setup(i, GPIO.IN, GPIO.PUD_UP)
	GPIO.setup(houselight, GPIO.OUT)

	if blocked = 1:
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

	while trial <= trials:
		if lights == 0:
			GPIO.output(houselight, 1)
			GPIO.output(pokelights[2], 1)
			lights = 1	
		if GPIO.input(inports[1]) == 0:
			
			
	

	