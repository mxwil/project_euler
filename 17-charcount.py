"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

"""

def get_length(n):

	ONE_TWENTY = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
	TWENTY_NINETY = [0,0,6,6,5,5,5,7,6,6]
	HUNDRED = 7
	AND = 3

	if n == 1000: return 11
	if n < 20:
		return ONE_TWENTY[n]
	elif n < 100:
		o = int(str(n)[1])
		t = int(str(n)[0])
		return ( ONE_TWENTY[o] + TWENTY_NINETY[t] )
	else:
		o = int(str(n)[2])
		t = int(str(n)[1])
		h = int(str(n)[0])
		if t == 0 and o == 0:
			return ONE_TWENTY[h] + HUNDRED
		elif t == 1:
			return ONE_TWENTY[h] + HUNDRED + AND + ONE_TWENTY[int(str(n)[1:])]
		else: 
			return ONE_TWENTY[h] + HUNDRED + AND + TWENTY_NINETY[t] + ONE_TWENTY[o]
	return 0

def sum_length(n):

	l = 0
	for i in range(n):
		l += get_length(i)
	return l
