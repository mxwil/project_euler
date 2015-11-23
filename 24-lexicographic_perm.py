#!/usr/bin/python
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from math import factorial, floor
from time import time

def nth_perm(n, d):
	
	digits = range(d) #this will initialise an array representing the digits e.g. [0,1,2,3,4,5,6,7,8,9]
	N = n-1 #e.g. 999999
	result = []
	
	for i in range(d-1,-1,-1): #iterate over the digits 9-0
		
		F = factorial(i) 
		D = int(floor(N/F))%10 #get the last digit of the result when we divide N by factorial(i)
		
		result.append(str(digits[D])) #the remainder is the next digit in the permutation
		digits.pop(D)
		
		N %= F #set N to the remainder when divided
		if N == 0: #then we have completed the computation
			break
		
	result += [str(s) for s in digits] #add any unused digits
	
	return (''.join(result)) #return the answer as a string

st = time()
print nth_perm(1000000,10)
print 'Took',time()-st,'seconds.'


