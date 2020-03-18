def itemAfford(budget):	
	for i in priceDict:
		if (budget >= priceDict[i]):
			print(i)
	

priceDict = dict(Babba = 0.12, Apple = 0.34, Mango = 0.58, Orange = 1.61, Okra = 1.34, Muskmellon = 4.64, GreenBabba = 7.84)

print(priceDict)

print("What is your budget?")
budget = float(raw_input())

print("With your budget, you can afford: ")


itemAfford(budget)


