#!/usr/bin/python
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from math import factorial
from time import time
def nth_perm(n, d):
	digits, N, result = range(d), n-1, []
	for n in range(d-1,-1,-1):
		F = factorial(n)
		D = int(floor(N/F))%10
		result.append(str(digits[D]))
		digits.pop(D)
		N %= F
		if N == 0: break
	result += [str(s) for s in digits]
	return (''.join(result))

st = time()
print nth_perm(1000000,10)
print 'Took',time()-st,'seconds.'


