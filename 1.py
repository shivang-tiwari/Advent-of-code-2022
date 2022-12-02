a = []

with open("in.txt") as fp:
	Lines = fp.readlines()
	tot = 0
	for line in Lines:
		x = line.strip()
		if len(x) > 0:
			tot += int(x)
		else:
			a.append(tot)
			tot = 0

a.sort()
print(sum(a[-3:]))
