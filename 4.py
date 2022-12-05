def ok(a,b):
	if a[1] < b[0] or b[1] < a[0]:
		return 0
	return 1

with open("in.txt") as fp:
	Lines = fp.readlines()
	tot = 0
	ans = 0
	for line in Lines:
		x = line.strip()
		x = x.split(',')
		for i in range(len(x)):
			x[i] = [int(y) for y in x[i].split('-')]
		ans += ok(x[0],x[1])

print(ans)
