from master import Master
from groover import Groover
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
		print("3. Ticket return")
		print("4. New round")
		response = self.process_input()
		if(response == '1'):
			self.state = "inventory"
		elif(response == '2'):
			self.state = "give_ticekts"
		elif(response == '3'):
			self.state = "quit"
		elif(response == '4'):
			self.state = "new_round"

	def inventory(self):
		print("### Inventory")
		print("Master inventory:")
		print(str(self.master.student_tix) + " student")
		print(str(self.master.adult_tix) + " adult")
		print("Type a name or type 'all' to see Groover inventories")
		response = self.process_input()
		if(response == 'all'):
			self.state = "quit"

	def give_ticekts(self):
		print("### Give Tickets")
		print("Who would you like to give tickets to?")
		name = self.process_input()
		groover = None
		if(not self.master.known_groover(name)):
			print("Groover unknown, adding Groover")
			groover = Groover(name)
			self.master.groovers += [groover]
		else:
			groover = self.master.groovers[groover]

		print("How many student tickets do they want?")
		give_student = int(self.process_input())
		groover.student_tix += give_student
		self.master.student_tix -= give_student

		print("How many adult tickets do they want?")
		give_adult = int(self.process_input())
		groover.adult_tix += give_adult
		self.master.adult_tix -= give_adult

		print(str(groover.name) + " now has " + str(groover.student_tix) + " student ticekts and "
				+ str(groover.adult_tix) + " adult ticekts.")
		print("There are " + str(self.master.student_tix) + " stduent and " + str(self.master.adult_tix) 
				+ " adult tickets remaining.")
		self.state = "main"




	def new_round(self):
		print("### New round")
		new_adult = 0
		response = ""
		while(not response.isdigit()):
			print("How many new student tickets?")
			response = self.process_input()
		self.master.total_student = int(response)
		self.master.student_tix = int(response)
		response = ""
		while(not response.isdigit()):
			print("How many new adult tickets?")
			response = self.process_input()
		self.master.total_adult = int(response)
		self.master.adult_tix = int(response)
		print("The new round has begun!")
		print("Totals for this round:")
		print(str(self.master.total_student) + " student")
		print(str(self.master.total_adult) + " adult")
		self.state = "main"



	def __init__(self):
		self.master = Master()
		self.state = "welcome"
		self.func_map["welcome"] = self.welcome_message
		self.func_map["main"] = self.main_menu
		self.func_map["inventory"] = self.inventory
		self.func_map["new_round"] = self.new_round
		self.func_map["give_ticekts"] = self.give_ticekts






