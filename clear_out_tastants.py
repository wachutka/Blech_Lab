from PyMata.pymata import PyMata
from time import sleep

# Define channels to be used

tastes = [2, 3]		# Enter DIO board port numbers

# How long to leave valves open (seconds)

duration = 20

board = PyMata('/dev/ttyACM0')	# USB port identifier
# Board is a generic variable name and must be changed everywhere in the code if changed here.

for i in tastes:
	board.digital_write(tastes[i],1)

sleep(duration)

for i in tastes:
	board.digital_write(tastes[i],0)

print 'The purge is complete.  This was the most sucessful purge yet.'


