from math import sqrt

def smallestCenterRoute(number):
	row_number = (sqrt(number)+1)//2
	bottom_num = (2*row_number-1)**2
	top_num = (2*(row_number+1)-1)**2
	row_len = (top_num-bottom_num)/4
	center_dis = row_len/2

	centers = [abs(number - (bottom_num + row_len*i +center_dis)) for i in range(4)]
	smallest_distance = min(centers)+row_number
	return(smallest_distance)

number = 1024
print(smallestCenterRoute(number))

