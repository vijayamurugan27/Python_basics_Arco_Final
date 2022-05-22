from datetime import date
from datetime import datetime

my_date = date(1996, 12, 11)
print("Date passed as argument is", my_date)

today = date.today()
print("Today's date is", today)


#for getting year. month, day

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# To get timestamp
date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)


#convert date to string

today = date.today()
print(type(today))
today_1 =str(today)
print(type(today_1))

# Time object to represent time in python


from datetime import time

# calling the constructor hours, minutes, seconds
my_time = time(13, 24, 56)

print("Entered time", my_time)
print("Entered hour", my_time.hour)
print("Entered minute", my_time.minute)
print("Entered second", my_time.second)
print("Entered microsecond", my_time.microsecond)

# To convert the date object to string
time1 = my_time.isoformat()
print("srting representation of the time :", time1)
print(type(time1))

#------------------------------------------

# Datetime class
from datetime import datetime
a = datetime(1999, 12, 12)
print(a)

print("year = ",  a.year)
print( "month = ", a.month)
print( "hour = ", a.hour)
print( "minute =", a.minute)
print("timestamp =  ",a.timestamp())

# calling constructor with 1
# argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)

# Calling constructor with
# 0 argument
my_time = time()
print("\nTime without argument", my_time)


#to get current date and time

from datetime import datetime
today = datetime.now()
print("Current date and time is", today)
print(type(today))

# To convert the datetime to string
today_1 = date_time.isoformat()
print(today_1)
print(type(today_1))


# Timedelta class

from datetime import datetime, timedelta

today = datetime.now()
print("Todays's date and time", today)

time_delta_1 = today +timedelta(days = 2)
time_delta_2 = today +timedelta(days = 730)
print("after two days is ", str(time_delta_1))
print("after two years is ", str(time_delta_2))


# To calculate time difference between two dates and time


time_delta_3 = time_delta_2- today
time_delta_4 = time_delta_1 - today

print("Time difference : =", str(time_delta_3))
print("Time difference : =", str(time_delta_4))

#-----------------------------------------------------------

# datetime timezone conversion

# from python-dateutil-2.8.2 import tz
# tz.tzutc()


# pip install python-dateutil
# # Don't use th ebelow commands
# from dateutil.relativedelta import *
# from dateutil.easter import *
# from dateutil.rrule import *
# from dateutil.parser import *
# from datetime import *
# now = parse("Sat Oct 11 17:13:46 UTC 2003")
# today = now.date()
# year = rrule(YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=FR)[0].year
# rdelta = relativedelta(easter(year), today)
# print("Today is: %s" % today)
# # Today is: 2003-10-11
# print("Year with next Aug 13th on a Friday is: %s" % year)
# # Year with next Aug 13th on a Friday is: 2004
# print("How far is the Easter of that year: %s" % rdelta)
# # How far is the Easter of that year: relativedelta(months=+6)
# print("And the Easter of that year is: %s" % (today+rdelta))
# # And the Easter of that year is: 2004-04-11

# from dateutil import tz

# import datetime
# a = tz.tzutc().utcoffset(datetime.datetime.utcnow())
# print(a)

# b = tz.gettz('US/Pacific')
# print(b)

# # c = tz.gettz('US / Pacific').utcoffset(datetime.datetime.utcnow())
# # print(c)

# abc = tz.gettz('US/Pacific')
# dat = datetime.datetime(2010, 9, 25, 10, 36)
# c = dat.tzinfo
# d = dat.astimezone(tz.tzutc())
# print(abc, dat, c, d)


