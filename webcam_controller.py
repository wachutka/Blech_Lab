import datetime
import os
import RPi.GPIO as GPIO
import easygui
import numpy as np

# List of ports to be listened to for inputs
inports = ['', '', '', '']
tastes = ['sucrose', 'quinine', 'water', 'nonsense']
video_input = 35 #Integer

# Set the port in inports to inputs
for inport in inports:
	GPIO.setup(int(inport), GPIO.IN)

# Ask the user for the directory to save the videos in
directory = easygui.diropenbox(msg = 'Select the directory to save the videos from this experiment', title = 'Select directory')
# Change to that directory
os.chdir(directory)

# Counter of trials
trials = [1, 1, 1, 1]

# Run an infinite loop and wait for the video input. Save a generically named video for 6 seconds if an input comes in
while True:
	if GPIO.input(video_input) == 1:
		os.system('sudo streamer -q -c /dev/video0 -s 640x480 -f jpeg -t 360 -r 60 -j 75 -w 0 -o generic.avi')
		start = datetime.datetime.now()
		current = datetime.datetime.now()
		delta = current - start
		input_port = None
		while np.abs(delta.total_seconds()) <= 7.0:
			if GPIO.input(int(inports[0])) == 1:
				input_port = 0
			if GPIO.input(int(inports[1])) == 1:
				input_port = 1
			if GPIO.input(int(inports[2])) == 1:
				input_port = 2
			if GPIO.input(int(inports[3])) == 1:
				input_port = 3
			#Update the current time
			current = datetime.datetime.now()
			delta = current - start
				
		#rename the generic.avi file according to the input received
		os.system('mv generic.avi ' + tastes[input_port] + '_trial_' + str(trials[input_port]) + '.avi')
		
		#increment the appropriate counter of trials
		trials[input_port] += 1

# Doesn't really matter as forced exit is needed out of this program
GPIO.cleanup()
	
