N = 1000
bord = [['.' for y in range(N)] for x in range(N)]

start = [0,500]
lim = 0
with open("in.txt") as fp:
	Lines = fp.readlines()
	tot = 0
	for line in Lines:
		l = line.strip().split(' -> ')
		a = [x.split(',') for x in l]
		for i in range(1,len(a)):
			y1,x1 = [int(z) for z in a[i-1]]
			y2,x2 = [int(z) for z in a[i]]
			lim = max(lim,x1,x2)
			if x1 == x2:
				for y in range(min(y1,y2),max(y1,y2)+1):
					bord[x1][y] = '#'
			else:
				for x in range(min(x1,x2),max(x1,x2)+1):
					bord[x][y1] = '#'
			

lim += 2		
cnt = 0
bord[start[0]][start[1]] = '+'

for j in range(N):
	bord[lim][j] = '#'


while(True):
	x,y = start
	flag = False
	while x+1 < N:
		if bord[x+1][y] == '.':
			x += 1
			continue
		if bord[x+1][y-1] == '.':
			x += 1
			y -= 1
			continue
		if bord[x+1][y+1] == '.':
			x += 1
			y += 1
			continue
		flag = True
		break
	if not flag:
		break
	else:
		bord[x][y] = 'o'
		if [x,y] == start:
			break
	cnt += 1
cnt += 1
print(cnt)
