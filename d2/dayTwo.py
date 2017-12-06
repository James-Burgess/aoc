def getInput():
	#luss all this and do it in a listcomp
 	return([[int(a) for a in unsplit_array.split()] for unsplit_array in open('input.txt').read().split('\n')])

# 	array = []
# 	file = open('input.txt').read()
# 	string_input = file.split('\n')
# 	for string in string_input:
# 		input_list = string.split()
# 		small_array = [int(a) for a in input_list]
# 		array.append(small_array)
#	return(array)



def checksumCalc(array):
	checksum = 0
	for i in array:
		checksum += max(i)-min(i)
	return(checksum)

def evenlyDivisibleValue(large_array):
	checksum = 0
	for array in large_array:
		for j in range(len(array)):
			for k in range(j):
				if array[j] % array[k] == 0: 
					checksum += array[j] // array[k]; break
				if array[k] % array[j] == 0: 
					checksum += array[k] // array[j]; break
	return(checksum)

test_array = [[5,9,2,8],[9,4,7,3],[3,8,6,5]]
array = getInput()

print(checksumCalc(array))


print(evenlyDivisibleValue(array))

