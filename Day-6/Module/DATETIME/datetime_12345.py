# Python datetime module

# In Python, date and time are not a data type of their own, but a module named datetime can be imported to work with the date as well as time. Python Datetime module comes built into Python, so there is no need to install it externally. 

# Python Datetime module supplies classes to work with date and time. These classes provide a number of functions to deal with dates, times and time intervals. Date and datetime are an object in Python, so when you manipulate them, you are actually manipulating objects and not string or timestamps. 

# The DateTime module is categorized into 6 main classes – 

#     date – An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Its attributes are year, month and day.
#     time – An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. Its attributes are hour, minute, second, microsecond, and tzinfo.
#     datetime – Its a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.
#     timedelta – A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
#     tzinfo – It provides time zone information objects.
#     timezone – A class that implements the tzinfo abstract base class as a fixed offset from the UTC (New in version 3.2).

#--------------------------------------------------------------------------------------------------------------------------------------
# Date class

# The date class is used to instantiate date objects in Python. 
# When an object of this class is instantiated, it represents a
#  date in the format YYYY-MM-DD. Constructor of this class needs three mandatory 
#  arguments year, month and date.

# Constructor syntax:  

# class datetime.date(year, month, day)

# The arguments must be in the following range –  

#     MINYEAR <= year <= MAXYEAR
#     1 <= month <= 12
#     1 <= day <= number of days in the given month and year

# Note – If the argument is not an integer it will raise a TypeError and if it is
#  outside the range a ValueError will be raised. 
# Example 1: Date object representing date in Python

# Python program to
# demonstrate date class

# import the date class
from datetime import date
from time import strftime

# initializing constructor
# and passing arguments in the
# format year, month, date
my_date = date(1996, 12, 11)

print("Date passed as argument is", my_date)

# Uncommenting my_date = date(1996, 12, 39)
# will raise an ValueError as it is
# outside range

# uncommenting my_date = date('1996', 12, 11)
# will raise a TypeError as a string is
# passed instead of integer

#--------------------------------------------------------------------
# Get Current Date

# To return the current local date today() function of date class is used. today() 
# function comes with several attributes (year, month and day). 
# These can be printed individually. 

# Python program to
# print current date

from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)

#----------------------------------------------------------------
# Get Today’s Year, Month, and Date

# We can get the year, month, and date attributes from the date object using the year,
#  month and date attribute of the date class.

from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# Get date from Timestamp

# We can create date objects from timestamps y=using the fromtimestamp() method.
#  The timestamp is the number of seconds from 1st January 1970 at UTC to a particular date.
from datetime import datetime

# Getting Datetime from timestamp
date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)


# Convert Date to String

# We can convert date object to a string representation 
# using two functions isoformat() and strftime().

from datetime import date

# calling the today
# function of date class
today = date.today()

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))

# # List of Date class Methods
# Function Name   	Description
# ctime()	            Return a string representing the date
# fromisocalendar()	Returns a date corresponding to the ISO calendar
# fromisoformat()	    Returns a date object from the string representation of the date
# fromordinal()	    Returns a date object from the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1
# fromtimestamp()	    Returns a date object from the POSIX timestamp
# isocalendar()	    Returns a tuple year, week, and weekday
# isoformat()	        Returns the string representation of the date
# isoweekday()	    Returns the day of the week as integer where Monday is 1 and Sunday is 7
# replace()	        Changes the value of the date object with the given parameter
# strftime()	        Returns a string representation of the date with the given format
# timetuple()	        Returns an object of type time.struct_time
# today()	            Returns the current local date
# toordinal()	        Return the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1
# weekday()	        Returns the day of the week as integer where Monday is 0 and Sunday is 6

#---------------------------------------------------------------------------------------------

# Time class

# The time class creates the time object which represents local time, independent of any day. 

# Constructor Syntax: 

#     class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

# All the arguments are optional. tzinfo can be None otherwise all the attributes
#  must be integer in the following range – 

#     0 <= hour < 24
#     0 <= minute < 60
#     0 <= second < 60
#     0 <= microsecond < 1000000
#     fold in [0, 1]



# Time object representing time in Python

# Python program to
# demonstrate time class

from datetime import time

# calling the constructor
my_time = time(13, 24, 56)

print("Entered time", my_time)

# calling constructor with 1
# argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)

# Calling constructor with
# 0 argument
my_time = time()
print("\nTime without argument", my_time)

# Uncommenting time(hour = 26)
# will rase an ValueError as
# it is out of range

# uncommenting time(hour ='23')
# will raise TypeError as
# string is passed instead of int

# Get hours, minutes, seconds, and microseconds

# After creating a time object, its attributes can also be printed separately. 

from datetime import time

Time = time(11, 34, 56)

print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

#--------------------------------------------------------------
# Convert Time object to String

# We can convert time object to string using the isoformat() method.

from datetime import time

# Creating Time object
Time = time(12,24,36,1212)

# Converting Time object to string
time1 = Time.isoformat()
print("String Representation:", time1)
print(type(time1))


# #---------------------------------------------------------
# List of Time class Methods
# Function Name	Description
# dst()	Returns tzinfo.dst() is tzinfo is not None
# fromisoformat()	Returns a time object from the string representation of the time
# isoformat()	Returns the string representation of time from the time object
# replace()	Changes the value of the time object with the given parameter
# strftime()	Returns a string representation of the time with the given format
# tzname()	Returns tzinfo.tzname() is tzinfo is not None
# utcoffset()	Returns tzinfo.utcffsets() is tzinfo is not None



