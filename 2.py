
win = {
	'A' : 'C',
	'B' : 'A',
	'C' : 'B'
}

lose = {
	'A' : 'B',
	'B' : 'C',
	'C' : 'A'
}

point = {
	'A' : 1,
	'B' : 2,
	'C' : 3
}

mp = {
	'X' : 'A',
	'Y' : 'B',
	'Z' : 'C'
}


score = 0
with open("in.txt") as fp:
	Lines = fp.readlines()
	tot = 0
	for line in Lines:
		x = line.strip().split()
		if x[1] == 'X':
			x[1] = win[x[0]]
		if x[1] == 'Y':
			x[1] = x[0]
		if x[1] == 'Z':
			x[1] = lose[x[0]]
		
		
		score += point[x[1]]
		if x[0] == x[1]:
			score += 3
		if win[x[1]] == x[0]:
			score += 6

print(score)
