tot = 9

a = [[] for x in range(tot)]

with open("in.txt") as fp:
	Lines = fp.readlines()
	flag = True
	for line in Lines:
		x = line
		if len(x) <= 1:
			continue
		
		if x[1] == '1':
			flag = False
			continue
		
		if flag:
			j = 0
			for i in range(1,len(x),4):
				if x[i] != ' ':
					a[j].append(x[i])
				j += 1
		
		else:
			x = x.strip()
			cnt = int(x[x.find("move ") + 5:x.find(" from")])
			s = int(x[x.find("from") + 5:x.find(" to")]) - 1
			d = int(x[x.find("to ") + 3:]) - 1
			
			# a[d] = a[s][cnt-1::-1] + a[d]
			a[d] = a[s][:cnt] + a[d]
			a[s] = a[s][cnt:]
		
for i in range(tot):
	print(a[i][0],end="")
