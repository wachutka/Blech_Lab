import time
import os
import RPi.GPIO as GPIO
import easygui

# List of ports to be listened to for inputs
inports = ['', '', '', '']

# Set the port in inports to inputs
for inport in inports:
	GPIO.setup(inport, GPIO.IN)

# Ask the user for the directory to save the videos in
directory = easygui.diropenbox(msg = 'Select the directory to save the videos from this experiment', title = 'Select directory')
# Change to that directory
os.chdir(directory)

# Counter of trials
trials = [1, 1, 1, 1]

# Run an infinite loop and wait for inputs. Save an appropriately named video for 5 seconds if an input comes in
while True:
	if GPIO.input(inports[0]) == 1:
		filename = 'port' + inports[0] + '_trial' + str(trials[0]) + '.avi'  
		os.system('sudo streamer -q -c /dev/video0 -s 640x480 -f jpeg -t 150 -r 30 -j 75 -w 0 -o %s' %filename)
		trials[0] += 1

	if GPIO.input(inports[1]) == 1:
		filename = 'port' + inports[1] + '_trial' + str(trials[1]) + '.avi'  
		os.system('sudo streamer -q -c /dev/video0 -s 640x480 -f jpeg -t 150 -r 30 -j 75 -w 0 -o %s' %filename)
		trials[1] += 1

	if GPIO.input(inports[2]) == 1:
		filename = 'port' + inports[2] + '_trial' + str(trials[2]) + '.avi'  
		os.system('sudo streamer -q -c /dev/video0 -s 640x480 -f jpeg -t 150 -r 30 -j 75 -w 0 -o %s' %filename)
		trials[2] += 1

	if GPIO.input(inports[3]) == 1:
		filename = 'port' + inports[3] + '_trial' + str(trials[3]) + '.avi'  
		os.system('sudo streamer -q -c /dev/video0 -s 640x480 -f jpeg -t 150 -r 30 -j 75 -w 0 -o %s' %filename)
		trials[3] += 1

# Doesn't really matter as forced exit is needed out of this program
GPIO.cleanup()
	
