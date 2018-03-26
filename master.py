class Master:

	#########
	###
	## He who is called the Master, the wielder of ticketing power
	#
	#

	# Amt currently in posetion
	student_tix = 0
	adult_tix = 0

	# Amt given this round
	total_student = 0
	total_adult = 0

	# List of Groover objects puppets under
	# control of the Master
	groovers = []

	def __init__(self):
		student_tix = 0
		adult_tix = 0

