import functools
ID = {}

nodes = []
val = []
inp = []
with open("in.txt") as fp:
	Lines = fp.readlines()
	tot = 0
	for line in Lines:
		l = line.strip().split(';')
		name = l[0][l[0].find("alve ")+5:l[0].find(" has")]
		rate = int(l[0][l[0].find("rate=")+5:])
		ID[name] = len(ID)
		inp.append(l[1])
		val.append(rate)
		if rate > 0:
			nodes.append(ID[name])

n = len(ID)

start = ID['AA']

graph = [[] for i in range(n)]

dist = []

for i in range(n):
	if "valves" in inp[i]:
		nbrs = inp[i][inp[i].find("valves ")+7:].split(',')
		nbrs = [x.strip() for x in nbrs]
	else:
		nbrs = inp[i][inp[i].find("valve ")+6:].split()
	for x in nbrs:
		graph[i].append(ID[x])


def floydWarshall(graph):
	V = len(graph)
	INF = int(1e9)
	
	dist = [[INF for i in range(n)] for j in range(n)]
	
	for i in range(n):
		for x in graph[i]:
			dist[i][x] = 1
	
	for k in range(V):
		for i in range(V):
			for j in range(V):
				dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
	return dist		 


dist = floydWarshall(graph)

@functools.lru_cache(maxsize=None)
def solve(i,vis,time):
	if time <= 1:
		return 0
	global graph
	global val
	global nodes
	best_take = 0
	best_no_take = 0
	for x in nodes:
		if vis & (1 << x) == 0:
			vis ^= 1 << x
			best_no_take = max(best_no_take,solve(x,vis,time - dist[i][x]))
			best_take = max(best_take,solve(x,vis,time - dist[i][x] - 1))
			vis ^= 1 << x
	best_take += (time - 1) * val[i]
	return max(best_take,best_no_take)



vis = 0
tot = 30
print(solve(ID['AA'],vis,tot))
