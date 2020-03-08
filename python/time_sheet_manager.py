import csv
from datetime import datetime

with open('../data/test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            s1 = row[1]
            s2 = row[2]
            s1 = str(s1)
            s2 = str(s2)
            if str(row[3]) == 'Yes':
            	s3 = '0:00'
            else:
            	s3 = '1:00'

            format = '%H:%M'
            time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
            time = str(time)       
            time = datetime.strptime(time[:4], format) - datetime.strptime(s3, format)
            print (time)