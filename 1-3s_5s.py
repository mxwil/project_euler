#!/usr/bin/python

def find_sum_3s5s(upto):
    S = 0
    for i in range(0,upto):
        if i % 3 == 0 or i % 5 == 0:                                   
            S += i
    return S

def find_sum_even_fibs(upto):
	x, y, S = 0, 1, 0
	while y < upto:
		if y % 2 == 0:
			S += y
		x, y = y, x + y
	return S

def largest_prime_factor(n):

	i = 2
	while i * i <= n:
		if n % i:
			i += 1 
		else:
			n /= i 
	return n

def is_palindrome(n):
	return True if str(n)[::-1] == str(n) else False

def largest_palindrome():
	print 'Working...'
	x = 0
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			k = i*j
			if is_palindrome(k) and k > x:
				print 'New largest found:',i,'x',j,'=',k
				x = k

def smallest_multiple():
	i = 2520
	while True:
		if not i%20 and not i%19 and not i%18 and not i%17 and not i%16 and not i%15 and not i%14 and not i%13 and not i%12 and not i%11:
			return i
			break
		i += 10

def sum_squares(n):
	x = 0
	for i in range(1,n+1):
		x += i**2
	return x

def square_of_sum(n):
	s = 0
	for i in range(1,n+1):
		s += i
	return s**2

def square_dif(n):
	return square_of_sum(n)-sum_squares(n)
	



    
    
