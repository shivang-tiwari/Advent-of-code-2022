from collections import Counter

dis = 14

with open("in.txt") as fp:
	Lines = fp.readlines()
	flag = True
	for line in Lines:
		x = line.strip()
		for i in range(dis,len(x)):
			if len(Counter(x[i-dis:i]).keys()) == dis:
				print(i)
				break
