##part1

def getInput():
	file = open('input.txt').read()
	string_input = file.split('\n')
	input_list = []
	for string in string_input:
		input_list.append(string.split())
	return(input_list)

def removeSingles(array):
	master_list = []
	for a in array:
		if len(a) != 2:
			master_list.append(a)
	return(master_list)

def cleanList(master_list):
	for master in master_list:
		master.pop(1)
		master.pop(1)
	return(master_list)


def findKing(master_list):
	keys = [master_list[i][0].strip(',') for i in range(len(master_list))]
	used_key = []
	for key in keys:
		for a in master_list:
			for m in range(1,len(a)):
				word = (a[m].strip(','))
				if key == word:
					used_key.append(key)
	return (set(keys) - set(used_key))


array = getInput()
array = removeSingles(array)
array = cleanList(array)
array = findKing(array)
print(array)


###part2



a2 = getInput()
keys = [[a[0],a[1]] for a in a2]



print(keys)
print(a2)
