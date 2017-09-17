#
# Example file for working with Calendars
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2017, 9, 0, 0)
print (str)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2017, 9)
print (str)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
#for i in c.itermonthdays(2017, 9):
#  print (i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
#for name in calendar.month_name:
#  print (name)
#for day in calendar.day_name:
#  print (day)
  
# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for m in range(1,13): # 13 is exclusive
  # returns an array of weeks that represent the month
  cal = calendar.monthcalendar(2017, m)
  # The first Friday has to be within the first two weeks
  weekone = cal[0]
  weektwo = cal[1]
   
  if weekone[calendar.FRIDAY] != 0:
    meetday = weekone[calendar.FRIDAY]
  else:
    # if the first Friday isn't in the first week, it must be in the second
    meetday = weektwo[calendar.FRIDAY]
      
  print ("%10s %2d" % (calendar.month_name[m], meetday))
