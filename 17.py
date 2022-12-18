a = None
with open("in.txt") as fp:
	Lines = fp.readlines()
	tot = 0
	for line in Lines:
		l = line.strip()
		a = l

rocks = [
	[
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0],
		[1,1,1,1]
	],
	[
		[0,0,0,0],
		[0,1,0,0],
		[1,1,1,0],
		[0,1,0,0]
	],
	[
		[0,0,0,0],
		[0,0,1,0],
		[0,0,1,0],
		[1,1,1,0]
	],
	[
		[1,0,0,0],
		[1,0,0,0],
		[1,0,0,0],
		[1,0,0,0]
	],
	[
		[0,0,0,0],
		[0,0,0,0],
		[1,1,0,0],
		[1,1,0,0]
	]
]

process = True
steps = int(1000000000000)
ext = 0
if process:
	steps -= 691

	cnt = steps // (640 + 1075)
	steps %= (640 + 1075)

	ext = 1111 
	ext += cnt * (1703 + 1008)

width = 7
height = int(2e5)

bord = [ [0 for i in range(width)] for j in range(height) ]


low = height-1

for i in range(width):
	bord[low][i] = 1


def ok(x,y):
	global bord
	n = len(bord)
	m = len(bord[0])
	return x >= 0 and y >= 0 and x < n and y < m and bord[x][y] == 0

def check(x,y,r):
	global bord
	global rocks
	for i in range(4):
		for j in range(4):
			if rocks[r][i][j] == 1:
				xx = x - (4-i-1)
				yy = y + j
				if not ok(xx,yy):
					return False
	return True

s = 3963 if process else 0
r = 1 if process else 0
last = 0
hg = low

for k in range(steps):
	x,y = low-4,2
	while(True):
		
		# Get pushed
		old = [x,y]
		if a[s] == '>':
			y += 1
		else:
			y -= 1
		s += 1
		s %= len(a)
		
		if not check(x,y,r):
			x,y = old
		# Go down
		old = [x,y]
		x += 1
		if not check(x,y,r):
			x,y = old
			break
	
	for i in range(4):
		for j in range(4):
			if rocks[r][i][j] == 1:
				xx = x - (4-i-1)
				yy = y + j
				assert bord[xx][yy] == 0
				bord[xx][yy] = 1
				low = min(low,xx)
	r += 1
	r %= len(rocks)
res = height - low - 1
res += ext
print(res)
