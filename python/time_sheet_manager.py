import csv
from datetime import datetime

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
				time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
				time = str(time)
				time = time.split(':')
				time = time[0]+':'+time[1]
				time = datetime.strptime(time, format) - datetime.strptime(s3, format)
				time = str(time)
				time = time.split(':')
				row[4] = time[0]+'.'+time[1]
				info_holder.append(row)
	
		return info_holder


def update_total_hours():
	info_holder = read_timesheet()
	with open('../data/test.csv', "w") as csv_file:
		csv_writer= csv.writer(csv_file)
		for row in info_holder:
			csv_writer.writerow(row)
	return info_holder

def write_timesheet():

	info_holder = read_timesheet()
	with open('../data/employee_file2.csv', mode='w') as csv_file:
		fieldnames = ['emp_name', 'dept', 'birth_month']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

		writer.writeheader()
		writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
		writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})


def write_day(day, time_in,time_out,lunch):

	info_holder = read_timesheet()
	with open('../data/test.csv', "w") as csv_file:
		
		csv_writer= csv.writer(csv_file)
		for row in info_holder:
		
			if row[0] == day:
				row_update = [day, time_in, time_out,lunch,'0:00']
				csv_writer.writerow(row_update)
			else:
				csv_writer.writerow(row)
	


def write_new():

	with open('../data/test.csv', mode='w') as csv_file:
		fieldnames = ['day','in','out','lunch','total hours']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
		for i in days:
			writer.writerow({'day': i, 'in': '9:00', 'out': '18:00','lunch':'n','total hours':'0'})


def display_timesheet():
	info_holder = read_timesheet()
	for i in info_holder:
		print (i)


def main():


	#Reads Existing Timesheet
	
	#write_day(info_holder,'Monday')
	
	update_total_hours()
	display_timesheet()
	#print ('Hello')

if __name__ == '__main__':
	main()


