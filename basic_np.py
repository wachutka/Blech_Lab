from PyMata.pymata import PyMata
from time import sleep

board = PyMata('/dev/ttyACM0')	# USB port identifier
# Board is a generic variable name and must be changed everywhere in the code if changed here.

trials = 5		# Number of trials

tasteport1 = 2		# Identify output ports
tasteport2 = 3

pokeport1 = 8		# Identify input ports
pokeport2 = 9

tasteduration1 = 2 	# Time valve should be open in seconds
tasteduration2 = 2

iti = 5			# Set ITI

# Set mode on input channels and clear outputs
board.set_pin_mode(pokeport1, board.INPUT, board.DIGITAL)	
board.set_pin_mode(pokeport2, board.INPUT, board.DIGITAL)
#board.digital_write(tasteport1, 0)
#board.digital_write(tasteport2, 0)

trial = 1

while trial < trials:
	if board.digital_read(pokeport1) == 1:
		board.digital_write(tasteport1, 1)
		sleep(tasteduration1)
		board.digital_write(tasteport1, 0)
		print 'Completed trial number', trial
		sleep(iti)
		trial = trial+1
	elif board.digital_read(pokeport2) == 1:
		board.digital_write(tasteport2, 1)
		sleep(tasteduration2)
		board.digital_write(tasteport2, 0)
		print 'Completed trial number', trial
		sleep(iti)
		trial = trial+1

print('It\'s all ogre now')	# Shrek is love, shrek is life
		
