#!/usr/bin/python
from time import time
"""


You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
start = time()
is_leap = lambda y: bool((not y % 400) or (y % 100 and not y % 4))
M = [31,28,31,30,31,30,31,31,30,31,30,31]
days, sundays = 2, 0
for year in range(1901,2001):
	if is_leap(year):
		M[1] = 29
	else: 
		M[1] = 28
	for month in range(0,12):
		if days % 7 == 0:
			sundays += 1
		days += M[month]

print "Number of Sundays:",sundays
print "Time taken:", (time() - start),"seconds."

		


