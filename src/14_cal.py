"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# year = int(input("Input the year : "))
# month = int(input("Input the month : "))

# print(calendar.month(year, month))

user_input = input("Give me a month and year:")

input_list = user_input.split(" ")

if user_input == "":
    print(calendar.month(datetime.today().year, datetime.today().month))
elif not all(num.isdigit() for num in input_list) or len(input_list) > 2 or int(input_list[0]) > 12:
    print("If no input is given, current month and year will be the output\n\
    If number from 1 to 12 is given => month of the current year will be the output")
elif len(input_list) == 1:
    print(calendar.month(datetime.today().year, int(user_input)))
else:
    print(calendar.month(int(input_list[1]), int(input_list[0])))