#----------------------------------------------------------------------------------


# Datetime class

# The DateTime class contains information on both date and time.
#  Like a date object, datetime assumes the current Gregorian calendar extended in both
#   directions; like a time object, datetime assumes there are exactly 3600*24 seconds in 
#   every day.

# Constructor Syntax: 

#     class datetime.datetime(year, month, day, hour=0, minute=0, 
# second=0, microsecond=0, tzinfo=None, *, fold=0) 
     

# The year, month and day arguments are mandatory. tzinfo can be None, 
# rest all the attributes must be an integer in the following range –  

#     MINYEAR <= year <= MAXYEAR
#     1 <= month <= 12
#     1 <= day <= number of days in the given month and year
#     0 <= hour < 24
#     0 <= minute < 60
#     0 <= second < 60
#     0 <= microsecond < 1000000
#     fold in [0, 1]

# Note – Passing an argument other than integer will 
# raise a TypeError and passing arguments outside the range will raise ValueError.
# Python program to
# demonstrate datetime object

from datetime import datetime

# Initializing constructor
a = datetime(1999, 12, 12)
print(a)

# Initializing constructor
# with time parameters as well
print("year = ",  a.year)
print( "month = ", a.month)
print( "hour = ", a.hour)
print( "minute =", a.minute)
print("  timestamp =  ",a.timestamp())


# Current date and time

# You can print the current date and time using the 
# Datetime.now() function. now() function returns the current local date and time. 

from datetime import datetime

# Calling now() function
today = datetime.now()
print(type(today))
print("Current date and time is", today)

# Convert Python Datetime to String
today_1 = date_time.isoformat()
print(today_1)
print(type(today_1))

# List of Datetime Class Methods
# Function Name	Description
# astimezone()	Returns the DateTime object containing timezone information.
# combine()	Combines the date and time objects and return a DateTime object
# ctime()	Returns a string representation of date and time
# date()	Return the Date class object
# fromisoformat()	Returns a datetime object from the string representation of the date and time
# fromordinal()	Returns a date object from the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1. The hour, minute, second, and microsecond are 0
# fromtimestamp()	Return date and time from POSIX timestamp
# isocalendar()	Returns a tuple year, week, and weekday
# isoformat()	Return the string representation of date and time
# isoweekday()	Returns the day of the week as integer where Monday is 1 and Sunday is 7
# now()	Returns current local date and time with tz parameter
# replace()	Changes the specific attributes of the DateTime object
# strftime()	Returns a string representation of the DateTime object with the given format
# strptime()	Returns a DateTime object corresponding to the date string
# time()	Return the Time class object
# timetuple()	Returns an object of type time.struct_time
# timetz()	Return the Time class object
# today()	Return local DateTime with tzinfo as None
# toordinal()	Return the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1
# tzname()	Returns the name of the timezone
# utcfromtimestamp()	Return UTC from POSIX timestamp
# utcoffset()	Returns the UTC offset
# utcnow()	Return current UTC date and time
# weekday()	Returns the day of the week as integer where Monday is 0 and Sunday is 6


#-------------------------------------------------------------------------------------

# Timedelta class

# Python timedelta class is used for calculating differences in dates 
# and also can be used for date manipulations in Python. It is one of the easiest ways 
# to perform date manipulations.

# Constructor syntax:  

#     class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
#     Returns : Date 

# Add days to datetime object



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

# Operations supported by Timedelta Class
# Operator	Description
# Addition (+)	Adds and returns two timedelta objects
# Subtraction (-)	Subtracts and returns two timedelta objects
# Multiplication (*)	Multiplies timedelta object with float or int 
# Division (/)	Divides the timedelta object with float or int
# Floor division (//)	Divides the timedelta object with float or int and return the int of floor value of the output 
# Modulo (%)	Divides two timedelta object and returns the remainder
# +(timedelta)	Returns the same timedelta object
# -(timedelta)	Returns the resultant of -1*timedelta
# abs(timedelta)	Returns the +(timedelta) if timedelta.days > 1=0 else returns -(timedelta)
# str(timedelta)	Returns a string in the form (+/-) day[s],  HH:MM:SS.UUUUUU
# repr(timedelta)	Returns the string representation in the form of the constructor call


#-----------------------------------------------------------------
# Format Datetime

# Formatting Datetime can be very necessary as the date representation may differe from
#  place to place. Like in some countries it can be yyyy-mm-dd and in other country it can 
# be dd-mm-yyyy. To format Python Datetime strptime and strftime functions can be used.
# Python Datetime strftime

# strftime() method converts the given date, time or datetime object to the a string
#  representation of the given format.


# Example: Python Datetime format


from datetime import datetime, timedelta

today = datetime.now()
print("Todays's date and time without formatting : ", today)

print("----------------------------------------------------------")
# help(strftime it's not working in my system.)
# today_a = datetime.now()
# print("Todays's date and time without formatting : ", today_a)

# today_1 = datetime.today_a("%a %m %y")
# print("Format_1",today_1)


# today_1 = today("%A %-m %Y")
# print("Format_2",today_1)


# today_1 = today("%-I %p %S")
# print("Format_3",today_1)


# today_1 = today("%-j")
# print("Format_4",today_1)

# pip install python-dateutil
