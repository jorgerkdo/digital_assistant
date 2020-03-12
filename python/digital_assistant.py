import csv
from datetime import datetime
import time_sheet_manager
from time_sheet_manager import *
import re

#Framestore Digitals Assistant

def main_menu():
	print """
	Welcome to the main menu
	
	Options:
	
	1) Timesheet

	2) Daily Targets

	3) Weekly Schedule

	4) Checkin - Timesheet

	5) Checkout - Timesheet

	Note: This is not linked to mystore, all information is saved locally

	Other Options:
	m = menu
	h = help 
	x = exit

	"""

def help_menu():
	print """
	Welcome to the help menu

		
	Options:

	Timesheet - Allows you to manage your time card 
	locally (not connected to mystore)

	What it offers:
	Locally record your time sheet, calculate the total amount of 
	hours worked during a day

	[Time Sheet Menu]:
	1) Reset Timesheet - Resets your time sheet to a 40 hour week 9:00-18:00
	2) Display Timesheet - Displays all week timesheet plus total hours
	3) Update Day Timesheet - Lets you manually update a day in your week
	4) checkin - Automatically adds the IN -  current time and day to your timesheet
	5) checkout - Automatically adds the OUT - current time and day to your timesheet
	Note: checkin/checkout functions work on the main menu as well for quick access


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

		3) Update Day Time Sheet

		4) Checkin - Timesheet

		5) Checkout - Timesheet
		
		Other Options:
		m = menu 
		x = exit

		"""
	print (timesheet_menu)

	while (timesheet_status == 'running'):
		if started == 'start':
			print ('What do you want to do today?')
		else:
			print ('What else can I do for you?')

		action = raw_input(prompt)
		started = 'started'


		if action == '1':
			print ('You are about to reset your timesheet')
			confirmation = raw_input('Do you wish to proceed? [y/n]>')
			if confirmation == 'y':
				time_sheet_manager.write_new()
				update_total_hours()
				time_sheet_manager.display_timesheet()

		if action == '2':
			update_total_hours()
			time_sheet_manager.display_timesheet()


		if action == '3':
			incorret_format = True
			day = raw_input('Day>')
			
			while incorret_format == True:
				if day.lower() in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
					incorret_format = False
					pass
				else:
					print ('Please input a weekday')
					day = raw_input('Day>')
				
			r = re.compile('.*:.*')
			time_in = raw_input('Time in>')
			incorret_format = True
			while incorret_format == True:

				if r.match(time_in) is not None:
					incorret_format = False
					pass
				else:
					print('Please use 24:00 format')
					time_in = raw_input('Time in>')

			time_out = raw_input('Time Out>')
			incorret_format = True
			while incorret_format == True:
				if r.match(time_out) is not None:
					incorret_format = False
					pass
				else:
					print('Please use 24:00 format')
					time_out = raw_input('Time Out>')


			lunch = raw_input('Did you work through lunch?[y/n]>')
			incorret_format = True
			while incorret_format == True:
				if lunch in ['y','n']:
					incorret_format = False
					pass
				else:
					lunch = raw_input('Did you work through lunch?[y/n]>')

			time_sheet_manager.write_day(day,time_in,time_out,lunch)
			update_total_hours()
			time_sheet_manager.display_timesheet()


		if action == '4':

			confirmation = raw_input('Proceed with checkin? [y/n]>')
			if confirmation == 'y':
				checkin()
				update_total_hours()
				display_timesheet()

		if action == '5':
			confirmation = raw_input('Proceed with checkout? [y/n]>')
			if confirmation == 'y':
				checkout()
				update_total_hours()
				display_timesheet()

		if action == 'h':
			help_menu()

		if action == 'm':
			print(timesheet_menu)

		if action == 'x' or action == 'exit':
			timesheet_status = 'stop'

def main():
	
	assistant_status = 'running'
	action = None
	started = 'start'
	prompt = 'Main Menu>'

	# Main


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


		if action == 'm':
			main_menu()


		if action == 'timesheet' or action == '1':
			print ("Great, let's update your timesheet")
			time_sheet()


		if action == '2':
			print ("Not yet available")
			

		if action == '3':
			print('Not yet available')

		if action == '4':
			confirmation = raw_input('Proceed with checkin? [y/n]>')
			if confirmation == 'y':
				checkin()
				update_total_hours()
				display_timesheet()

		if action == '5':
			confirmation = raw_input('Proceed with checkout? [y/n]>')
			if confirmation == 'y':
				checkout()
				update_total_hours()
				display_timesheet()

		if action == 'h':
			help_menu()

		if action == 'x' or action == 'exit':
			assistant_status = 'stop'


	print ("Thank you for using this Digital Assistant")



if __name__ == '__main__':
	main()