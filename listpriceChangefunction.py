def changePrice(item, newPrice):
	z = int(a.index(item))
	if(z < 0):
		print("This object does not exist in the list. Please try again.")
	else:
		x[z] = newPrice

x = [1.12, 1.34, 1.58, 2.61, 2.34, 5.64, 8.84]

a = ["Babba", "Apple", "Mango", "Orange", "Okra", "Muskmellon", "Green Babba"]

print a

print x

print("These are prices of products at respective idices")

print("Which price do you want to change?")
item = str(raw_input())

print("What is the new price you want to assign to it?")
newPrice = float(raw_input())

changePrice(item, newPrice)

print a

print x
