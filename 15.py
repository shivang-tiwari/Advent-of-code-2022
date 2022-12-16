N = 4000000
pos = []
beac = {}

with open("in.txt") as fp:
	Lines = fp.readlines()
	tot = 0
	for line in Lines:
		l = line.strip().split(':')
		x1 = int(l[0][l[0].find('x=')+2:l[0].find(',')])
		y1 = int(l[0][l[0].find('y=')+2:])
		x2 = int(l[1][l[1].find('x=')+2:l[1].find(',')])
		y2 = int(l[1][l[1].find('y=')+2:])
		pos.append([[x1,y1],[x2,y2]])
		beac[(x2,y2)] = 1


def dis(a,b):
	return abs(a[0]-b[0]) + abs(a[1]-b[1])

def merge(a):
	a.sort()
	res = []
	l,r = a[0]
	for L,R in a:
		if L <= r+1:
			r = max(r,R)
		else:
			res.append([l,r])
			l,r = L,R
	res.append([l,r])
	return res


targ = [0,N]

res = None

for x in range(N+1):
	rgs = []
	for p in pos:
		x1,y1 = p[0]
		x2,y2 = p[1]
		d = dis(p[0],p[1]) - abs(x - x1)
		if d < 0:
			continue
		r = d + y1
		l = y1 - d
		rgs.append([l,r])
	mg = merge(rgs)
	if mg[0][0] <= targ[0] and mg[0][1] >= targ[1]:
		continue
	res = [x,mg[0][1] + 1]
	
x,y = res

print(x*N + y)

