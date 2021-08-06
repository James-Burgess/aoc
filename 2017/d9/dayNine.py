instructions = [x for x in open('input.txt').read()]

def clean(i):
	c = 0
	while c < len(i):
		if i[c] == "<":
			j = c
			while 1:
				if i[j] != ">":
					break
				if i[j] == "!":
					j += 2
				else:
					j += 1
			del i[c:j]
		c +=1
	l1 = ['{','}']
	l2 = [x for x in i if x in l1]	
	return(l2)


def count(instructions):
	answer = 0
	
	
	i = 0
	while i < (len(instructions)):
		if instructions[i] == '{' and instructions[i+1] == '}':

			back_count = i
			size_count = 1
			

			while instructions[back_count] != '}' and back_count > 0:
				back_count -= 1
				size_count += 1
				print(back_count)

			del instructions[i]
			del instructions[i]


			answer += size_count
			i = 0
		else:
			i += 1

		if instructions[0] == '}': 
			del instructions[0]

		
		print(len(instructions))
		print(''.join(instructions))
		print(answer)
	return(answer+1)



instructions = clean(instructions)
print(count(instructions))


