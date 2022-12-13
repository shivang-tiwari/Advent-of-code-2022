import json
from functools import cmp_to_key


def comp(a,b):
	if a == b:
		return 0
	if isinstance(a,int) and isinstance(b,int):
		if a < b:
			return -1
		if a == b:
			return 0
		if a > b:
			return 1
	if isinstance(a,int) and isinstance(b,list):
		if len(b) == 0:
			return 1
		x = comp(a,b[0])
		if len(b) == 1:
			return x
		if x == 0:
			x = -1
		return x
		
	if isinstance(a,list) and isinstance(b,int):
		return -1 * comp(b,a)
	
	n = min(len(a),len(b))
	for i in range(n):
		x = comp(a[i],b[i])
		if x != 0:
			return x
	return 1 if len(a) > len(b) else -1

i = 1

items = []

with open("in.txt") as fp:
	Lines = fp.readlines()
	a = None
	b = None
	for line in Lines:
		l = line.strip()
		if len(l) == 0:
			continue
		items.append(json.loads(l))


def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if comp(arr[j] , arr[j + 1]) == 1:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	if not swapped:
		return


t1 = [[2]]
t2 = [[6]]

items.append(t1)
items.append(t2)

bubbleSort(items)

print((1 + items.index(t1)) * (1 + items.index(t2)))
