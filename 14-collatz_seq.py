#!/usr/bin/python
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

import time
start = time.time()

def collatz(n):
	x, s = n, [n]
	while x != 1:
		if x % 2 == 0:
			x = x/2
		else: x = 3*x + 1
		s.append(x)
	return s

def collatz_count(n, c=1):
	while n > 1:
		c += 1
		if n % 2 == 0:
			n = n/2
		else: 
			n = 3*n + 1
	return c

def find(n):
	m = [0,0]
	for x in range(n):
		if x % 100000 == 0: 
			print 'Progress:',(float(x)/float(n) * 100),'%'
		c = collatz_count(x)
		if c > m[1]:
			m[0] = x
			m[1] = c

	return m

e = time.time() - start
m = find(1000000)
print "Found %s at length %s in %s seconds" % (m[1],m[0],e)
