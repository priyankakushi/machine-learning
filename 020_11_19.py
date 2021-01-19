#We can compare two dates by using the comarison operators like>, >=, and <=

'''from datetime import datetime as dt
#compares the time. if the time is in between 8AM and 4PM, then it prints wor king hours othewise it prints fun hours

if (dt.now().hour > 8) and (dt.now().hour < 18):
    print("Working hours")

else:
    print("Fun Hours")

import calendar
cal = calendar.month(2019,11)
#printing the calendar of December 2018
print(cal)

#printing the calendar of the year 2019
calendar.prcal(2019)

y = 2019
while(y<2026):
    print("Calender of month : ", y, "\n")
    calendar.prcal(y)

    y+=1'''

#datetime

import time
#prin the number of tricks spent since 12AM, 1st January 1970
print(time.time())

#returns a time tuple
print(time.localtime(time.time()))
#print(time.localtime(time.time()))
#print(time.localtime(time.time()))
#print(time.localtime(time.time()))
#print(time.localtime(time.time()))
#print(time.localtime(time.time()))
#print(time.localtime(time.time()))
#print(time.localtime(time.time()))
#print(time.localtime(time.time()))
#print(time.localtime(time.time()))

#returns the formatted time
print(time.asctime(time.localtime(time.time())))
#print(time.asctime(time.localtime(time.time())))
#print(time.asctime(time.localtime(time.time())))
#print(time.asctime(time.localtime(time.time())))
#print(time.asctime(time.localtime(time.time())))
#print(time.asctime(time.localtime(time.time())))
#print(time.asctime(time.localtime(time.time())))
#print(time.asctime(time.localtime(time.time())))
#print(time.asctime(time.localtime(time.time())))
#print(time.asctime(time.localtime(time.time())))


#Each element will be printed after 1 second
'''for i in range(0,6):
    print(i)
    time.sleep(1)'''

'''for a in range(0,5):
    print(a)
    time.sleep(1)

for b in range (0,4):
    print(b)
    time.sleep(1)

for c in range(1,3):
    print(c)
    time.sleep(1)

for d in range(0,7):
    print(d)
    time.sleep(1)

for e in range(0, 6):
    print(e)
    time.sleep(1)

for f in range(0,2):
    print(f)
    time.sleep(1)

for g in range(0,4):
    print(g)
    time.sleep(1)

for h in range(0,10):
    print(h)
    time.sleep(1)'''

# returns the current datetime object
#print(datetime.datetime.now())


#returns the datetime object for the specified date
import datetime
print(datetime.datetime(2018,12, 10))

#from datetime import datetime as dt
#compares the time.if the time is in between 8AM and 16PM, then it prints wor
#king hours otherwise it prints fun hours

#printing the calendar
import calendar;
cal = calendar.month(2018,11)
print(cal)

'''cal = calendar.month(2019,1)
print(cal)

cal = calendar.month(2019,2)
print(cal)

cal = calendar.month(2019, 10)
print(cal)

cal = calendar.month(2019,6)
print(cal)

cal = calendar.month(2019,4)
print(cal)

cal = calendar.month(2015,5)
print(cal)

cal = calendar.month(2019, 8)
print(cal)

cal = calendar.month(2016,4)
print(cal)

cal = calendar.month(2018,3)
print(cal)'''


#printing the calendar of the year 2019

calendar.prcal(2019)

'''calendar.prcal(2011)

calendar.prcal(2012)

calendar.prcal(2013)

calendar.prcal(2014)

calendar.prcal(2015)

calendar.prcal(2016)

calendar.prcal(2017)

calendar.prcal(2018)

calendar.prcal(2019)

calendar.prcal(2020)'''













