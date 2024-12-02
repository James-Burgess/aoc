with open('d1.txt') as f:
    lines = f.readlines()

lines = [line.split() for line in lines]
l1 = [l[0] for l in lines]
l2 = [l[1] for l in lines]

c = 0
for i1, i2 in zip(sorted(l1), sorted(l2)):
    c += abs(int(i1) - int(i2))

print(c)


from collections import Counter

c = Counter(l2)

j = 0
for i in l1:
    j += int(i) * c.get(i, 0)

print(j)