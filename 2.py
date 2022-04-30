from random import randint

def GenDataSet(n=10):
	l = []
	for i in range(n):
		l.append(randint(0, 5))
	return(l)

def Counter(data: list):
	m = {}
	for i in data:
		if i in m.keys():
			m[i] += 1
		else:
			m[i] = 1 
	return m

def Split(data: list):
	data = Counter(data)
	sl = []
	for i in data.keys():
		l = []
		for j in range(data[i]):
			l.append(i)
		sl.append(l)
	return sl

ds = GenDataSet(randint(1, 15))
print(Split(ds))
print(ds)