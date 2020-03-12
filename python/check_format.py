import re


r = re.compile('.*:.*')
if r.match('19:00') is not None:
   print ('matches')
