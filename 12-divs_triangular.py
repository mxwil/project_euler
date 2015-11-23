def tri(n):
	return [sum(range(1,x)) for x in range(1,n+1)]

def divisors(x):
	count = 0
	for i in range(1,int(x**0.5)+1):
		if x % i == 0:
			print i
			if i != x/i:
				count += 2
			else:
				count += 1
	return count

def find_500(u):
	m = 0
	tris = tri(u)
	for x in tris:
		if divisors(x) >= 500:
			return x

