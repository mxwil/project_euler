"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""

def primes(n):
    if n<=2: return []
    sieve=[True] * (n+1)
    for x in range( 3, int(n**0.5)+1, 2):
        for y in range( 3, (n//x)+1, 2):
            sieve[(x*y)]=False
    return [2]+[i for i in range(3, n, 2) if sieve[i]]

def is_pan(n):
	all_digits = (range(1,10))
	digits = len(str(n))
	d = all_digits[0:digits]
	l = [int(X) for X in list(str(n))]
	u = []
	for x in l:
		if ( not x in u ) and x in d:
			u.append(x)
	if len(u) == digits:
		return True
	return False

def find_pan_primes(n):
	biggest = 0
	for prime in primes(n):
		if is_pan(prime):
			print prime
			if prime > biggest: biggest = prime
	print "Finished"
	return biggest

