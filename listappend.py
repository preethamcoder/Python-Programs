x = [1.12, 1.34, 1.58, 2.61, 2.34, 5.64, 8.84]

a = ["Babba", "Apple", "Mango", "Orange", "Okra", "Muskmellon", "Green Babba"]

print a

print x

print("These are prices of products at respective idices")

print("Which price do you want to change?")
y = str(raw_input())

z = int(a.index(y))

if(z < 0):
	print("This object does not exist in the list. Please try again.")
else:
	x[z] = x[z] * 0.5

print a

print x


