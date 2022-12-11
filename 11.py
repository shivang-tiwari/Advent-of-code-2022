from functools import reduce

n = 8
rounds = 10000
monkeys = [[] for i in range(n)]
freq = [0 for i in range(n)]
what = [-1 for i in range(n)]
mod = -1

for k in range(rounds):
	with open("in.txt") as fp:
		Lines = fp.readlines()
		op = 0
		tot = 0
		i = 0
		items = []
		tr = -1
		fl = -1
		for line in Lines:
			l = line.strip().split()
			if len(l) == 0:
				continue
			
			if l[0] == "Monkey":
				i = int(l[1][:-1])
			
			if l[0] == "Starting":
				if freq[i] > 0:
					continue
				items = l[2:]
				for j in range(len(items)):
					if items[j][-1] == ",":
						items[j] = items[j][:-1]
					items[j] = int(items[j])
				
				monkeys[i] = items + monkeys[i]
			
			if l[0] == "Operation:":
				for j in range(len(monkeys[i])):
					worry = monkeys[i][j]
					change = int(l[5]) if l[5] != "old" else worry
					worry = ((worry + change) if l[4] == '+' else (worry * change))
					if mod != -1:
						worry %= mod
					monkeys[i][j] = worry
			
			if l[0] == "Test:":
				what[i] = int(l[-1])
			
			if l[0] == "If":
				if l[1] == "true:":
					tr = int(l[-1])
				else:
					fl = int(l[-1])
					for item in monkeys[i]:
						if item % what[i] == 0:
							monkeys[tr].append(item)
						else:
							monkeys[fl].append(item)
					freq[i] += len(monkeys[i])
					monkeys[i] = []
	
	mod = reduce((lambda x, y: x * y), what)			

freq.sort()
print(freq[-1] * freq[-2])
