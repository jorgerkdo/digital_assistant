import datetime
from datetime import *
import csv
import re

def read_timesheet():
	with open('../data/test.csv') as csv_file:
		
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		info_holder = []
		for row in csv_reader:
			if line_count == 0:
				#print(f'Column names are {", ".join(row)}')
				info_holder.append(row)
				line_count += 1
			else:
				s1 = row[1]
				s2 = row[2]
				s1 = str(s1)
				s2 = str(s2)
				if str(row[3]) == 'y':
					s3 = '00:00'
				else:
					s3 = '01:00'

				format = '%H:%M'
				
				if datetime.strptime(s2, format) > datetime.strptime(s1, format):
					time = datetime.strptime(s2, format) - datetime.strptime(s1, format)

					time = str(time)
					time = time.split(':')
					time = time[0]+':'+time[1]

					if datetime.strptime(time,format)> datetime.strptime(s3, format):
						time = datetime.strptime(time, format) - datetime.strptime(s3, format)
					else:
						pass
					
					time = str(time)
					time = time.split(':')
					row[4] = time[0]+'.'+time[1]
				else:

					if row[1]== '0:00' or row[2] == '0:00':
						row[4] = '0.0'
					else:
						row[4] = 'error'

				info_holder.append(row)
	
		return info_holder


def update_total_hours():
	info_holder = read_timesheet()
	with open('../data/test.csv', "w") as csv_file:
		csv_writer= csv.writer(csv_file)
		for row in info_holder:
			csv_writer.writerow(row)
	return info_holder


def write_day(day, time_in,time_out,lunch):

	info_holder = read_timesheet()
	with open('../data/test.csv', "w") as csv_file:
		
		csv_writer= csv.writer(csv_file)
		for row in info_holder:
		
			if row[0].lower() == day.lower():
				row_update = [row[0], time_in, time_out,lunch,'0:00']
				csv_writer.writerow(row_update)
			else:
				csv_writer.writerow(row)
	


def write_new():

	with open('../data/test.csv', mode='w') as csv_file:
		fieldnames = ['day','in','out','lunch','total hours']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
		for i in days:
			if i == 'Saturday' or i == 'Sunday':
				writer.writerow({'day': i, 'in': '0:00', 'out': '00:00','lunch':'n','total hours':'0'})
			else:
				writer.writerow({'day': i, 'in': '9:00', 'out': '18:00','lunch':'n','total hours':'0'})


def display_timesheet():
	info_holder = read_timesheet()
	worked_hours = 0.00
	for i in info_holder:
		print (i)
	counter = 0
	for i in info_holder:
		
		if counter == 0:
			pass
		else:
			try:
				worked_hours = worked_hours+ (float(i[4]))
			except:
				pass


		counter = counter + 1 
		
	print ('Week Total Hours: ' + str(worked_hours))


def checkin():



	weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

	date_today = date.today()
	day_today = date_today.weekday()
	now_today= datetime.now()
	time_today= now_today.strftime("%H:%M")
	weekday_today = weekDays[day_today]
	info_holder = read_timesheet()

	
	with open('../data/test.csv', "w") as csv_file:
		
		csv_writer= csv.writer(csv_file)
		for row in info_holder:
		
			if row[0].lower() == weekday_today.lower():
				row_update = [row[0], time_today, row[2] , row[3],row[4]]
				csv_writer.writerow(row_update)
			else:
				csv_writer.writerow(row)
	
def checkout():



	weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

	date_today = date.today()
	day_today = date_today.weekday()
	now_today= datetime.now()
	time_today= now_today.strftime("%H:%M")
	weekday_today = weekDays[day_today]
	info_holder = read_timesheet()

	
	with open('../data/test.csv', "w") as csv_file:
		
		csv_writer= csv.writer(csv_file)
		for row in info_holder:
		
			if row[0].lower() == weekday_today.lower():
				row_update = [row[0], row[1] , time_today , row[3],row[4]]
				csv_writer.writerow(row_update)
			else:
				csv_writer.writerow(row)
	

def main():


	#Reads Existing Timesheet
	
	#write_day(info_holder,'Monday')
	#write_new()
	
	#checkin()
	#checkout()
	#write_day('Saturday', '09:00','09:00','n')
	update_total_hours()
	display_timesheet()
	
if __name__ == '__main__':
	main()


