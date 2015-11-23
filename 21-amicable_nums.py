#!/usr/bin/python
"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

def d(x):
	S = 1
	if not x & 1:
		S += 2 + x/2
	for i in range(3,int(x**0.5)+1):
		if x % i == 0:
			S += i
			if x / i != i: S+= x / i
	return S

S = 0
for x in range(1000):
	if d(d(x)) == x:
		print 'Amicable numbers:',x,'and',d(x)
		S += x
print S