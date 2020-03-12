import datetime
from datetime import *


weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

date = date.today()
day = date.weekday()
now = datetime.now()
time= now.strftime("%H:%M")
print (date)
print (time)
print (weekDays[day])