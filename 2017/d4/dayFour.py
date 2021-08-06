def phraseTest(phrase):
	phrase_array = phrase.split(" ")
	for i in range(len(phrase_array)):
	    for j in range(i + 1, len(phrase_array)):
	        if phrase_array[i] == phrase_array[j]:
	        	return False
	        if ''.join(sorted(phrase_array[i])) == ''.join(sorted(phrase_array[j])):
	        	return False
	return True

import sys
y = sys.stdin.read()
x = y.split('\n')
count = 0

for i in x:
	if phraseTest(i):
		count +=1

print("working %s / total %s " %(count, len(x)))

