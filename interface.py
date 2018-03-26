from master import Master
import sys

class Interface:

	########
	###
	## A class to hold interface functions
	#
	#

	# Holds the Master data for the app
	# Master holds all other data
	master = None

	# Holds the state of the application
	state = ""

	# Maps states to their functions
	func_map = {}

	def welcome_message(self):
		print("   _____ __  _      __        __                       __           ")
		print("  / ___// /_(_)____/ /_____  / /_____ ___  ____ ______/ /____  _____")
		print("  \__ \/ __/ / ___/ //_/ _ \/ __/ __ `__ \/ __ `/ ___/ __/ _ \/ ___/")
		print(" ___/ / /_/ / /__/ ,< /  __/ /_/ / / / / / /_/ (__  ) /_/  __/ /    ")
		print("/____/\__/_/\___/_/|_|\___/\__/_/ /_/ /_/\__,_/____/\__/\___/_/     ")
		print("                                                                    ")
		print(" ")

		self.state = "main"

	def process_input(self):
		user_input = input("> ")

		if(user_input == 'q'):
			self.state = "quit"

		return user_input

	def run_program(self):
		while(self.state != "quit"):
			self.func_map[self.state]()

		print("Goodbye!")
		return

	def main_menu(self):
		print("### Main menu")
		print("1. Inventory")
		print("2. Give ticekts")
		print("3. New round")
		response = self.process_input()
		if(response == '1'):
			self.state = "inventory"
		elif(response == '2'):
			self.state = "quit"
		elif(response == '3'):
			self.state = "quit"

	def inventory(self):
		print("### Inventory")
		print("Master inventory:")
		print(str(self.master.student_tix) + " student")
		print(str(self.master.adult_tix) + " adult")
		print("Type a name or type 'all' to see Groover inventories")
		response = self.process_input()
		if(response == 'all'):
			self.state = "quit"

	def __init__(self):
		self.master = Master()
		self.state = "welcome"
		self.func_map["welcome"] = self.welcome_message
		self.func_map["main"] = self.main_menu
		self.func_map["inventory"] = self.inventory






