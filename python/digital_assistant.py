#Framestore Digitals Assistant

def main_menu():
	print """
	Welcome to the main menu
	
	Options:
	
	1) Timesheet

	2) Daily Targets

	3) Weekly Schedule

	Other Options:
	menu
	help 
	exit

	"""

def help_menu():
	print """
	This is the help menu
		
	Options:

	Timesheet - Allows you to manage your time card locally, 
	provides hours and overtime calculator

	exit - Stops the program


	"""

def time_sheet():
	timesheet_status = 'running'
	action = None
	started = 'start'
	prompt = '[Timesheet Menu]>>'
	timesheet_menu = """
		Welcome to the timesheet
		Here are your options:

		1) New timesheet

		2) Display timesheet

		3) Update Time Sheet

		Other Options:
		menu 
		exit

		"""
	print (timesheet_menu)

	while (timesheet_status == 'running'):
		if started == 'start':
			print ('What do you want to do today?')
		else:
			print ('What else can I do for you?')

		action = raw_input(prompt)
		started = 'started'

		if action == 'menu':
			print(timesheet_menu)

		if action == 'exit':
			timesheet_status = 'stop'

def main():
	
	assistant_status = 'running'
	action = None
	started = 'start'
	prompt = 'Main Menu>'

	# Main
	print ("Welcome to Framestore's Digital Assistant")

	while(assistant_status == 'running'):

		#Loop for start text
		if started == 'start':
			main_menu()
			print ("What do you want to do today?")
		else:
			print ("What else do you need to do today?")
		#Main Action
		action = raw_input(prompt)

		started = 'started'

		#Main Menu


		if action == 'menu':
			main_menu()


		if action == 'timesheet' or action == '1':
			print ("Great, let's update your timesheet")
			time_sheet()
		if action == 'help':
			help_menu()

		if action == 'exit':
			assistant_status = 'stop'


	print ("Thank you for using this Digital Assistant")



if __name__ == '__main__':
	main()