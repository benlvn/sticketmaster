class Groover:

	#########
	###
	## Data related to each Groover's ticket count
	#
	#

	name = ""

	# Number of tickets in possession
	student_tix = 0
	adult_tix = 0

	# Number of tickets sold
	student_sold = 0
	adult_sold = 0

	def __init__(self, name):
		self.name = name


