from random import randint, choice
from math import log2

def GenDataSet(n=10):
	l = []
	for i in range(n):
		l.append(randint(0, 1))
	return(l)

def Probability(submultitudeSize, multitudeSize):
	return submultitudeSize/multitudeSize

def SEntropy(Pi_1, Pi_2): #получает вероятность
	try:
		S = -Pi_1 * log2(Pi_1) - Pi_2 * log2(Pi_2)
	except ValueError:
		S = 0
	return S
def Split(data: list):
	p = randint(1, len(data)-1)
	l1 = data[:p]
	l2 = data[p:]
	return [l1, l2]

def Counter(data: list):
	mValueSize = 0
	mainValue = data[0]
	for i in data:
		if i == mainValue:
			mValueSize += 1
	sValueSize = len(data) - mValueSize
	return mValueSize, sValueSize

def abgyosh(data):
	n1, n2 = Counter(data)
	pr1 = Probability(n1, len(data))
	pr2 = 1 - pr1
	entropy = SEntropy(pr1, pr2)
	return {"entropy":entropy, "fvs":n1, "svs":n2}

ds = GenDataSet()
BolishoySpisok = []
BolishoySpisok.append(ds)
BolishoySpisok.extend(Split(ds))
for i in BolishoySpisok:
	print(abgyosh(i))