def changePrice(item, newPrice):
	if item in priceDict:	
		priceDict[item] = newPrice
	else:
		print("Your item does not exist in the list.")

priceDict = dict(Babba = 1.12, Apple = 1.34, Mango = 1.58, Orange = 2.61, Okra = 2.34, Muskmellon = 5.64, GreenBabba = 8.84)

print(priceDict)

#priceDict["Babba"] = 1.32

#priceDict["Apple"] = 43.04

#priceDict["Timber"] = 32.23
print("Which price do you want to change?")
item = str(raw_input())

print("What is the new price you want to assign to it?")
newPrice = float(raw_input())

changePrice(item, newPrice)

print(priceDict)
