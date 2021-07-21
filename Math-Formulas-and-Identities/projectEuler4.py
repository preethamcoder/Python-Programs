sum = 0
sqsum = 0
for i in range(1, 101):
	sum += (i ** 2)
	sqsum += i

print(abs((sqsum ** 2) - sum))