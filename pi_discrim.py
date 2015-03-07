# Discrimination task for Blech Lab

import time
from math import floor
from random import random
import RPi.GPIO as GPIO

# Clear tastant lines
def clearout(outports = ['', '', '', ''], dur = 5):
	for i in outports:
		GPIO.setup(i, GPIO.OUT)

	for i in outports:
		GPIO.output(i, True)
	time.sleep(dur)
	for i in outports:
		GPIO.output(i, False)

	GPIO.cleanup()
	print('Tastant line clearing complete.')

# Calibrate tastant lines
def calibrate(outports = ['', '', '', ''], opentime = 0.015, repeats = 5):
	for i in outports:
		GPIO.setup(i, GPIO.OUT)

	for rep in range(repeats):
		for i in outports:
			GPIO.output(i, True)
		time.sleep(opentime)
		for i in outports:
			GPIO.output(i, False)

	GPIO.cleanup()
	print('Calibration procedure complete.')

# Passive H2O deliveries
def passive_water(outport = , opentime = 0.015, iti = 15, trials = 100):
	GPIO.setup(outport, GPIO.OUT)
	
	for trial in range(trials):
		GPIO.output(outport, True)
		time.sleep(opentime)
		GPIO.output(outport, False)
		print('Trial '+str(trial+1)+' of '+str(trials)+' completed.')
		time.sleep(iti)

	GPIO.cleanup()
	print('Passive H2O deliveries completed')

# Basic nose poking procedure for H2O rewards
def basic_np(outport = [], opentime = 0.015, iti = [0.5, 1, 1.5], trials = 120):
	trial = 1
	inport = ''
	GPIO.setup(inport, GPIO.IN, GPIO.PUD_UP)
	for i in outports:
		GPIO.setup(i, GPIO.OUT)

	while trial <= trials:
		if GPIO.input(inport) == 1:
			GPIO.output(outport, True)
			time.sleep(opentime)
			GPIO.output(outport, False)
			print('Trial '+str(trial)+' of '+str(trials)+' completed.')
			trial += 1
			if trial <= trials/2:
				delay = floor((random()*(iti[1]-iti[0]))*100)/100+iti[0]
				time.sleep(delay)
			else:
				floor((random()*(iti[2]-iti[0]))*100)/100+iti[0]
				time.sleep(delay)		
		

	GPIO.cleanup()
	print('Basic nose poking has been completed. '+str(correct)+' of '+str(trials)+' were correct.')

# Discrimination task training procedure
def disc_train(outports = ['','','',''], opentimes = [0.015, 0.015, 0.015, 0.015], iti = [10000, 12000, 14000], trials = 120):
	bothpl = 0
	plswitch = 120
	inports = ['', '', '']
	tarray = []
	for i in outports:
		GPIO.setup(i, GPIO.OUT)
	for i in inports:
		GPIO.setup(i, GPIO.IN, GPIO.PUD_UP)
	for i in range(trials):
	
	

	
