from PyMata.pymata import PyMata
from time import sleep
from random import shuffle

class blech_board:

	def __init__(self, port = '/dev/ttyACM0'):

		#Warn experimenter that ports are going to switch on, before they are turned off again after initialization
		raw_input('WARNING: Switch off your instruments, all ports are going to turn on. Press ANY KEY to continue')
		self.board = PyMata(port)

		#Look at pymata.py and pymata_command_handler.py if you want to follow the logic. PyMata instances have a _command_handler 			instance in them - this _command_handler instance has two variables - total_pins_discovered and  				number_of_analog_pins_discovered. This sets digital pins 0 to (total_pins_discovered - number_of 			analog_pins_discovered - 1) to 0
		dio = self.board._command_handler.total_pins_discovered - self.board._command_handler.number_of_analog_pins_discovered

		for i in range(dio):
			self.board.digital_write(i, 0)
		
		print 'It is safe to turn your instruments on now. All digital ports have been switched off'

	def calibrate(self, port, on_time, repeats, iti):

		for i in range(repeats):
			
			sleep(iti)
			self.board.digital_write(port, 1)
			sleep(on_time)
			self.board.digital_write(port, 0)

	def passive_deliveries_constant(self, ports = [0, 1, 2, 3], iti = 15.0, deliveries_per_channel = 30, on_time = [0.02,0.02,0.02,0.02]):
		
		num_tastes = len(ports)
		total_deliveries = num_tastes*deliveries_per_channel
		self.delivery_arr = []
		for i in range(total_deliveries):
			self.delivery_arr.append(i%num_tastes)
		shuffle(self.delivery_arr)

		for i in self.delivery_arr:
			
			sleep(iti)
			self.board.digital_write(ports[i], 1)
			sleep(on_time[i])
			self.board.digital_write(ports[i], 0)

	def clear_tastes(self, port, open_time = 200.0):
		
		self.board.digital_write(port, 1)
		sleep(open_time)
		self.board.digital_write(port, 0)

	def np_no_switch(self, poke_ports = [8, 9], taste_ports = [2, 3], deliveries_per_channel = 50, iti = 5.0, on_time = [0.02, 0.02]):

		for i in poke_ports:
			self.board.set_pin_mode(i, self.board.INPUT, self.board.DIGITAL)

		total_deliveries = len(poke_ports)*deliveries_per_channel
		
		delivery_counter = 0
		while (delivery_counter<total_deliveries):
			for i in poke_ports:
				if self.board.digital_read(i) == 0:
					self.board.digital_write(taste_ports[i], 1)
					sleep(iti)
					self.board.digital_write(taste_ports[i], 0)
					print 'Trial ', delivery_counter+1,' of ', total_deliveries, ' done'

					delivery_counter += 1
		print 'All done'

	def np_switching(self, poke_ports = [8, 9], taste_ports = [2, 3], deliveries_per_channel = 30, iti = 15.0, switching_every = 1, on_time = [0.02, 0.02]):
	
		for i in poke_ports:
			self.board.set_pin_mode(i, self.board.INPUT, self.board.DIGITAL)

		total_deliveries = len(poke_ports)*deliveries_per_channel

		self.poke_array = []
		for i in range(total_deliveries):
			self.poke_array.append((i/len(poke_ports))%swiitching_every)
		delivery_counter = 0	

		for i in self.poke_array:
			while True:
				if self.board.digital_read(poke_ports[i]) == 0:
					self.board.digital_write(taste_ports[i], 1)
					sleep(iti)
					self.board.digital_write(taste_ports[i], 0)
					print 'Trial ', delivery_counter+1,' of ', total_deliveries, ' done'
					break
					delivery_counter += 1
		print 'All done'					
					

					
			
		
		

			
		

