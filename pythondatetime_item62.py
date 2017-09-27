# Python 2.7.14
# Shelley Tennison
# Purpose: Tech Academy drill for Python course


import time
import datetime


portlandTime = datetime.datetime.now().strftime('%H')

portlandHour = int(portlandTime)


newyorkHour = portlandHour + 3
if newyorkHour > 24:
    newyorkHour -= 24

londonHour = portlandHour + 8
if londonHour > 24:
    londonHour -= 24

newyorkOpen = 'Open'
if (newyorkHour < 9 or newyorkHour > 21):
    newyorkOpen = 'Closed'

londonOpen = 'Open'
if (londonHour < 9 or londonHour > 21):
    londonOpen = 'Closed'


print 'It is currently ' + str(portlandTime)+ ' in Portland.' 
print 'It is currently ' + str(newyorkHour)+ ' in New York. The branch is ' +newyorkOpen+ '.'
print 'It is currently ' + str(londonHour)+ ' in London. The branch is ' +londonOpen+ '.'
