def getInput():
# 	array = []
# 	file = open('input.txt').read()
# 	string_input = file.split('\n')
# 	for string in string_input:
# 		input_list = string.split()
# 		small_array = [int(a) for a in input_list]
# 		array.append(small_array)
#	return(array)

#luss all this and do it in a listcomp
 	return([[int(a) for a in string.split()] for string in open('input.txt').read().split('\n')])

def checksumCalc(array):
	checksum = 0
	for i in array:
		checksum += max(i)-min(i)
	print(checksum)

def evenlyDivisibleValue(array):
	checksum = 0
	for i in range(len(array)):
		for j in range(len(array[i])):
			for k in range(j):
				if array[i][j] % array[i][k] == 0: 
					ans = array[i][j] / array[i][k]
					checksum += ans
					break
				if array[i][k] % array[i][j] == 0:
					ans = array[i][k] / array[i][j]
					checksum += ans
					break
	return(checksum)



array = getInput()
checksumCalc(array)

test_array = [[5,9,2,8],[9,4,7,3],[3,8,6,5]]
print(evenlyDivisibleValue(array))

