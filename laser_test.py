def laser(laser = 1, ontime = 10, freq = 30, dc = 100):

	import time	

# Setup ports as PWM outputs
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(22, GPIO.OUT)

	laser1 = GPIO.PWM(12, freq)
	laser2 = GPIO.PWM(22, freq)

# Turn lasers on for duration (ontime), at frequency (freq), with duty cycle (dc).
	if laser = 1:
		laser1.start(dc)
		time.sleep(ontime)
		laser1.stop()
	elif laser = 2:
		laser2.start(dc)
		time.sleep(ontime)
		laser2.stop()

	print('Laser test completed.')
