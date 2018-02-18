##part 1
instructions = [int(x) for x in open('input.txt').read().split('\n')]

def findExit(instructions):
	current_index = instructions[0]
	count = 0 

	while current_index < len(instructions):
		step = instructions[current_index]	
		instructions[current_index] = step + 1
		current_index += step
		count += 1

	return(count)

print(findExit(instructions))


## part 2 
instructions = [int(x) for x in open('input.txt').read().split('\n')]

def findFunnyExit(instructions):
	current_index = instructions[0]
	count = 0 

	while current_index < len(instructions):
		step = instructions[current_index]

		if instructions[current_index] >= 3:	
			instructions[current_index] = step - 1
		else:
			instructions[current_index] = step + 1

		current_index += step
		count += 1

	return(count)

print(findFunnyExit(instructions))