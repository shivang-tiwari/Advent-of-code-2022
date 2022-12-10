width = 40
height = 6
checkpoint = 20
delta = 40
ans = 0
cyc = 0
x = 1

bord = [[' '] * width for i in range(height)]

i = 0
j = 0

def check():
	global ans
	global cyc
	global x
	global checkpoint
	global delta
	global bord
	global i
	global j
	
	if abs(x-j) <= 1:
		bord[i][j] = '█'
	
	j += 1
	if j == width:
		j = 0
		i += 1
	

with open("in.txt") as fp:
	Lines = fp.readlines()
	tot = 0
	for line in Lines:
		l = line.strip().split()
		if l[0] == "noop":
			check()
			cyc += 1
		else:
			check()
			cyc += 1
			check()
			x += int(l[1])
			cyc += 1

for p in bord:
	print(''.join(p))
