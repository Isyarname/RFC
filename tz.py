from random import randint, choice
from math import log2

def GenDataSet(size=10):
	data = []
	for i in range(0, size):
		data.append(randint(0,1))
	return data

def Probability(submultitudeSize, multitudeSize):
	return submultitudeSize/multitudeSize

def SEntropy(Pi_1, Pi_2):
	try:
		S = -Pi_1 * log2(Pi_1) - Pi_2 * log2(Pi_2)
	except ValueError:
		S = 0
	return S

def Split(data: list):
	splitPoint = randint(1, len(data)-1)
	data0 = data[:splitPoint]
	data1 = data[splitPoint:]
	return (data0, data1)

def Counter(data: list):
	mainValue = data[0]
	mValueSize = 0
	for i in data:
		if mainValue == i:
			mValueSize += 1
	sValueSize = len(data) - mValueSize
	return (mValueSize, sValueSize)

# Генерируем набор данных
# Вычисляем его энтропию
# Делим на два списка
# Вычисляем энтропию для каждого из списков
# Выводим каждый полученный в ходе эксперимента набор данных,
# и его энтропию 

#[0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
#[0, 0, 0][1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
#[0, 0, 0]

#Выловить ошибку ValueError и опознать группу к которой принадлежит
#набор данных (1 или 0)
#Если ошибки нет(в списке все еще находятся разные данные)
#то мы продолжаем делить список на две части и ловим ошибки
#если не осталось списков с разными данными то соединяем списки
#с одинаковыми данными, и выводим результаты (два списка и тип значений в нём)
try:
	####
	#список не опознан, продолжаем делить его
except ValueError:
	#Список опознан и имеет один тип значений

#["кот", "собака", "черепаха", "черепаха", "кот", "собака", "черепаха", "кот"]