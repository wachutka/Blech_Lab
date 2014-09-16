from PyMata.pymata import PyMata
from time import sleep

board = PyMata('/dev/ttyACM0')	# USB port identifier	
# Board is a generic variable name and must be changed everywhere in the code if changed here.

port = 2		# Enter DIO board port number

duration = 0.008	# How long to leave valve open (seconds)

repeats = 5		# How many times to open valve

Print 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
