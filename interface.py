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
	state = None

	def process_input(self):
		user_input = input("> ")

		if(user_input == 'q'):
			self.state = "quit"

		return user_input

	def run_program(self):
		while(self.state != "quit"):
			self.state()

		print("Goodbye!")
		return

	def welcome_message(self):
		print("   _____ __  _      __        __                       __           ")
		print("  / ___// /_(_)____/ /_____  / /_____ ___  ____ ______/ /____  _____")
		print("  \__ \/ __/ / ___/ //_/ _ \/ __/ __ `__ \/ __ `/ ___/ __/ _ \/ ___/")
		print(" ___/ / /_/ / /__/ ,< /  __/ /_/ / / / / / /_/ (__  ) /_/  __/ /    ")
		print("/____/\__/_/\___/_/|_|\___/\__/_/ /_/ /_/\__,_/____/\__/\___/_/     ")
		print("                                                                    ")
		print(" ")

		self.state = self.main_menu

	def main_menu(self):
		print("### Main menu")
		print("1. Inventory")
		print("2. Give ticekts")
		print("3. Ticket return")
		print("4. New round")
		response = self.process_input()
		if(response == '1'):
			self.state = self.inventory
		elif(response == '2'):
			self.state = self.give_ticekts
		elif(response == '3'):
			self.state = self.ticket_return
		elif(response == '4'):
			self.state = self.new_round

	def inventory(self):
		print("### Inventory")

		print("Master inventory:")
		print("\t$" + str(self.master.money))
		print('\t' + str(self.master.student_tix) + " student")
		print('\t' + str(self.master.adult_tix) + " adult")

		while(True):
			print("Type a name or type 'all' to see Groover inventories")
			print("Type 'main' to go back to the main menu")

			response = self.process_input()
			if(response == 'all'):
				for groover in self.master.groovers:
					print(groover.name)
					print('\t' + str(groover.student_tix) + " student")
					print('\t' + str(groover.adult_tix) + " adult")
			elif(response == 'master'):
				print("Master inventory:")
				print("\t$" + str(self.master.money))
				print('\t' + str(self.master.student_tix) + " student")
				print('\t' + str(self.master.adult_tix) + " adult")
			elif(response == 'main'):
				self.state = self.main_menu
				return
			elif(not self.master.known_groover(response)):
				print("Groover unknown")
			else:
				groover = self.master.get_groover(response)
				print(groover.name)
				print('\t' + str(groover.student_tix) + " student")
				print('\t' + str(groover.adult_tix) + " adult")


	def ticket_return(self):
		print("### Ticket return")

		print("Who is returning tickets?")
		groover = None
		while(groover == None):
			name = self.process_input()
			if(self.master.known_groover(name)):
				groover = self.master.get_groover(name)
			else:
				print("Groover unkown.  Please type a known name")

		print("How much money are they returning?")
		get_money = int(self.process_input())
		self.master.money += get_money

		print("How many student ticekts are they returning?")
		get_student = int(self.process_input())
		groover.student_tix = 0
		self.master.student_tix += get_student

		print("How many adult ticekts are they returning?")
		get_adult = int(self.process_input())
		groover.adult_tix = 0
		self.master.adult_tix += get_adult

		print("Master inventory:")
		print("\t$" + str(self.master.money))
		print('\t' + str(self.master.student_tix) + " student tickets")
		print('\t' + str(self.master.adult_tix) + " adult tickets")

		self.state = self.main_menu

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
			groover = self.master.get_groover(name)

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
		print("There are " + str(self.master.student_tix) + " student and " + str(self.master.adult_tix) 
				+ " adult tickets remaining.")
		self.state = self.main_menu




	def new_round(self):
		print("### New round")

		print("How many new student tickets?")
		new_student = int(self.process_input())
		self.master.total_student = new_student
		self.master.student_tix += new_student

		print("How many new adult tickets?")
		new_adult = int(self.process_input())
		self.master.total_adult = new_adult
		self.master.adult_tix += new_adult

		print("The new round has begun!")
		print("Totals for this round:")
		print(str(self.master.total_student) + " student")
		print(str(self.master.total_adult) + " adult")

		self.state = self.main_menu



	def __init__(self):
		self.master = Master()
		self.state = self.welcome_message






