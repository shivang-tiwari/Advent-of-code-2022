import sys


pos = []

with open("in.txt") as fp:
	Lines = fp.readlines()
	for line in Lines:
		l = [int(x) for x in line.strip().split(',')]
		pos.append(l)

ans = 6 * len(pos)


for i in range(len(pos)):
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			for dz in [-1,0,1]:
				if abs(dx) + abs(dy) + abs(dz) != 1:
					continue
				d = [dx,dy,dz]
				for j in range(len(pos)):
					if j == i:
						continue
					ok = True
					for k in range(3):
						if pos[i][k] + d[k] != pos[j][k]:
							ok = False
					if ok:
						ans -= 1
						break
					

print(ans)
