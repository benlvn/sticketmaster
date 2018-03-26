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
	state = "welcome"

	# Maps states to their functions
	func_map = {"welcome": welcome_message(),
				"main": main_menu(),
				"inventory": inventory()}

	def __init__():
		master = None

	def welcome_message():
		print("   _____ __  _      __        __                       __           ")
		print("  / ___// /_(_)____/ /_____  / /_____ ___  ____ ______/ /____  _____")
		print("  \__ \/ __/ / ___/ //_/ _ \/ __/ __ `__ \/ __ `/ ___/ __/ _ \/ ___/")
		print(" ___/ / /_/ / /__/ ,< /  __/ /_/ / / / / / /_/ (__  ) /_/  __/ /    ")
		print("/____/\__/_/\___/_/|_|\___/\__/_/ /_/ /_/\__,_/____/\__/\___/_/     ")
		print("                                                                    ")
		print(" ")

	def process_input():
		user_input = input("> ")

		if(user_input = 'q'):
			state = "quit"

	def run_program():
		while(state != "quit"):
			func_map[state]()

		print("Goodbye!")
		return




	def main_menu():
		print("### Main menu")
		print("1. Inventory")
		print("2. Give ticekts")
		print("3. New round")
		response = process_input("> ")
		if(response == '1'):
			state = "inventory"
		elif(response == '2'):
			state = "quit"
		elif(response == '3'):
			state = "quit"

	def inventory():
		print("### Inventory")
		print("Master inventory:")
		print("%d student", master.student_tix)
		print("%d adult", master.adult_tix)
		print("Type a name or type 'all' to see Groover inventories")
		response = process_input("> ")
		if(response == '1'):
			state = "inventory"
		elif(response == '2'):
			state = "quit"
		elif(response == '3'):
			state = "quit"




