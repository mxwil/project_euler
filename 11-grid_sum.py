#!/usr/bin/python


"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

from time import time

def get_num(m,x,y):
	try:
		return int(m[y][x])
	except IndexError:
		return 0

def search():
	f = open('grid.txt')
	lines = f.read().split('\n')
	m = [line.split() for line in lines]
	k = 0
	result = 0

	#scan rows
	for y in range(0,20):
		for x in range(0,17):
			k += 1
			p = get_num(m,x,y)
			for n in range(x+1,x+4):
				p *= get_num(m,n,y)
				if p > result: 
					result = p
					print 'New highest: Across from',get_num(m,x,y),'at position %d,%d' % (x,y)

	#scan verticals
	for x in range(0,20):
		for y in range(0,17):
			k += 1
			p = get_num(m,x,y)
			for n in range(y+1,y+4):
				p *= get_num(m,x,n)
				if p > result: 
					result = p
					print 'New highest: Down from',get_num(m,x,y),'at position %d,%d' % (x,y)
	#scan diag possibilities
	for x in range(0,20):
		for y in range(0,20):
			if x < 17 and y < 17:
				k += 1
				p = get_num(m,x,y)
				X,Y = x,y
				while True:
					X += 1
					Y += 1
					if (X < x+4 and Y < y+4): 
						p *= get_num(m,X,Y)
					else: break
				if p > result: 
					result = p
					print 'New highest: Diagonally down and right from',get_num(m,x,y),'at position %d,%d' % (x,y)
				p = get_num(m,x,y)
				X,Y = x,y
				while True:
					X -= 1
					Y += 1
					if (X > x-4 and Y < y+4): 
						p *= get_num(m,X,Y)
					else: break
				if p > result: 
					result = p
					print 'New highest: Diagonally down and left from',get_num(m,x,y),'at position %d,%d' % (x,y)

	print 'Checked %d combinations' % (k)
	return result

if __name__ == "__main__":
	t = time()
	print search()
	print "Time taken: {0} secs".format(time()-t)

"""
Terminal output:

New highest: Across from 8 at position 0,0
New highest: Across from 8 at position 0,0
New highest: Across from 8 at position 0,0
New highest: Across from 2 at position 1,0
New highest: Across from 22 at position 2,0
New highest: Across from 78 at position 13,0
New highest: Across from 12 at position 15,0
New highest: Across from 49 at position 0,1
New highest: Across from 40 at position 11,1
New highest: Across from 98 at position 12,1
New highest: Across from 93 at position 8,2
New highest: Across from 51 at position 4,4
New highest: Across from 63 at position 6,4
New highest: Across from 95 at position 8,7
New highest: Across from 91 at position 15,7
New highest: Across from 78 at position 10,8
New highest: Down from 66 at position 15,6
New highest: Diagonally down and left from 89 at position 6,12
Checked 969 combinations
70600674
"""
