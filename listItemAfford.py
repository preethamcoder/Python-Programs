def itemAfford(price):
	i = 0
	while(i <= (len(x) - 1)):
		if(price >= x[i]):
			print(a[i])
		i = i + 1

x = [1.12, 1.34, 1.58, 2.61, 2.34, 5.64, 8.84]

a = ["Babba", "Apple", "Mango", "Orange", "Okra", "Muskmellon", "Green Babba"]

print a

print x

print("These are prices of products at respective idices")

print('What is your budget?')

price = float(raw_input()) 

print("With your budget, you can afford: ")

itemAfford(price)






