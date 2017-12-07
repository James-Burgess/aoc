### part1
from math import sqrt

def smallestCenterRoute(number):
	row_number = (sqrt(number)+1)//2
	bottom_num = (2*row_number-1)**2
	top_num = (2*(row_number+1)-1)**2
	row_len = (top_num-bottom_num)/4
	center_dis = row_len/2

	centers = [abs(number - (bottom_num + row_len*i + center_dis)) for i in range(4)]
	smallest_distance = min(centers) + row_number
	return(smallest_distance)

number = 1024
print(smallestCenterRoute(number))

###part2
from itertools import count

def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0),(0,0,-1),(1,-1,0),(1,0,1)]:
            for _ in range(s+ds):
                i += di; j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                             for l in range(j-1,j+2))
                yield a[i,j]

def part2(n):
    for x in sum_spiral():
        if x>n: return x
print(part2(363010))